# Tax Refund Specification v1.0

## Business Logic
The standard proportional tax refund is calculated based on the ratio of the 
refunded amount to the original total amount, applied to the total tax paid.

## Mathematical Formula
The tax refund $T_r$ is calculated as:

$$T_r = (R/A) \times T_{total}$$

Where:
- $R$ = Refunded Amount (Price of the item being returned)
- $A$ = Original Total Amount (Total order value)
- $T_{total}$ = Total Tax Paid on the order