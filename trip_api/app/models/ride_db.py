# app/models/ride_db.py
from app.schemas.ride_schema import RideRequest, RideStatus

# Seeds our mock ride-hailing tracker database
db_rides = {
    101: {
        "id": 101,
        "passenger_name": "Sarah Connor",
        "pickup_location": "Cyberdyne HQ",
        "dropoff_location": "Safe House B",
        "estimated_fare": 32.00,
        "status": RideStatus.REQUESTED,
        "driver_name": None
    }
}