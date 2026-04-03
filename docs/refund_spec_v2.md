# Tax Refund Specification v2.0 (Luxury Amendment)

## 1. Objective
To introduce a "Luxury Surcharge" on high-value transactions to align with the 2026 Tax Code.

## 2. Mathematical Definition
The refund $T_r$ is calculated based on the Proportional Refund logic, but subject to a 2% deduction if the Total Transaction Amount ($A$) exceeds $500.

### Base Variables
* $R$: Refundable Amount
* $A$: Total Transaction Amount
* $T_{total}$: Total Tax Paid

### Final Formula
$$T_r = \text{BaseRefund} \times \text{Multiplier}$$

Where:
* $\text{BaseRefund} = (R / A) \times T_{total}$
* $\text{Multiplier} = 0.98 \text{ if } A > 500, \text{ else } 1.0$

## 3. Validation Case
* **Input:** $R=50, A=1000, T=15$
* **Base Refund:** $(50/1000) \times 15 = 0.75$
* **Luxury Adjustment:** $0.75 \times 0.98 = 0.735$
* **Expected Output:** $0.74$ (Rounded to 2 decimal places)