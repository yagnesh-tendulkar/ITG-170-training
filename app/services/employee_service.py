from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee_schema import EmployeeCreate, EmployeeUpdate


class EmployeeService:
    """Service layer for employee business logic and database operations."""

    def __init__(self, db: Session):
        """
        Initialize the EmployeeService with a database session.

        Args:
            db: SQLAlchemy session for database operations.
        """
        self.db = db

    def create_employee(self, employee_data: EmployeeCreate) -> Employee:
        """
        Create a new employee record.

        Args:
            employee_data: EmployeeCreate schema with employee details.

        Returns:
            Employee: The created employee object.

        Raises:
            ValueError: If email is already registered.
        """
        existing_employee = self.db.query(Employee).filter(
            Employee.email == employee_data.email
        ).first()
        if existing_employee:
            raise ValueError("Email already registered.")

        new_employee = Employee(**employee_data.model_dump())
        self.db.add(new_employee)
        self.db.commit()
        self.db.refresh(new_employee)
        return new_employee

    def get_all_employees(
        self,
        skip: int = 0,
        limit: int = 100,
        search_name: Optional[str] = None,
        department: Optional[str] = None,
        is_active: Optional[bool] = None,
    ) -> List[Employee]:
        """
        Retrieve all employees with optional filtering and pagination.

        Args:
            skip: Number of records to skip (default 0).
            limit: Maximum number of records to return (default 100).
            search_name: Optional search string to filter by first or last name.
            department: Optional filter by department.
            is_active: Optional filter by active status.

        Returns:
            List[Employee]: List of employee records matching filters.
        """
        query = self.db.query(Employee)

        if search_name:
            query = query.filter(
                (Employee.first_name.ilike(f"%{search_name}%"))
                | (Employee.last_name.ilike(f"%{search_name}%"))
            )

        if department:
            query = query.filter(Employee.department == department)

        if is_active is not None:
            query = query.filter(Employee.is_active == is_active)

        employees = query.offset(skip).limit(limit).all()
        return employees

    def get_employee_by_id(self, employee_id: int) -> Optional[Employee]:
        """
        Retrieve a single employee by ID.

        Args:
            employee_id: The ID of the employee to retrieve.

        Returns:
            Optional[Employee]: The employee object if found, None otherwise.
        """
        employee = self.db.query(Employee).filter(
            Employee.id == employee_id
        ).first()
        return employee

    def get_employees_by_department(self, department: str) -> List[Employee]:
        """
        Retrieve all employees in a specific department.

        Args:
            department: The department name to filter by.

        Returns:
            List[Employee]: List of employees in the department.
        """
        employees = self.db.query(Employee).filter(
            Employee.department == department
        ).all()
        return employees

    def search_employees_by_name(self, search_query: str) -> List[Employee]:
        """
        Search employees by first or last name.

        Args:
            search_query: Search string to match against names.

        Returns:
            List[Employee]: List of employees matching the search query.
        """
        employees = self.db.query(Employee).filter(
            (Employee.first_name.ilike(f"%{search_query}%"))
            | (Employee.last_name.ilike(f"%{search_query}%"))
        ).all()
        return employees

    def update_employee(
        self,
        employee_id: int,
        employee_update: EmployeeUpdate,
    ) -> Optional[Employee]:
        """
        Update an existing employee record.

        Args:
            employee_id: The ID of the employee to update.
            employee_update: EmployeeUpdate schema with fields to modify.

        Returns:
            Optional[Employee]: The updated employee object if found, None otherwise.

        Raises:
            ValueError: If the new email is already registered by another employee.
        """
        employee = self.db.query(Employee).filter(
            Employee.id == employee_id
        ).first()
        if not employee:
            return None

        if employee_update.email and employee_update.email != employee.email:
            existing_email = self.db.query(Employee).filter(
                Employee.email == employee_update.email,
                Employee.id != employee_id,
            ).first()
            if existing_email:
                raise ValueError("Email already registered by another employee.")

        update_data = employee_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(employee, key, value)

        self.db.commit()
        self.db.refresh(employee)
        return employee

    def delete_employee(self, employee_id: int) -> bool:
        """
        Delete an employee record by ID.

        Args:
            employee_id: The ID of the employee to delete.

        Returns:
            bool: True if deletion was successful, False if employee not found.
        """
        employee = self.db.query(Employee).filter(
            Employee.id == employee_id
        ).first()
        if not employee:
            return False

        self.db.delete(employee)
        self.db.commit()
        return True

    def get_active_employees(
        self,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Employee]:
        """
        Retrieve all active employees.

        Args:
            skip: Number of records to skip (default 0).
            limit: Maximum number of records to return (default 100).

        Returns:
            List[Employee]: List of active employee records.
        """
        employees = self.db.query(Employee).filter(
            Employee.is_active == True
        ).offset(skip).limit(limit).all()
        return employees

    def count_employees(self) -> int:
        """
        Get the total count of employees.

        Returns:
            int: Total number of employees in the database.
        """
        count = self.db.query(Employee).count()
        return count

    def count_employees_by_department(self, department: str) -> int:
        """
        Get the count of employees in a specific department.

        Args:
            department: The department name to count employees for.

        Returns:
            int: Number of employees in the department.
        """
        count = self.db.query(Employee).filter(
            Employee.department == department
        ).count()
        return count
