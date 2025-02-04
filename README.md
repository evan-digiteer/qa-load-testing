# Load Testing with Locust

This project contains load testing scripts using Locust.

## Setup

1. Install Locust globally:
   ```bash
   pip install locust
   ```

## Running Tests

1. Start Locust:
   ```bash
   locust
   ```

2. Open web interface at: http://localhost:8089

3. Enter your test parameters:
   - Number of users
   - Spawn rate
   - Host URL (e.g., http://your-api-url.com)

## Modifying Tests

Edit `locustfile.py` to modify the test scenarios. Current endpoints:
- GET /
- GET /api/endpoint
- POST /api/items

## Reports

Locust provides real-time metrics and can export results in CSV format.