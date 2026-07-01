from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")

client = AsyncIOMotorClient(MONGO_URI)

db = client["voice_ai_db"]

companies_collection = db["companies"]
customers_collection = db["customers"]
call_logs_collection = db["call_logs"]