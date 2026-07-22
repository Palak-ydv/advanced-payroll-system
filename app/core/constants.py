"""Application Constants"""
from enum import Enum

# Employee Status
class EmployeeStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    ON_LEAVE = "on_leave"
    TERMINATED = "terminated"

# Leave Types
class LeaveType(str, Enum):
    CASUAL = "casual"
    SICK = "sick"
    EARNED = "earned"
    MATERNITY = "maternity"
    PATERNITY = "paternity"
    UNPAID = "unpaid"

# Attendance Status
class AttendanceStatus(str, Enum):
    PRESENT = "present"
    ABSENT = "absent"
    HALF_DAY = "half_day"
    LEAVE = "leave"
    WEEKEND = "weekend"
    HOLIDAY = "holiday"

# Salary Components
class SalaryComponentType(str, Enum):
    BASIC = "basic"
    ALLOWANCE = "allowance"
    INCENTIVE = "incentive"
    DEDUCTION = "deduction"
    TAX = "tax"
    RECOVERY = "recovery"

# User Roles
class UserRole(str, Enum):
    ADMIN = "admin"
    HR_MANAGER = "hr_manager"
    PAYROLL_MANAGER = "payroll_manager"
    EMPLOYEE = "employee"
    VIEWER = "viewer"

# Payment Status
class PaymentStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

# India Tax Slabs (FY 2024-25)
INCOME_TAX_SLABS = [
    {"min": 0, "max": 300000, "rate": 0.0},
    {"min": 300000, "max": 600000, "rate": 0.05},
    {"min": 600000, "max": 900000, "rate": 0.10},
    {"min": 900000, "max": 1200000, "rate": 0.15},
    {"min": 1200000, "max": 1500000, "rate": 0.20},
    {"min": 1500000, "max": float('inf'), "rate": 0.30},
]

# Surcharge rates (for income above 50 lakh)
SURCHARGE_RATE = 0.25

# Health and Education Cess
HEALTH_EDUCATION_CESS = 0.04

# EPF and ESI
EPF_CONTRIBUTION_RATE = 0.12  # Employee: 12%, Employer: 12% + admin charge
ESI_RATE = 0.0075  # 0.75% for monthly salary < 21000
ESI_EMPLOYER_RATE = 0.0325  # 3.25%

# Professional Tax (PT) - varies by state
PROFESSIONAL_TAX_MONTHLY = {
    "maharashtra": 200,
    "karnataka": 200,
    "tamil_nadu": 0,  # TN doesn't have PT
    "others": 150,
}

# Standard Deduction
STANDARD_DEDUCTION = 50000

# Section 80 Limits
SECTION_80C_LIMIT = 150000
SECTION_80D_LIMIT_SELF = 25000
SECTION_80D_LIMIT_SENIOR = 50000
SECTION_80GG_LIMIT = 200000

# Gratuity
GRATUITY_LIMIT = 2000000  # 20 lakhs
GRATUITY_DIVISOR = 26

# Working Days Per Month
WORKING_DAYS_PER_MONTH = 26

# Days Per Week
DAYS_PER_WEEK = 6

# Leave Carry Forward
LEAVE_CARRY_FORWARD_LIMIT = 30
