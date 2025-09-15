# Load Testing with Locust

This project contains load testing scripts using Locust.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
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

## Web Interface Parameters

### Host
The base URL of your application to test. Include protocol (http/https) and port if needed (e.g., http://localhost:3000, https://api.example.com).

### Number of Users
Total concurrent virtual users to simulate. This represents the peak load you want to test.
- Typical starting values: 10-50 users
- For production testing: 100-1000+ users depending on your application's capacity
- Start small and increase gradually to find breaking points

### Spawn Rate
How many users to start per second. Controls how quickly the load ramps up.
- Typical values: 1-10 users/second
- Lower rates (1-2) provide gentler load increases, better for identifying performance degradation
- Higher rates simulate sudden traffic spikes

### Controls
- **Start**: Begins the test with specified parameters
- **Stop**: Immediately halts all users and ends the test
- Monitor the real-time charts for response times, RPS (requests per second), and failure rates

## Modifying Tests

Edit `locustfile.py` to modify the test scenarios. The file includes:
- Login simulation in `on_start` (currently set for HTML forms; API example commented)
- Commented placeholder tasks (e-commerce simulation examples)
- Active basic tasks for documented endpoints:
  - GET /
  - GET /api/endpoint
  - POST /api/items

Uncomment and customize the placeholder tasks or add new tasks for your specific endpoints. Update login method based on whether your app uses HTML forms or API authentication.

## Reports

Locust provides real-time metrics and can export results in CSV format.