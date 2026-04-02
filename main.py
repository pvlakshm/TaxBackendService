from fastapi import FastAPI
from pydantic import BaseModel
from decimal import Decimal, ROUND_HALF_UP

app = FastAPI(title="Tax Refund Service")

class RefundRequest(BaseModel):
    refund_amount: float
    total_amount: float
    tax_paid: float

@app.post("/api/v1/calculate")
async def calculate_refund(request: RefundRequest):
    # Convert to Decimal for financial precision
    R = Decimal(str(request.refund_amount))
    A = Decimal(str(request.total_amount))
    T_total = Decimal(str(request.tax_paid))

    # Original Formula: (R / A) * T_total
    tax_refund = (R / A) * T_total
    
    # Quantize to 2 decimal places
    final_amount = tax_refund.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)

    return {
        "status": "success",
        "formula_version": "1.0",
        "tax_refund": float(final_amount)
    }