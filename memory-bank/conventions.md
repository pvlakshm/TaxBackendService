# Coding Conventions and Standards

## Python Code Style
- Follow PEP 8 guidelines for Python code formatting
- Use 4 spaces for indentation (no tabs)
- Maximum line length of 79 characters for code, 72 for comments and docstrings
- Use meaningful variable and function names in snake_case
- Use descriptive class names in PascalCase

## Documentation Standards
- All public functions and classes should have docstrings
- Docstrings should follow Google Python Style Guide format
- Business logic should be documented in versioned specification documents in Markdown with LaTeX formulas
- Comments should explain "why" rather than "what"

## File Organization
```
TaxBackendService/
├── src/                  # Source code
│   └── main.py          # Main application file
├── tests/                # Test files
│   └── test_main.py     # Tests for main application
├── docs/                 # Documentation
│   ├── refund_spec_v1.md # Business logic specification v1.0
│   └── refund_spec_v2.md # Business logic specification v2.0
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── .gitignore            # Git ignore file
```

## Naming Conventions
- Variables: `snake_case`
- Functions: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Files: `snake_case.py`
- Directories: `snake_case`

## API Design
- Use semantic versioning for API endpoints (e.g., `/api/v1/calculate`)
- Follow RESTful principles
- Use JSON for request/response bodies
- Return consistent response structures:
  ```json
  {
    "status": "success",
    "formula_version": "1.0",
    "tax_refund": 7.50
  }
  ```

## Error Handling
- Use appropriate HTTP status codes
- Provide meaningful error messages
- Validate input data at the API boundary using Pydantic models
- Handle exceptions gracefully and return consistent error responses

## Testing Conventions
- Use pytest as the testing framework
- Follow AAA pattern (Arrange, Act, Assert) for test structure
- Use fixtures for reusable test setup
- Name test functions descriptively: `test_<functionality>_<condition>`
- Include both positive and negative test cases
- Test edge cases and boundary conditions
- Test precision and rounding behavior

## Precision and Rounding
- Use Python's `decimal` module for financial calculations
- Apply `ROUND_HALF_UP` rounding for financial-grade precision
- Quantize results to 2 decimal places for currency representation
- Document precision requirements in specification documents

## Dependency Management
- List all dependencies in `requirements.txt`
- Pin specific versions for production deployments
- Regularly update dependencies to address security vulnerabilities
- Use virtual environments for isolation

## Git Workflow
- Use descriptive commit messages following conventional commits format
- Create feature branches for new functionality
- Submit pull requests for code reviews
- Keep commits focused and atomic
- Maintain a clean git history

## Business Logic Documentation
- Maintain business logic in versioned specification documents
- Use LaTeX for mathematical formulas in Markdown documents
- Clearly define variables and their meanings
- Include validation cases with expected inputs and outputs
- Update specifications when business requirements change
