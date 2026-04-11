# TaxBackendService
Testing
![Python](https://img.shields.io/badge/python-3.14+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-e92063?logo=pydantic&logoColor=white)
![pytest](https://img.shields.io/badge/tested%20with-pytest-0a9edc?logo=pytest&logoColor=white)

An enterprise-grade Python microservice for calculating proportional tax refunds. Part of the **Tax Refund System**, which also includes [TaxFrontendPortal](https://github.com/pvlakshm/TaxFrontendPortal) — the React-based user interface that consumes this API.

---

## Overview

`TaxBackendService` exposes a single REST endpoint that computes how much tax a customer is owed when returning part of an order. All arithmetic uses Python's `decimal` module with `ROUND_HALF_UP` rounding to guarantee financial-grade precision. Business logic is maintained as a versioned, LaTeX-formatted specification so the "source of truth" is accessible to both engineers and non-technical stakeholders.

---

## System Architecture

```
+----------------------+      POST /api/v1/calculate      +----------------------+
|  TaxFrontendPortal   | --------------------------------> |  TaxBackendService   |
|  (React / CRA)       | <-------------------------------- |  (FastAPI / Python)  |
+----------------------+         JSON response             +----------------------+
```

---

## Business Logic

The service applies a **proportional tax refund** formula defined in [`docs/refund_spec_v1.md`](docs/refund_spec_v1.md). All calculations use financial-grade decimal precision (`ROUND_HALF_UP`).

---

## Tech Stack

| Concern        | Technology                                    |
|----------------|-----------------------------------------------|
| Language       | Python 3.14+                                  |
| Web Framework  | FastAPI (async)                               |
| Validation     | Pydantic v2                                   |
| Precision Math | Python `decimal` module (`ROUND_HALF_UP`)     |
| Testing        | Pytest (AAA pattern with fixtures)            |
| HTTP Client    | httpx (used in tests)                         |
| Server         | Uvicorn (ASGI)                                |

---

## Project Structure

```
TaxBackendService/
├── main.py               # FastAPI app, CORS config, and calculation endpoint
├── test_main.py          # Pytest test suite
├── requirements.txt      # Python dependencies
└── docs/
    └── refund_spec_v1.md # Versioned business logic specification (LaTeX)
```

---

## Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Service

```bash
python -m uvicorn main:app --reload
```

The service starts at `http://127.0.0.1:8000`.

### 3. Explore the Interactive API Docs

```
http://127.0.0.1:8000/docs
```

---

## API Reference

### `POST /api/v1/calculate`

Calculates the proportional tax refund for a returned item.

**Request Body**

```json
{
  "refund_amount": 50,
  "total_amount": 100,
  "tax_paid": 15
}
```

| Field           | Type    | Description                           |
|-----------------|---------|---------------------------------------|
| `refund_amount` | Decimal | Price of the item being returned      |
| `total_amount`  | Decimal | Original total value of the order     |
| `tax_paid`      | Decimal | Total tax paid on the order           |

**Success Response (`200`)**

```json
{
  "status": "success",
  "formula_version": "1.0",
  "tax_refund": 7.5
}
```

**Error Response (`400`)**

```json
{
  "detail": "Total amount must be positive"
}
```

---

## Running Tests

```bash
python -m pytest test_main.py -v
```

---

## CORS

CORS is configured permissively for local development (`allow_origins=["*"]`). Before deploying to production, restrict allowed origins:

```python
allow_origins=["https://your-frontend-domain.com"]
```

---

## Specification

Business logic is versioned as a LaTeX-formatted Markdown document:

- **[docs/refund_spec_v1.md](docs/refund_spec_v1.md)**

Open in a Markdown viewer with LaTeX support (e.g. GitHub, VS Code + Markdown Math extension) to render the formula correctly.

---

## Related Repositories

- **[TaxFrontendPortal](https://github.com/pvlakshm/TaxFrontendPortal)** — React frontend that provides the user interface for this service.
