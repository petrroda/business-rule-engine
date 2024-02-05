from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def pricing(self):
        self.client.post('/pricing', data = """{
  "Job Profile": {
    "id": "string",
    "benefits": [
      {
        "id": 0
      }
    ]
  },
  "User Profile": {
    "id": "string",
    "roles": [
      {
        "id": 0
      }
    ],
    "benefits": [
      {
        "id": 0
      }
    ]
  }
}""")