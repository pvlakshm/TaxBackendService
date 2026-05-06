# Project Overview

## Name
TaxBackendService

## Description
An enterprise-grade Python microservice for calculating proportional tax refunds. Part of the Tax Refund System, which also includes TaxFrontendPortal — the React-based user interface that consumes this API.

## Purpose
Exposes a single REST endpoint that computes how much tax a customer is owed when returning part of an order. All arithmetic uses Python's `decimal` module with `ROUND_HALF_UP` rounding to guarantee financial-grade precision.

## Technology Stack
- **Language**: Python 3.14+
- **Web Framework**: FastAPI (async)
- **Validation**: Pydantic v2
- **Precision Math**: Python `decimal` module (`ROUND_HALF_UP`)
- **Testing**: Pytest (AAA pattern with fixtures)
- **HTTP Client**: httpx (used in tests)
- **Server**: Uvicorn (ASGI)

## Key Components
1. **Main Application** (`src/main.py`): FastAPI app with CORS configuration and calculation endpoint
2. **Tests** (`tests/test_main.py`): Pytest test suite with various test cases
3. **Documentation** (`docs/refund_spec_v1.md`, `docs/refund_spec_v2.md`): Versioned business logic specifications
4. **Dependencies** (`requirements.txt`): Python dependencies

## Business Logic
The service applies a proportional tax refund formula defined in the specification documents. The current implementation uses v1.0 of the formula:
T_r = (R/A) × T_total

Where:
- R = Refunded Amount (Price of the item being returned)
- A = Original Total Amount (Total order value)
- T_total = Total Tax Paid on the order

The v2.0 specification introduces a "Luxury Surcharge" on high-value transactions, documented in `docs/refund_spec_v2.md`.

## API Endpoint
- **POST** `/api/v1/calculate`: Calculates the proportional tax refund for a returned item

## Related Repositories
- [TaxFrontendPortal](https://github.com/pvlakshm/TaxFrontendPortal): React frontend that provides the user interface for this service
