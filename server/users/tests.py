from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory
from .serializers import UserListSerializer
from .views import UserViewSet
from authen.models import roles
 
def create_user(self):
    self.client = APIClient()
    self.user = User(first_name='test_user',last_name='test',email=
    'test@gmail.com',username='test',password="abc123")
    self.user.set_password("abc123")
    self.user.save()
    self.token = Token.objects.create(user=self.user)
 
class UserLoginTestCase(APITestCase):
 
    @classmethod
    def setUp(self):
        # SetUp required environment for tests
        create_user(self)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
 
 
    def test_user_login(self):
        data = {'username':'test','password':"abc123"}
        login_url = reverse('login')
        response = self.client.post(login_url,data)
        # resp = response.json()
        self.assertEqual(response.status_code,302)
    
    def test_change_role_to_SM(self):
        data = {'roles':'dev'}
        roles.objects.filter(user=self.user.id).update(role='sm')

        print("id: ",self.user.roles)
        url = reverse('user-change-role',args=[self.user.id])


        response = self.client.patch(url,data)

        self.assertEqual(response.status_code, 200)



    # def test_get_all_users(self):
    #     url = reverse('user-list')
    #     response = self.client.get    (url)
    #     users = User.objects.all()
    #     factory = APIRequestFactory()
    #     request = factory.get('users')
    #     serializer = UserListSerializer(users,context={'request': request},many=True)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, 200)

    def tearDown(self):
        # Clean up after each test
        self.user.delete()