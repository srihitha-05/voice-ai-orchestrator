from fastapi import APIRouter
from bson import ObjectId
from services.vapi_service import make_call

from db import customers_collection

router = APIRouter()


@router.post("/campaign/{company_id}")
async def trigger_campaign(company_id: str):

    customers = await customers_collection.find(
        {
            "company_id": ObjectId(company_id),
            "status": "PENDING"
        }
    ).to_list(length=100)

    for customer in customers:

        # Placeholder for Vapi call
        response = make_call(customer)

       
        if response.status_code == 201 or response.status_code == 200:
            await customers_collection.update_one(
                {"_id": customer["_id"]},
                {
                    "$set": {
                        "status": "CALL_INITIATED"
                    }
                }
            )
        else:
            print("Vapi call failed:", response.text)

    return {
        "message": "Campaign Triggered",
        "customers_called": len(customers)
    }