from locust import HttpUser, task, between


class ChatTestUser(HttpUser):
    # Wait time between tasks
    wait_time = between(1, 2)

    @task
    def send_message(self):
        # Simulate sending a POST request to the chat app
        self.client.post("/", data={"username": "test_user", "message": "Hello from Locust!"})
