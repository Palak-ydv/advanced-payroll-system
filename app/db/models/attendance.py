"""Attendance model"""
from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey, Date, Float, Text
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.core.constants import AttendanceStatus

class Attendance(Base):
    """Attendance model for tracking employee attendance"""
    __tablename__ = "attendance"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    attendance_date = Column(Date, nullable=False)
    status = Column(Enum(AttendanceStatus), default=AttendanceStatus.ABSENT, nullable=False)
    check_in_time = Column(DateTime, nullable=True)
    check_out_time = Column(DateTime, nullable=True)
    working_hours = Column(Float, default=0.0)
    overtime_hours = Column(Float, default=0.0)
    remarks = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    employee = relationship("Employee", back_populates="attendance_records")
    
    def __repr__(self):
        return f"<Attendance(id={self.id}, employee_id={self.employee_id}, date={self.attendance_date}, status={self.status})>"
