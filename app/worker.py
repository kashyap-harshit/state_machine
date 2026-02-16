from .models import TaskStatus, Task
from .db import AsyncSessionLocal
import asyncio
from sqlalchemy import select


async def getting_stuff():
    async with AsyncSessionLocal() as session:
        the_query = select(Task).where(Task.status==TaskStatus.PENDING)
        results = await session.execute(the_query)
        tasks = results.scalars().all()
        for task in tasks:

            print("this are the pending tasks: ",task.payload)

if __name__=="__main__":
    asyncio.run(getting_stuff())
    