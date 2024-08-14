from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

client = None
db = None

async def init_db():
    global client, db
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    db = client[settings.MONGODB_NAME]

async def get_db():
    if db is None:
        await init_db()
    return db

async def close_db_connection():
    global client
    if client:
        client.close()
        client = None