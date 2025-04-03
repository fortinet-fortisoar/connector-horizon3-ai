# Testing the Horizon AI Connector

This document provides guidelines for setting up and running tests for the Horizon AI connector.

## Setup

1. **Configure Test Data**
   
   First, create a proper `data.py` file by copying the sample and adding your API token:
   
   ```bash
   cp tests/data_sample.py tests/data.py
   ```
   
   Then edit `tests/data.py` to insert your API token:
   
   ```python
   config = {
       "verify_ssl": True,
       "api_token": "YOUR_API_TOKEN_HERE",
       "server_url": "https://api.horizon3ai.com/"
   }
   ```

2. **Install Dependencies**
   
   Install the required testing packages:
   
   ```bash
   pip install -r tests/requirements.txt
   ```

## Running Tests

### Run All Tests

To run all tests for the connector:

```bash
pytest tests/test_horizon_connector.py -v
```

### Run Specific Tests

To run a specific test function:

```bash
pytest tests/test_horizon_connector.py::test_check_health -v
```