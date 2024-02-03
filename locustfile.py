from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def pricing(self):
        self.client.get("/pricing")