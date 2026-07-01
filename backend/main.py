from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.companies import router as companies_router
from api.customers import router as customers_router
from api.campaigns import router as campaigns_router
from routes.webhook import router as webhook_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(companies_router)
app.include_router(customers_router)
app.include_router(campaigns_router)
app.include_router(webhook_router)

@app.get("/")
def home():
    return {"message": "Voice AI Backend Running 🚀"}