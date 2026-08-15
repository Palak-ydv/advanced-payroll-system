"""Salary related models"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey, Date, Text, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.core.constants import SalaryComponentType, PaymentStatus

class SalaryComponent(Base):
    """Salary Component model (earnings, deductions, etc.)"""
    __tablename__ = "salary_components"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    component_type = Column(Enum(SalaryComponentType), nullable=False)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    salary_structures = relationship("SalaryStructure", back_populates="component")
    salary_slip_details = relationship("SalarySlipDetail", back_populates="component")
    
    def __repr__(self):
        return f"<SalaryComponent(id={self.id}, name={self.name}, type={self.component_type})>"

class SalaryStructure(Base):
    """Salary Structure model (employee's salary breakdown)"""
    __tablename__ = "salary_structures"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    component_id = Column(Integer, ForeignKey("salary_components.id"), nullable=False)
    amount = Column(Float, default=0.0, nullable=False)
    percentage = Column(Float, nullable=True)  # For percentage-based components
    effective_from = Column(Date, nullable=False)
    effective_to = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    employee = relationship("Employee", back_populates="salary_structures")
    component = relationship("SalaryComponent", back_populates="salary_structures")
    
    def __repr__(self):
        return f"<SalaryStructure(id={self.id}, employee_id={self.employee_id}, component_id={self.component_id})>"

class SalarySlip(Base):
    """Salary Slip model (monthly/periodic salary slip)"""
    __tablename__ = "salary_slips"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    salary_month = Column(Date, nullable=False)  # Year-Month
    salary_year = Column(Integer, nullable=False)
    gross_salary = Column(Float, default=0.0, nullable=False)
    total_earnings = Column(Float, default=0.0, nullable=False)
    total_deductions = Column(Float, default=0.0, nullable=False)
    net_salary = Column(Float, default=0.0, nullable=False)
    ctc = Column(Float, default=0.0, nullable=False)  # Cost to Company
    working_days = Column(Integer, default=26)
    days_present = Column(Integer, default=0)
    days_absent = Column(Integer, default=0)
    payment_status = Column(Enum(PaymentStatus), default=PaymentStatus.PENDING)
    payment_date = Column(DateTime, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    employee = relationship("Employee", back_populates="salary_slips")
    slip_details = relationship("SalarySlipDetail", back_populates="salary_slip", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<SalarySlip(id={self.id}, employee_id={self.employee_id}, month={self.salary_month})>"

class SalarySlipDetail(Base):
    """Salary Slip Detail model (line items in salary slip)"""
    __tablename__ = "salary_slip_details"
    
    id = Column(Integer, primary_key=True, index=True)
    salary_slip_id = Column(Integer, ForeignKey("salary_slips.id"), nullable=False)
    component_id = Column(Integer, ForeignKey("salary_components.id"), nullable=False)
    amount = Column(Float, default=0.0, nullable=False)
    percentage = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    salary_slip = relationship("SalarySlip", back_populates="slip_details")
    component = relationship("SalaryComponent", back_populates="salary_slip_details")
    
    def __repr__(self):
        return f"<SalarySlipDetail(id={self.id}, slip_id={self.salary_slip_id}, component_id={self.component_id})>"
