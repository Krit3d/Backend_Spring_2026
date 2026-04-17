from pydantic import EmailStr

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import User


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add_user(self, username: str, age: int, email: EmailStr) -> int:
        user = User(username=username, age=age, email=str(email))
        self.session.add(user)

        try:
            await self.session.commit()

        except IntegrityError as exc:
            await self.session.rollback()

            # Use exception chaining
            raise ValueError from exc

        await self.session.refresh(user)

        return user.id

    async def get_user(self, user_id: int) -> User | None:
        result = await self.session.execute(
            select(User).where(User.id == user_id)
        )

        return result.scalar_one_or_none()

    async def get_all_users(self) -> list[User]:
        result = await self.session.execute(select(User))

        return list(result.scalars().all())
