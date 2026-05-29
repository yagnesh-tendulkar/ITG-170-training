# app/api/v1/rides.py
from fastapi import APIRouter, status, Query, Path
from typing import List, Optional

from app.schemas.ride_schema import RideRequest, RideStatusUpdate, RideStatus
from app.schemas.error_schema import APIErrorResponse
from app.models.ride_db import db_rides
from app.core.exceptions import RideSharingException

router = APIRouter()

# --- 1. POST: Request a New Ride (Input Body Validation) ---
@router.post(
    "/", 
    status_code=status.HTTP_201_CREATED, 
    response_model=dict,
    responses={400: {"model": APIErrorResponse}}
)
async def request_ride(ride: RideRequest):
    """
    Takes an input data payload body to book a trip.
    Throws a 400 bad request error if the Ride ID is taken.
    """
    if ride.id in db_rides:
        raise RideSharingException(
            status_code=status.HTTP_400_BAD_REQUEST,
            error_summary="Booking Conflict",
            detail=f"Ride ID {ride.id} has already been captured by the system."
        )
    
    # Store data format matching our mock system
    new_ride = ride.model_dump()
    new_ride["status"] = RideStatus.REQUESTED
    new_ride["driver_name"] = None
    
    db_rides[ride.id] = new_ride
    return new_ride


# --- 2. GET: List & Filter Bookings (Query Parameters) ---
@router.get("/", response_model=List[dict])
async def list_rides(
    status_filter: Optional[RideStatus] = Query(None, description="Filter trips by their current state"),
    min_fare: Optional[float] = Query(None, description="Filter for trips that cost at least this amount", gt=0)
):
    """
    Retrieves rides. Demonstrates Query Parameters to filter 
    live results seamlessly.
    """
    results = list(db_rides.values())
    
    if status_filter:
        results = [r for r in results if r["status"] == status_filter]
    if min_fare:
        results = [r for r in results if r["estimated_fare"] >= min_fare]
        
    return results


# --- 3. PUT: Dispatch / Driver Updates (Path Parameter & Input Body) ---
@router.put(
    "/{ride_id}", 
    response_model=dict,
    responses={404: {"model": APIErrorResponse}}
)
async def update_ride_status(
    ride_id: int = Path(..., description="Target ride sequence database ID", gt=0),
    update_payload: RideStatusUpdate = None
):
    """
    Uses a Path Parameter to locate the record and an Input Body to 
    safely mutate the ride status.
    """
    if ride_id not in db_rides:
        raise RideSharingException(
            status_code=status.HTTP_404_NOT_FOUND,
            error_summary="Ride Record Missing",
            detail=f"Cannot assign status changes. Ride tracking index {ride_id} does not exist."
        )
        
    current_ride = db_rides[ride_id]
    current_ride["status"] = update_payload.status
    if update_payload.driver_name:
        current_ride["driver_name"] = update_payload.driver_name
        
    db_rides[ride_id] = current_ride
    return current_ride


# --- 4. DELETE: Cancel Request (Path Parameter with Business Logic Rules) ---
@router.delete(
    "/{ride_id}", 
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"model": APIErrorResponse}, 422: {"model": APIErrorResponse}}
)
async def cancel_ride(ride_id: int = Path(..., gt=0)):
    """
    Uses a Path Parameter to evaluate resource state. 
    Returns 204 No Content if cancellation succeeds.
    Throws 422 Unprocessable if a driver has already picked up the passenger.
    """
    if ride_id not in db_rides:
        raise RideSharingException(
            status_code=status.HTTP_404_NOT_FOUND,
            error_summary="Ride Not Found",
            detail=f"Cannot cancel booking. Reference ID {ride_id} is invalid."
        )
        
    targeted_ride = db_rides[ride_id]
    
    # Business logic verification rule
    if targeted_ride["status"] in [RideStatus.DRIVER_ASSIGNED, RideStatus.COMPLETED]:
        raise RideSharingException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            error_summary="Cancellation Denied",
            detail=f"This ride cannot be cancelled because its state is already '{targeted_ride['status']}'."
        )
        
    del db_rides[ride_id]
    return None