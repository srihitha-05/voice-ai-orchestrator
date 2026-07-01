from fastapi import APIRouter
from bson import ObjectId
from db import customers_collection

router = APIRouter()


@router.get("/customers/{company_id}")
async def get_customers(company_id: str):

    customers = await customers_collection.find(
        {
            "company_id": ObjectId(company_id)
        }
    ).to_list(length=100)

    for customer in customers:
        customer["_id"] = str(customer["_id"])
        customer["company_id"] = str(customer["company_id"])

    return customers