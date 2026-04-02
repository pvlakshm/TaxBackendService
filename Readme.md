# Tax Refund Backend Service

An enterprise-grade microservice for calculating tax refunds. This service follows the "Rigorous Software Engineering" principles for financial accuracy and architectural stability.

## Domain Logic & Specification
The authoritative business logic and mathematical formulas for this service are maintained as versioned specifications.

- **Current Specification:** [docs/refund_spec_v1.md](./docs/refund_spec_v1.md)
- **Standard:** LaTeX-based formal definitions.

## Tech Stack
- **Language:** Python 3.14+
- **Framework:** FastAPI (Asynchronous API)
- **Validation:** Pydantic v2 (Type safety and schema enforcement)
- **Math:** Python `decimal` module (ROUND_HALF_UP)
- **Testing:** Pytest (AAA pattern with Fixtures)

## Valdation
To certify this baseline as stable, the following three-step validation must be completed.

### 1. Install dependencies
```pip install -r requirements.txt```

### 2. Mathematical Accuracy (Automated)
Run the test suite to verify all tests pass.

```python -m pytest test_main.py -v ```

### 3. API Contract Integrity (Interactive)
Validate the live OpenAPI schema and response structure.

- Start the service: ```python -m uvicorn main:app --reload```
- Navigate to: http://127.0.0.1:8000/docs
- Execute Smoke Test:
  - **Input**: {"refund_amount": 50, "total_amount": 100, "tax_paid": 15}
  - **Output**: {"status": "success", "formula_version": "1.0", "tax_refund": 7.5}

### 4. Specification Rendering
Verify the "Source of Truth" is legible for non-technical stakeholders.

Open ```docs/refund_spec_v1.md``` in a Markdown viewer.

Success Criterion: Ensure the LaTeX formula renders as a clear mathematical equation, not raw code.