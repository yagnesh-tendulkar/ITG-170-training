from sqlalchemy import Column, Integer, String

from app.models import Base


class RequestLog(Base):
    __tablename__ = "request_logs"

    id = Column(Integer, primary_key=True)

    request_id = Column(String)

    method = Column(String)

    endpoint = Column(String)

    status_code = Column(Integer)

    response_time = Column(Integer)