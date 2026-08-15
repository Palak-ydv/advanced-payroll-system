"""Tax related models"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey, Date, Text, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.core.constants import TaxRegime

class TaxConfiguration(Base):
    """Tax Configuration model"""
    __tablename__ = "tax_configurations"
    
    id = Column(Integer, primary_key=True, index=True)
    financial_year = Column(String(20), unique=True, nullable=False)  # e.g., "2024-2025"
    tax_regime = Column(Enum(TaxRegime), default=TaxRegime.NEW, nullable=False)
    standard_deduction = Column(Float, default=0.0, nullable=False)
    hra_exemption_percentage = Column(Float, default=0.0)
    medical_allowance_limit = Column(Float, default=0.0)
    transport_allowance_limit = Column(Float, default=0.0)
    section_80c_limit = Column(Float, default=150000.0)
    section_80d_limit = Column(Float, default=25000.0)
    section_80e_limit = Column(Float, default=0.0)  # No limit
    nps_contribution_limit = Column(Float, default=0.0)
    effective_from = Column(Date, nullable=False)
    effective_to = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    tax_deductions = relationship("TaxDeduction", back_populates="tax_config")
    
    def __repr__(self):
        return f"<TaxConfiguration(id={self.id}, fy={self.financial_year}, regime={self.tax_regime})>"

class TaxDeduction(Base):
    """Tax Deduction model (employee-specific tax deductions)"""
    __tablename__ = "tax_deductions"
    
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    tax_config_id = Column(Integer, ForeignKey("tax_configurations.id"), nullable=False)
    section_80c_amount = Column(Float, default=0.0)  # LIC, PPF, ELSS, etc.
    section_80d_amount = Column(Float, default=0.0)  # Health insurance
    section_80e_amount = Column(Float, default=0.0)  # Education loan interest
    section_80g_amount = Column(Float, default=0.0)  # Charitable donations
    nps_contribution = Column(Float, default=0.0)
    home_loan_interest = Column(Float, default=0.0)  # Section 24
    other_deductions = Column(Float, default=0.0)
    total_deductions = Column(Float, default=0.0)
    remarks = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    tax_config = relationship("TaxConfiguration", back_populates="tax_deductions")
    
    def __repr__(self):
        return f"<TaxDeduction(id={self.id}, employee_id={self.employee_id}, total={self.total_deductions})>"
