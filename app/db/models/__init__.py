"""Database models"""
from app.db.models.user import User
from app.db.models.employee import Employee, Department, Designation
from app.db.models.salary import SalaryStructure, SalaryComponent, SalarySlip
from app.db.models.attendance import Attendance
from app.db.models.leave import Leave, LeaveRequest
from app.db.models.tax import TaxConfiguration, TaxDeduction
from app.db.models.audit import AuditLog

__all__ = [
    "User",
    "Employee",
    "Department",
    "Designation",
    "SalaryStructure",
    "SalaryComponent",
    "SalarySlip",
    "Attendance",
    "Leave",
    "LeaveRequest",
    "TaxConfiguration",
    "TaxDeduction",
    "AuditLog",
]
