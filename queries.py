import asyncio

from sqlalchemy import text

from database_api import db_api


async def get_all():
    async with db_api.engine.connect() as conn:
        res = await conn.execute(text("SELECT * FROM first"))
        print(f"res: {res.all()}")


async def insert_data():
    stmt = text("""INSERT INTO first (id, name) VALUES (4, 'Pimmo');""")

    async with db_api.engine.connect() as conn:
        res = await conn.execute(stmt)
        await conn.commit()
        # print(f'res: {res.first()}')


async def main():
    await get_all()
    # await insert_data()
    # await get_first()


if __name__ == "__main__":
    asyncio.run(main())
