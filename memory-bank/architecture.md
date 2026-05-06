# System Architecture

## Overview
TaxBackendService is a Python microservice built using FastAPI for calculating proportional tax refunds with high precision requirements. The service exposes a REST API for financial calculations.

## High-Level Architecture
```
+----------------------+      POST /api/v1/calculate      +----------------------+
|  TaxFrontendPortal   | --------------------------------> |  TaxBackendService   |
|  (React / CRA)       | <-------------------------------- |  (FastAPI / Python)  |
+----------------------+         JSON response             +----------------------+
```

## Component Diagram
```
TaxBackendService/
├── src/
│   └── main.py           # FastAPI application entry point
├── tests/
│   └── test_main.py      # Test suite using pytest
├── requirements.txt      # Python dependencies
└── docs/
    ├── refund_spec_v1.md # Business logic specification v1.0
    └── refund_spec_v2.md # Business logic specification v2.0 (Luxury Amendment)
```

## Core Components

### 1. FastAPI Application (src/main.py)
- **Framework**: FastAPI for building REST APIs
- **Endpoint**: Single POST endpoint `/api/v1/calculate` for tax refund calculations
- **Middleware**: CORS middleware configured for cross-origin requests
- **Validation**: Pydantic models for request validation
- **Precision**: Uses Python's `decimal` module with `ROUND_HALF_UP` for financial-grade precision

### 2. Data Models
- **RefundRequest**: Pydantic model defining the input structure
  - `refund_amount`: Decimal - Price of the item being returned
  - `total_amount`: Decimal - Original total value of the order
  - `tax_paid`: Decimal - Total tax paid on the order

### 3. Business Logic
- **Formula**: Proportional tax refund calculation: `(R/A) * T`
- **Rounding**: Results quantized to 2 decimal places with `ROUND_HALF_UP`
- **Validation**: Input validation to ensure positive total amounts

## External Dependencies
- **FastAPI**: Web framework for building APIs
- **Uvicorn**: ASGI server for running the application
- **Pydantic**: Data validation and settings management
- **pytest**: Testing framework
- **httpx**: HTTP client for testing

## Deployment Architecture
- **Development**: Run with uvicorn using `--reload` flag for hot reloading
- **Production**: Deploy with proper CORS configuration restricting origins
- **Scaling**: Stateless service that can be scaled horizontally

## Data Flow
1. Client sends POST request to `/api/v1/calculate` with refund data
2. Pydantic validates the input data
3. FastAPI routes the request to the calculation function
4. Business logic applies the proportional refund formula
5. Result is rounded to 2 decimal places using financial-grade precision
6. Response is returned as JSON with status, formula version, and tax refund amount

## Security Considerations
- CORS is configured permissively for local development but should be restricted in production
- Input validation prevents invalid data from being processed
- No sensitive data is stored or processed by the service
