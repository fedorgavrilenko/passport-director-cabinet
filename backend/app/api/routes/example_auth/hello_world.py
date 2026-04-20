from fastapi import APIRouter, Depends
from app.api.models import Example
from app.api.database.db import get_connection

router = APIRouter(prefix="/example", tags=["some tag"])


@router.get("/example_route", response_model=Example)
async def hello_world(conn=Depends(get_connection)):
    row = await conn.fetchrow(
        """
        select * from users
        where name = $1
        """, "Alice")        

    return Example(example=row["email"])
