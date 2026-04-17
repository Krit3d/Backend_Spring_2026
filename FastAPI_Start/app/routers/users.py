from fastapi import APIRouter, HTTPException

from ..repositories.users import UserRepository
from ..schemas.users import UserCreate, User
from ..database import AsyncSessionLocal

# Organizing user-related endpoints
router = APIRouter()


@router.get("/api/users")
async def get_users_data() -> list[User]:
    async with AsyncSessionLocal() as session:
        rep = UserRepository(session)

        return await rep.get_all_users()


# POST endpoint for user registration
@router.post("/api/users", response_model=User)
async def create_user(user: UserCreate) -> User:
    async with AsyncSessionLocal() as session:
        rep = UserRepository(session)

        try:
            user_id = await rep.add_user(user.username, user.age, user.email)
        except ValueError:
            # Get a specific 409 status code instead of internal 500 error
            raise HTTPException(status_code=409, detail="User already exists!")
        else:
            # model_dump is for creation of model instances from obj with attrs
            return User(id=user_id, **user.model_dump())


@router.get("/api/users/{user_id}")
async def get_user_data(user_id: int) -> User:
    async with AsyncSessionLocal() as session:
        rep = UserRepository(session)

        data = await rep.get_user(user_id)

        if data is None:
            raise HTTPException(status_code=404, detail="User not found")

        return data
