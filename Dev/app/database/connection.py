from sqlmodel import SQLModel, create_engine, Session

sqlite_url = "sqlite:///dev_platform.db"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})


def init_db():
    SQLModel.metadata.create_all(engine)


def get_database_session():
    with Session(engine) as session:
        yield session


def boot_database():
    """Convenience wrapper used during app startup to initialize the database."""
    init_db()
