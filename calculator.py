from decimal import Decimal, ROUND_HALF_UP

class RefundCalculator:
    """
    Implements the core proportional tax refund logic.
    Formula: (Refund Amount / Total Amount) * Tax Paid
    """
    
    @staticmethod
    def calculate(refund_amount: Decimal, total_amount: Decimal, tax_paid: Decimal):
        # Standard Proportional Logic
        # We use Decimal for financial precision to avoid floating point issues.
        raw_result = (refund_amount / total_amount) * tax_paid
        
        # Financial Grade Precision: Rounding to 2 decimal places
        return raw_result.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)