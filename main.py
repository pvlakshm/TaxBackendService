from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from decimal import Decimal
from calculator import RefundCalculator as RC
from database import TaxDatabase

app = FastAPI()
db_instance = TaxDatabase()

class RefundRequest(BaseModel):
    refund_amount: Decimal
    total_amount: Decimal
    tax_paid: Decimal

def perform_calculation(calc_engine, request: RefundRequest) -> Decimal:
    return calc_engine.calculate(
        request.refund_amount, 
        request.total_amount, 
        request.tax_paid
    )

def persist_result(storage_engine, request: RefundRequest, result: Decimal):
    storage_engine.save_result(
        request.refund_amount, 
        request.total_amount, 
        request.tax_paid, 
        result
    )

def fetch_history(storage_engine):
    """Takes the DB as an argument to retrieve history."""
    return storage_engine.get_all_history()

@app.post("/api/v1/calculate")
async def handle_request(request: RefundRequest):
    if request.total_amount <= 0:
        raise HTTPException(status_code=400, detail="Total amount must be positive")
    
    if request.refund_amount > request.total_amount:
            raise HTTPException(status_code=400, detail="Refund cannot exceed total")

    final_refund = perform_calculation(RC, request)

    persist_result(db_instance, request, final_refund)

    return {"status": "success", "tax_refund": final_refund}

@app.get("/api/v1/history")
async def get_history_route():
    # We call our fetcher function and pass the db_instance
    history = fetch_history(db_instance)
    return history