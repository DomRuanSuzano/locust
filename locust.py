from locust import HttpUser, task, between
import os

API_URL = os.getenv('API_URL')
if not API_URL.startswith("http"):
    API_URL = f"http://{API_URL}"

class QuickstartUser(HttpUser):

    host = API_URL
    wait_time = between(1, 2.5)

    @task
    def get_all(self):
        self.client.get("/items")