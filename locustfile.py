from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        """Simulate user login at the start of test"""
        self.client.post("/login", {
            "username": "test_user",
            "password": "test_password"
        })

    @task(1)
    def index_page(self):
        self.client.get("/")
        
    @task(2)
    def browse_products(self):
        # Simulate browsing product pages
        self.client.get("/products")
        self.client.get("/products/category/electronics")
        self.client.get("/products/category/clothing")
        
    @task(1)
    def view_product_details(self):
        # Simulate viewing individual product pages
        product_ids = ["1", "2", "3", "4", "5"]
        for product_id in product_ids:
            self.client.get(f"/product/{product_id}")
            
    @task(3)
    def search_products(self):
        # Simulate product search
        search_terms = ["laptop", "phone", "headphones"]
        for term in search_terms:
            self.client.get(f"/search?q={term}")
            
    @task(1)
    def shopping_cart(self):
        # Simulate cart operations
        self.client.get("/cart")
        self.client.post("/cart/add", json={
            "product_id": "123",
            "quantity": 1
        })
        
    @task(1)
    def checkout_flow(self):
        # Simulate checkout process
        self.client.get("/checkout")
        self.client.post("/checkout/shipping", json={
            "address": "123 Test St",
            "city": "Test City",
            "zip": "12345"
        })
        
    @task(2)
    def contact_form(self):
        # Simulate form submission
        self.client.post("/contact", json={
            "name": "Test User",
            "email": "test@example.com",
            "message": "This is a test message"
        })
