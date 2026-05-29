# RideSharing API (trip_api)

A minimal learning FastAPI project providing a simple ridesharing API.

## Overview

This service implements a small in-memory ride management API with endpoints to request, list, retrieve, and cancel rides. It's intended for learning and development, not production use.

## Endpoints

Base path: `/api/v1`

- `POST /api/v1/rides` — Request a new ride. Accepts JSON body matching `RideRequest`:
  - `rider_name` (string)
  - `pickup` (string)
  - `destination` (string)
  Returns created `RideResponse` with `id` and `status`.

- `GET /api/v1/rides` — List all rides. Optional query param `status` to filter by ride status (`requested`, `in_progress`, `completed`, `cancelled`).

- `GET /api/v1/rides/{ride_id}` — Retrieve a ride by id.

- `DELETE /api/v1/rides/{ride_id}` — Cancel a ride (allowed only when status is `requested`). Returns `204 No Content` on success.

## Schemas

Defined under `app/schemas/ride_schema.py`:
- `RideRequest` — input for creating rides
- `RideResponse` — response schema for rides
- `RideStatus` — enum for ride lifecycle states

## How to run

From the repository root run (recommended):

```bash
cd /home/miracle/Desktop/Training/API/trip_api
uvicorn app.main:app --reload --app-dir /home/miracle/Desktop/Training/API/trip_api --port 8001
```

The API will be available at `http://127.0.0.1:8001` and interactive docs at `http://127.0.0.1:8001/docs`.

## Dependencies

- Python 3.10+
- FastAPI
- Uvicorn

Install with:

```bash
pip install fastapi uvicorn
```

## Notes

- Data is stored in memory (`app/models/ride_db.py`) and will be reset when the server restarts.
- The project includes a custom `RideSharingException` handler that returns structured error responses.

If you want, I can add examples for `curl` or a Postman collection next.