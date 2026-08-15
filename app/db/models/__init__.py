"""Database models package"""
from app.db.models.user import User
from app.db.models.employee import Employee, Department, Designation
from app.db.models.salary import SalaryComponent, SalaryStructure, SalarySlip, SalarySlipDetail
from app.db.models.attendance import Attendance
from app.db.models.leave import Leave, LeaveRequest
from app.db.models.tax import TaxConfiguration, TaxDeduction
from app.db.models.audit import AuditLog

__all__ = [
    "User",
    "Employee",
    "Department",
    "Designation",
    "SalaryComponent",
    "SalaryStructure",
    "SalarySlip",
    "SalarySlipDetail",
    "Attendance",
    "Leave",
    "LeaveRequest",
    "TaxConfiguration",
    "TaxDeduction",
    "AuditLog",
]
