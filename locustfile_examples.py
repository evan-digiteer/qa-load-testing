from locust import HttpUser, task, between
import re  # Required for Rails CSRF token extraction

# Example Locust file with placeholder tasks for different application types
# Uncomment and modify these examples for your specific use case

class ExampleWebsiteUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        """Simulate user login at the start of test"""
        # Placeholder for API login (JSON):
        # self.client.post("/api/login", json={
        #     "username": "test_user",
        #     "password": "test_password"
        # })

        # Placeholder for generic HTML form login (form data):
        # self.client.post("/login", data={
        #     "username": "test_user",
        #     "password": "test_password"
        # })

        # Example Rails HTML form login with CSRF protection:
        # import re
        # login_page = self.client.get("/admin/login")
        # token_match = re.search(r'name="authenticity_token" value="([^"]+)"', login_page.text)
        # if token_match:
        #     authenticity_token = token_match.group(1)
        #     response = self.client.post("/admin/login", data={
        #         "authenticity_token": authenticity_token,
        #         "user[email]": "your-email@example.com",
        #         "user[password]": "your-password",
        #         "button": ""
        #     })
        #     if response.status_code in [200, 302] or "dashboard" in response.url:
        #         self.client.get("/admin/dashboard")

    # Placeholder tasks commented out - replace with actual API endpoints
    # @task(1)
    # def index_page(self):
    #     self.client.get("/")

    # @task(2)
    # def browse_products(self):
    #     # Simulate browsing product pages
    #     self.client.get("/products")
    #     self.client.get("/products/category/electronics")
    #     self.client.get("/products/category/clothing")

    # @task(1)
    # def view_product_details(self):
    #     # Simulate viewing individual product pages
    #     product_ids = ["1", "2", "3", "4", "5"]
    #     for product_id in product_ids:
    #         self.client.get(f"/product/{product_id}")

    # @task(3)
    # def search_products(self):
    #     # Simulate product search
    #     search_terms = ["laptop", "phone", "headphones"]
    #     for term in search_terms:
    #         self.client.get(f"/search?q={term}")

    # @task(1)
    # def shopping_cart(self):
    #     # Simulate cart operations
    #     self.client.get("/cart")
    #     self.client.post("/cart/add", json={
    #         "product_id": "123",
    #         "quantity": 1
    #     })

    # @task(1)
    # def checkout_flow(self):
    #     # Simulate checkout process
    #     self.client.get("/checkout")
    #     self.client.post("/checkout/shipping", json={
    #         "address": "123 Test St",
    #         "city": "Test City",
    #         "zip": "12345"
    #     })

    # @task(2)
    # def contact_form(self):
    #     # Simulate form submission
    #     self.client.post("/contact", json={
    #         "name": "Test User",
    #         "email": "test@example.com",
    #         "message": "This is a test message"
    #     })

    # Example API tasks (uncomment and modify for API-based applications)
    # @task(1)
    # def get_api_data(self):
    #     self.client.get("/api/data")
    #
    # @task(1)
    # def post_api_create(self):
    #     self.client.post("/api/items", json={"name": "item", "value": "test"})