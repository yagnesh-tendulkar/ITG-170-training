# ─────────────────────────────────────────────
# models.py
#
# LEARNING NOTE:
# SQLAlchemy "models" represent database tables as Python classes.
# Each class = one table. Each attribute with Column() = one column.
#
# Key concepts:
#   - Column types: String, Integer, Boolean, DateTime, Text
#   - relationship(): lets us navigate between related tables (like JOIN)
#   - ForeignKey(): links one table's row to another table's row
# ─────────────────────────────────────────────

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database import Base


class User(Base):
    """
    Represents the 'users' table.
    Each row = one registered user.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)

    # We NEVER store plain text passwords — always store the hashed version!
    hashed_password = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # One user can have MANY reviews (one-to-many relationship)
    # back_populates links this to the 'owner' attribute in Review
    reviews = relationship("Review", back_populates="owner", cascade="all, delete-orphan")


class Review(Base):
    """
    Represents the 'reviews' table.
    Each row = one code review session.
    """
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)

    # ForeignKey links this review to a specific user
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    title = Column(String(200), nullable=False)
    language = Column(String(50), nullable=False)

    # Text = large string (no length limit) — good for storing code
    code_snippet = Column(Text, nullable=False)

    # AI results stored as JSON string
    bugs = Column(Text, default="[]")
    optimizations = Column(Text, default="[]")
    best_practices = Column(Text, default="[]")
    summary = Column(Text, default="")

    # Score out of 100 from AI
    overall_score = Column(Float, default=0.0)

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Many reviews belong to ONE user
    owner = relationship("User", back_populates="reviews")
