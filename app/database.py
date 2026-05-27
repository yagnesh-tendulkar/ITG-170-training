from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# =========================
# DATABASE CONNECTION
# =========================

DATABASE_URL = "mysql+pymysql://root:M1racle%40123@localhost:3306/fastapi_db"

# =========================
# ENGINE
# =========================

engine = create_engine(DATABASE_URL)

# =========================
# SESSION
# =========================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# =========================
# BASE CLASS
# =========================

Base = declarative_base()