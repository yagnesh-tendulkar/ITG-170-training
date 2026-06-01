from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.auth_schema import TokenResponse, UserRegister

# JWT Configuration
SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    """Service layer for authentication and authorization operations."""

    def __init__(self, db: Session):
        """
        Initialize the AuthService with a database session.

        Args:
            db: SQLAlchemy session for database operations.
        """
        self.db = db

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash a plain text password using bcrypt.

        Args:
            password: Plain text password to hash.

        Returns:
            str: Hashed password.
        """
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verify a plain text password against a hashed password.

        Args:
            plain_password: Plain text password to verify.
            hashed_password: Hashed password to compare against.

        Returns:
            bool: True if passwords match, False otherwise.
        """
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(
        data: dict,
        expires_delta: Optional[timedelta] = None,
    ) -> str:
        """
        Create a JWT access token.

        Args:
            data: Dictionary containing token claims (e.g., user_id).
            expires_delta: Optional token expiration time delta.

        Returns:
            str: Encoded JWT token.
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(
                minutes=ACCESS_TOKEN_EXPIRE_MINUTES
            )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def register_user(self, user_data: UserRegister) -> User:
        """
        Register a new user account with password hashing.

        Args:
            user_data: UserRegister schema with user credentials and role.

        Returns:
            User: The created user object.

        Raises:
            ValueError: If email or username already exists.
        """
        existing_email = self.db.query(User).filter(
            User.email == user_data.email
        ).first()
        if existing_email:
            raise ValueError("Email already registered.")

        existing_username = self.db.query(User).filter(
            User.username == user_data.username
        ).first()
        if existing_username:
            raise ValueError("Username already taken.")

        hashed_password = self.hash_password(user_data.password)
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hashed_password,
            role=user_data.role,
            is_active=True,
            is_verified=False,
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """
        Authenticate a user by email and password.

        Args:
            email: User email address.
            password: User password in plain text.

        Returns:
            Optional[User]: The authenticated user if credentials are valid, None otherwise.
        """
        user = self.db.query(User).filter(User.email == email).first()
        if not user:
            return None

        if not self.verify_password(password, user.hashed_password):
            return None

        if not user.is_active:
            return None

        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Retrieve a user by email address.

        Args:
            email: User email address to search for.

        Returns:
            Optional[User]: The user object if found, None otherwise.
        """
        user = self.db.query(User).filter(User.email == email).first()
        return user

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Retrieve a user by user ID.

        Args:
            user_id: User ID to search for.

        Returns:
            Optional[User]: The user object if found, None otherwise.
        """
        user = self.db.query(User).filter(User.id == user_id).first()
        return user

    def get_current_user(self, token: str) -> Optional[User]:
        """
        Decode JWT token and retrieve current authenticated user.

     
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id: int = payload.get("sub")
            if user_id is None:
                raise ValueError("Invalid token claims.")
        except JWTError as exc:
            raise ValueError("Invalid or expired token.") from exc

        user = self.get_user_by_id(user_id)
        if user is None:
            raise ValueError("User not found.")

        return user

    def create_login_response(self, user: User) -> TokenResponse:
        """
        Create a TokenResponse with JWT access token for logged-in user.

        Args:
            user: Authenticated user object.

        Returns:
            TokenResponse: Token response with access token and bearer type.
        """
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = self.create_access_token(
            data={"sub": user.id},
            expires_delta=access_token_expires,
        )
        return TokenResponse(access_token=access_token, token_type="bearer")

    def verify_token(self, token: str) -> bool:
        """
        Verify if a JWT token is valid without decoding.

        Args:
            token: JWT access token to verify.

        Returns:
            bool: True if token is valid, False otherwise.
      

        user = self.get_user_by_id(user_id)
        if not user:
            return False

        if not self.verify_password(old_password, user.hashed_password):
            raise ValueError("Old password is incorrect.")

        user.hashed_password = self.hash_password(new_password)
        self.db.commit()
        self.db.refresh(user)
        return True

    def verify_email(self, user_id: int) -> bool:
       
        user = self.get_user_by_id(user_id)
        if not user:
            return False  """
        Mark a user's email as verified.

        Args:
            user_id: ID of the user to verify.

        Returns:

        user.is_verified = True
        self.db.commit()
        self.db.refresh(user)
        return True

    def deactivate_user(self, user_id: int) -> bool:
        """
        Deactivate a user account.

        Args:
            user_id: ID of the user to deactivate.

        Returns:
            bool: True if deactivation was successful, False if user not found.
      

    def activate_user(self, user_id: int) -> bool:
      
        user = self.get_user_by_id(user_id)
        if not user:
            return False

        user.is_active = True
        self.db.commit()
        self.db.refresh(user)
        return True
