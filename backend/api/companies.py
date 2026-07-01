from fastapi import APIRouter
from db import companies_collection

router = APIRouter()


@router.get("/companies")
async def get_companies():

    companies = await companies_collection.find().to_list(length=100)

    for company in companies:
        company["_id"] = str(company["_id"])

    return companies