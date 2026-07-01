import asyncio
from db import companies_collection, customers_collection

async def seed():

    await companies_collection.delete_many({})
    await customers_collection.delete_many({})

    companies = [
        {
            "name": "Dream Homes",
            "prompt": "You help customers buy luxury houses."
        },
        {
            "name": "City Rentals",
            "prompt": "You help customers find rental apartments."
        }
    ]

    result = await companies_collection.insert_many(companies)

    company_ids = result.inserted_ids

    customers = [
        {
            "company_id": company_ids[0],
            "name": "John",
            "phone": "+911111111111",
            "status": "PENDING"
        },
        {
            "company_id": company_ids[0],
            "name": "Priya",
            "phone": "+912222222222",
            "status": "PENDING"
        },
        {
            "company_id": company_ids[0],
            "name": "Rahul",
            "phone": "+913333333333",
            "status": "PENDING"
        },
        {
            "company_id": company_ids[1],
            "name": "Alice",
            "phone": "+914444444444",
            "status": "PENDING"
        },
        {
            "company_id": company_ids[1],
            "name": "David",
            "phone": "+915555555555",
            "status": "PENDING"
        },
        {
            "company_id": company_ids[1],
            "name": "Mike",
            "phone": "+916666666666",
            "status": "PENDING"
        }
    ]

    await customers_collection.insert_many(customers)

    print("Database seeded successfully!")

asyncio.run(seed())