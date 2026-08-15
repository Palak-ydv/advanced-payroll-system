"""Employee related models"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Enum, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.core.constants import EmployeeStatus

class Department(Base):
    """Department model"""
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    employees = relationship("Employee", back_populates="department")
    
    def __repr__(self):
        return f"<Department(id={self.id}, name={self.name})>"

class Designation(Base):
    """Designation/Job Title model"""
    __tablename__ = "designations"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    employees = relationship("Employee", back_populates="designation")
    
    def __repr__(self):
        return f"<Designation(id={self.id}, title={self.title})>"

class Employee(Base):
    """Employee model"""
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    employee_id = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=True)
    pan_number = Column(String(20), unique=True, nullable=True)
    aadhar_number = Column(String(20), unique=True, nullable=True)
    bank_account = Column(String(50), nullable=True)
    bank_ifsc = Column(String(20), nullable=True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    designation_id = Column(Integer, ForeignKey("designations.id"), nullable=False)
    date_of_joining = Column(Date, nullable=False)
    date_of_relieving = Column(Date, nullable=True)
    status = Column(Enum(EmployeeStatus), default=EmployeeStatus.ACTIVE, nullable=False)
    basic_salary = Column(Float, default=0.0, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    department = relationship("Department", back_populates="employees")
    designation = relationship("Designation", back_populates="employees")
    salary_structures = relationship("SalaryStructure", back_populates="employee")
    salary_slips = relationship("SalarySlip", back_populates="employee")
    attendance_records = relationship("Attendance", back_populates="employee")
    leave_requests = relationship("LeaveRequest", back_populates="employee")
    
    def __repr__(self):
        return f"<Employee(id={self.id}, employee_id={self.employee_id}, email={self.email})>"
