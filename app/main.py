from fastapi import FastAPI, Depends
from .schemas import TaskCreate
from sqlalchemy.ext.asyncio import AsyncSession
from .db import get_db
from datetime import datetime, timezone, timedelta
from .models import Task

app = FastAPI()


@app.get("/")
def home():
    return "backend is up and running"


@app.post("/tasks", status_code=202)
async def create_task(task_data: TaskCreate, db: AsyncSession = Depends(get_db)):

    run_at = datetime.now(timezone.utc) + timedelta(seconds=task_data.delay_seconds)

    new_task = Task(
        task_type=task_data.task_type,
        payload=task_data.payload,
        scheduled_at=run_at,
    )

    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)

    return {"task id": new_task.id, "status": "accepted", "scheduled at": run_at}
