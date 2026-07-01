from fastapi import APIRouter
from pydantic import BaseModel
from bson import ObjectId

from db import customers_collection, call_logs_collection
from langgraph_flow.graph import graph

router = APIRouter()


class VapiWebhook(BaseModel):
    customer_id: str
    transcript: str


@router.post("/webhooks/vapi")
async def vapi_webhook(payload: VapiWebhook):

    result = graph.invoke(
        {
            "transcript": payload.transcript,
            "status": ""
        }
    )

    status = result["status"]

    # Update customer status
    await customers_collection.update_one(
        {"_id": ObjectId(payload.customer_id)},
        {
            "$set": {
                "status": status
            }
        }
    )

    # Save call log
    await call_logs_collection.insert_one(
        {
            "customer_id": ObjectId(payload.customer_id),
            "transcript": payload.transcript,
            "status": status
        }
    )

    return {
        "message": "Webhook Processed Successfully",
        "status": status
    }