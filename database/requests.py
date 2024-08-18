from database.models import async_session
from database.models import User
from sqlalchemy import select, update, delete


async def set_user(tg_id, username, first_name, last_name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, username=username, first_name=first_name, last_name=last_name, is_active=True))
            await session.commit()


async def get_tg_id():
    async with async_session() as session:
        user_tg_id = await session.scalars(select(User.tg_id))
    
    return user_tg_id
