from datetime import date
from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.attendance import Attendance
from app.schemas.attendance_schema import AttendanceCreate, AttendanceUpdate


class AttendanceService:

    def __init__(self, db: Session):
       
        self.db = db

    def create_attendance(self, attendance_data: AttendanceCreate) -> Attendance:
        
        existing_attendance = self.db.query(Attendance).filter(
            Attendance.employee_id == attendance_data.employee_id,
            Attendance.attendance_date == attendance_data.attendance_date,
        ).first()
        if existing_attendance:
            raise ValueError(
                "Attendance already marked for this employee on this date."
            )

        new_attendance = Attendance(**attendance_data.model_dump())
        self.db.add(new_attendance)
        self.db.commit()
        self.db.refresh(new_attendance)
        return new_attendance

    def get_all_attendance(
        self,
        skip: int = 0,
        limit: int = 100,
        status_filter: Optional[str] = None,
        employee_id: Optional[int] = None,
        sort_by: str = "attendance_date",
    ) -> List[Attendance]:
        
        query = self.db.query(Attendance)

        if employee_id:
            query = query.filter(Attendance.employee_id == employee_id)

        if status_filter:
            query = query.filter(Attendance.status == status_filter)

        if sort_by == "attendance_date":
            query = query.order_by(Attendance.attendance_date.desc())
        elif sort_by == "employee_id":
            query = query.order_by(Attendance.employee_id)

        attendance_records = query.offset(skip).limit(limit).all()
        return attendance_records

    def get_attendance_by_id(self, attendance_id: int) -> Optional[Attendance]:
      
        attendance = self.db.query(Attendance).filter(
            Attendance.id == attendance_id
        ).first()
        return attendance

    def get_attendance_by_employee(
        self,
        employee_id: int,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Attendance]:
        
        attendance_records = self.db.query(Attendance).filter(
            Attendance.employee_id == employee_id
        ).order_by(Attendance.attendance_date.desc()).offset(skip).limit(limit).all()
        return attendance_records

    def get_attendance_by_date(
        self,
        attendance_date: date,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Attendance]:
        
        attendance_records = self.db.query(Attendance).filter(
            Attendance.attendance_date == attendance_date
        ).offset(skip).limit(limit).all()
        return attendance_records

    def filter_attendance_by_status(
        self,
        status: str,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Attendance]:
        
        attendance_records = self.db.query(Attendance).filter(
            Attendance.status == status
        ).order_by(Attendance.attendance_date.desc()).offset(skip).limit(limit).all()
        return attendance_records

    def update_attendance(
        self,
        attendance_id: int,
        attendance_update: AttendanceUpdate,
    ) -> Optional[Attendance]:
       
        attendance = self.db.query(Attendance).filter(
            Attendance.id == attendance_id
        ).first()
        if not attendance:
            return None

        update_data = attendance_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(attendance, key, value)

        self.db.commit()
        self.db.refresh(attendance)
        return attendance

    def delete_attendance(self, attendance_id: int) -> bool:
       
        attendance = self.db.query(Attendance).filter(
            Attendance.id == attendance_id
        ).first()
        if not attendance:
            return False

        self.db.delete(attendance)
        self.db.commit()
        return True

    def get_attendance_count_by_status(self, status: str) -> int:
        
        count = self.db.query(Attendance).filter(
            Attendance.status == status
        ).count()
        return count

    def get_employee_attendance_count(self, employee_id: int) -> int:
     
        count = self.db.query(Attendance).filter(
            Attendance.employee_id == employee_id
        ).count()
        return count

    def get_attendance_for_period(
        self,
        employee_id: int,
        start_date: date,
        end_date: date,
    ) -> List[Attendance]:
        
        """
        attendance_records = self.db.query(Attendance).filter(
            Attendance.employee_id == employee_id,
            Attendance.attendance_date >= start_date,
            Attendance.attendance_date <= end_date,
        ).order_by(Attendance.attendance_date).all()
        return attendance_records
