"""Leave related models"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Date, Float, Text, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.core.constants import LeaveType

class Leave(Base):
    """Leave balance model"""
    __tablename__ = "leaves"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    leave_type = Column(Enum(LeaveType), nullable=False)
    total_balance = Column(Float, default=0.0, nullable=False)
    used_balance = Column(Float, default=0.0, nullable=False)
    available_balance = Column(Float, default=0.0, nullable=False)
    carry_forward = Column(Float, default=0.0, nullable=False)
    financial_year = Column(String(20), nullable=False)  # e.g., "2024-2025"
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    leave_requests = relationship("LeaveRequest", back_populates="leave")
    
    def __repr__(self):
        return f"<Leave(id={self.id}, employee_id={self.employee_id}, type={self.leave_type})>"

class LeaveRequest(Base):
    """Leave request/application model"""
    __tablename__ = "leave_requests"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    leave_id = Column(Integer, ForeignKey("leaves.id"), nullable=False)
    leave_type = Column(Enum(LeaveType), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    number_of_days = Column(Float, default=0.0, nullable=False)
    reason = Column(Text, nullable=True)
    status = Column(String(50), default="pending", nullable=False)  # pending, approved, rejected, cancelled
    approved_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    approval_date = Column(DateTime, nullable=True)
    approval_remarks = Column(Text, nullable=True)
    is_half_day = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    employee = relationship("Employee", back_populates="leave_requests")
    leave = relationship("Leave", back_populates="leave_requests")
    
    def __repr__(self):
        return f"<LeaveRequest(id={self.id}, employee_id={self.employee_id}, status={self.status})>"
