from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware # 1. Import the Middleware
from pydantic import BaseModel
from decimal import Decimal, ROUND_HALF_UP

app = FastAPI()

# 2. Configure the "Service Trust" Boundary
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For a local demo, "*" is efficient. In Prod, use ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"], # This allows the POST and the OPTIONS preflight
    allow_headers=["*"],
)

class RefundRequest(BaseModel):
    refund_amount: Decimal
    total_amount: Decimal
    tax_paid: Decimal

@app.post("/api/v1/calculate")
async def calculate_v1(request: RefundRequest):
    if request.total_amount <= 0:
        raise HTTPException(status_code=400, detail="Total amount must be positive")
    
    # Proportional Logic: (R/A) * T
    result = (request.refund_amount / request.total_amount) * request.tax_paid
    
    # Financial Grade Precision
    final_result = result.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    return {
        "status": "success",
        "formula_version": "1.0",
        "tax_refund": float(final_result)
    }