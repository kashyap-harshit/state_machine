from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Enum, DateTime, func
from sqlalchemy.dialects.postgresql import JSONB
import enum
from datetime import datetime


class Base(DeclarativeBase):
    pass


class TaskStatus(enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus), default=TaskStatus.PENDING
    )
    task_type: Mapped[str] = mapped_column(String(100))
    payload: Mapped[dict[str, any]] = mapped_column(JSONB)
    scheduled_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    retry_count: Mapped[int] = mapped_column(default=0)


