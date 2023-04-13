from django.test import TestCase
from chat_app.models import User
# Create your tests here.

class BasicTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(email="aman@gmail.com",password="Test1234@")
        self.user = self.client.force_login(user)
    
    def test_signup(self):
        data = {
            "name": "dummy",
            "email": "dummy@gmail.com",
            "password":"password",
            "confirm_password": "password",
            "mobile": 123456789
        }
        response = self.client.post("/",data)

        self.assertEqual(response.status_code,201)

    def test_chat(self):
        data = {
            "text":"hi"
        }
        response = self.client.post('/chat/',data)

        self.assertEqual(response.status_code,200)