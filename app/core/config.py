"""Application Configuration"""
import os
from pathlib import Path
from typing import Optional
from datetime import datetime, timedelta
from pydantic_settings import BaseSettings
from pydantic import Field

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    """Application Settings"""
    
    # Application Info
    app_name: str = "Advanced Payroll System"
    app_version: str = "1.0.0"
    debug: bool = Field(default=False, env="DEBUG")
    environment: str = Field(default="development", env="ENVIRONMENT")
    
    # Server
    api_v1_str: str = "/api/v1"
    allowed_hosts: list = Field(default=["localhost", "127.0.0.1"], env="ALLOWED_HOSTS")
    
    # Database
    database_url: str = Field(default="postgresql://payroll_user:password@localhost:5432/payroll_db", env="DATABASE_URL")
    database_echo: bool = Field(default=False, env="DATABASE_ECHO")
    database_pool_size: int = 20
    database_max_overflow: int = 10
    
    # Redis
    redis_url: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")
    
    # JWT
    secret_key: str = Field(default="change-this-secret-key-in-production", env="SECRET_KEY")
    algorithm: str = Field(default="HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    refresh_token_expire_days: int = Field(default=7, env="REFRESH_TOKEN_EXPIRE_DAYS")
    
    # Email
    email_from: str = Field(default="noreply@payrollsys.com", env="EMAIL_FROM")
    smtp_server: str = Field(default="smtp.gmail.com", env="SMTP_SERVER")
    smtp_port: int = Field(default=587, env="SMTP_PORT")
    smtp_user: str = Field(default="", env="SMTP_USER")
    smtp_password: str = Field(default="", env="SMTP_PASSWORD")
    smtp_tls: bool = Field(default=True, env="SMTP_TLS")
    
    # AWS
    aws_access_key_id: Optional[str] = Field(default=None, env="AWS_ACCESS_KEY_ID")
    aws_secret_access_key: Optional[str] = Field(default=None, env="AWS_SECRET_ACCESS_KEY")
    aws_region: str = Field(default="ap-south-1", env="AWS_REGION")
    aws_s3_bucket: str = Field(default="payroll-documents", env="AWS_S3_BUCKET")
    
    # Celery
    celery_broker_url: str = Field(default="redis://localhost:6379/0", env="CELERY_BROKER_URL")
    celery_result_backend: str = Field(default="redis://localhost:6379/0", env="CELERY_RESULT_BACKEND")
    
    # Logging
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    log_file: str = Field(default="/var/log/payroll/app.log", env="LOG_FILE")
    
    # India Tax Configuration
    fy_start_date: str = Field(default="2024-04-01", env="FY_START_DATE")
    fy_end_date: str = Field(default="2025-03-31", env="FY_END_DATE")
    standard_deduction: float = Field(default=50000.0, env="STANDARD_DEDUCTION")
    epf_percentage: float = Field(default=12.0, env="EPF_PERCENTAGE")
    esi_threshold: float = Field(default=21000.0, env="ESI_THRESHOLD")
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"

settings = Settings()
