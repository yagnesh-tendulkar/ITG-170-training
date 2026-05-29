# app/schemas/ride_schema.py
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class RideStatus(str, Enum):
    REQUESTED = "requested"
    DRIVER_ASSIGNED = "driver_assigned"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class RideRequest(BaseModel):
    id: int = Field(..., description="Unique booking tracking ID")
    passenger_name: str = Field(..., min_length=2, max_length=50, example="Alice Smith")
    pickup_location: str = Field(..., min_length=3, example="123 Main St, New York")
    dropoff_location: str = Field(..., min_length=3, example="JFK Airport Terminal 4")
    estimated_fare: float = Field(..., gt=0, example=45.50)

class RideStatusUpdate(BaseModel):
    status: RideStatus = Field(..., description="The target lifecycle status transition")
    driver_name: Optional[str] = Field(None, min_length=2, example="John Doe")