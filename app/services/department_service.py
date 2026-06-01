from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department_schema import DepartmentCreate, DepartmentUpdate


class DepartmentService:

    def __init__(self, db: Session):
        
        self.db = db

    def create_department(self, department_data: DepartmentCreate) -> Department:
        
        existing_department = self.db.query(Department).filter(
            Department.name == department_data.name
        ).first()
        if existing_department:
            raise ValueError("Department name already exists.")

        new_department = Department(**department_data.model_dump())
        self.db.add(new_department)
        self.db.commit()
        self.db.refresh(new_department)
        return new_department

    def get_all_departments(
        self,
        skip: int = 0,
        limit: int = 100,
        search_name: Optional[str] = None,
        is_active: Optional[bool] = None,
    ) -> List[Department]:
        """
        Retrieve all departments with optional filtering and pagination.

        Args:
            skip: Number of records to skip (default 0).
            limit: Maximum number of records to return (default 100).
            search_name: Optional search string to filter by department name.
            is_active: Optional filter by active status.

        Returns:
            List[Department]: List of department records matching filters.
        """
        query = self.db.query(Department)

        if search_name:
            query = query.filter(Department.name.ilike(f"%{search_name}%"))

        if is_active is not None:
            query = query.filter(Department.is_active == is_active)

        departments = query.offset(skip).limit(limit).all()
        return departments

    def get_department_by_id(self, department_id: int) -> Optional[Department]:
        """
        Retrieve a single department by ID.

        Args:
            department_id: The ID of the department to retrieve.

        Returns:
            Optional[Department]: The department object if found, None otherwise.
        """
        department = self.db.query(Department).filter(
            Department.id == department_id
        ).first()
        return department

    def get_department_by_name(self, name: str) -> Optional[Department]:
        """
        Retrieve a department by its unique name.

        Args:
            name: The name of the department to retrieve.

        Returns:
            Optional[Department]: The department object if found, None otherwise.
        """
        department = self.db.query(Department).filter(
            Department.name == name
        ).first()
        return department

    def search_departments(self, search_query: str) -> List[Department]:
        """
        Search departments by name.

        Args:
            search_query: Search string to match against department names.

        Returns:
            List[Department]: List of departments matching the search query.
        """
        departments = self.db.query(Department).filter(
            Department.name.ilike(f"%{search_query}%")
        ).all()
        return departments

    def update_department(
        self,
        department_id: int,
        department_update: DepartmentUpdate,
    ) -> Optional[Department]:
        """
        Update an existing department record.

        Args:
            department_id: The ID of the department to update.
            department_update: DepartmentUpdate schema with fields to modify.

        Returns:
            Optional[Department]: The updated department object if found, None otherwise.

        Raises:
            ValueError: If the new name is already registered by another department.
        """
        department = self.db.query(Department).filter(
            Department.id == department_id
        ).first()
        if not department:
            return None

        if department_update.name and department_update.name != department.name:
            existing_name = self.db.query(Department).filter(
                Department.name == department_update.name,
                Department.id != department_id,
            ).first()
            if existing_name:
                raise ValueError("Department name already exists.")

        update_data = department_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(department, key, value)

        self.db.commit()
        self.db.refresh(department)
        return department

    def delete_department(self, department_id: int) -> bool:
        """
        Delete a department record by ID.

        Args:
            department_id: The ID of the department to delete.

        Returns:
            bool: True if deletion was successful, False if department not found.
        """
        department = self.db.query(Department).filter(
            Department.id == department_id
        ).first()
        if not department:
            return False

        self.db.delete(department)
        self.db.commit()
        return True

    def get_active_departments(
        self,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Department]:
        """
        Retrieve all active departments.

        Args:
            skip: Number of records to skip (default 0).
            limit: Maximum number of records to return (default 100).

        Returns:
            List[Department]: List of active department records.
        """
        departments = self.db.query(Department).filter(
            Department.is_active == True
        ).offset(skip).limit(limit).all()
        return departments

    def count_departments(self) -> int:
        """
        Get the total count of departments.

        Returns:
            int: Total number of departments in the database.
        """
        count = self.db.query(Department).count()
        return count

    def count_active_departments(self) -> int:
        """
        Get the count of active departments.

        Returns:
            int: Number of active departments in the database.
        """
        count = self.db.query(Department).filter(
            Department.is_active == True
        ).count()
        return count
