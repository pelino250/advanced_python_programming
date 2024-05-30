Authentication is a crucial part of any web application. In Python, there are several ways to implement authentication. Here are some of the most common methods:

1. **Basic Authentication**: This is the simplest method of authentication. The client sends a request with an `Authorization` header. The header contains the word `Basic` followed by a space and a base64-encoded string `username:password`. On the server side, these credentials are decoded and checked against the stored values for authentication.

2. **Session Authentication**: This is a stateful authentication method. When a user logs in, the server creates a session for the user and sends a session ID back to the client. The client stores this session ID (usually in a cookie) and sends it with each subsequent request. The server checks this session ID to authenticate the user.

3. **Token Authentication**: This is a stateless authentication method. After successful login, the server generates a token (usually a JWT - JSON Web Token) and sends it back to the client. The client sends this token with each subsequent request in the `Authorization` header. The server validates this token to authenticate the user.

4. **OAuth**: This is a standard for access delegation. It's used when you want to give a third-party application access to your data without sharing your password. For example, when you log in to a website using your Google or Facebook account, that's OAuth.

Here's a simple example of how you might implement basic authentication in Python using the `requests` library:

```python
import requests
from requests.auth import HTTPBasicAuth

response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'pass'))

print(response.json())
```

For session and token authentication, you would typically use a web framework like Flask or Django, which provide built-in mechanisms for these types of authentication.

For OAuth, there are libraries like `oauthlib` that can help you implement it.

Remember, it's important to always secure your authentication process, for example by using HTTPS and storing passwords securely (never in plain text).

Django provides built-in support for both session and token-based authentication. Here's a brief overview of how you can use them:

**Session Authentication**

Session authentication is Django's default authentication system. When a user logs in, Django stores their ID in the session and every subsequent request from the same user is authenticated using data from the session.

Here's a basic example of how you can use Django's built-in views to handle login:

```python
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.
            ...
        ## delete me
        # def test_args(a, b):
        #     return a + b
        # # test_args(2, 1)
        # 
        # def test_kwargs(a=None, b=None, c=None, d=None):
        #     return a + b
        # test_kwargs(c=2, b=1)

```

**Token Authentication**

Token authentication is a simple, stateless authentication method. After successful login, the server generates a token and sends it back to the client. The client sends this token with each subsequent request in the `Authorization` header. The server validates this token to authenticate the user.

Django Rest Framework (DRF) provides built-in support for token authentication. Here's how you can use it:

First, you need to include `'rest_framework.authtoken'` in your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken',
    ...
]
```

Then, in your view, you can use the `Token` model to create a token for a user:

```python
from rest_framework.authtoken.models import Token

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            # Return the token to the client.
            ...
        else:
            # Return an 'invalid login' error message.
            ...
```

The client should include this token in the `Authorization` header of each subsequent request:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

On the server side, you can use the `TokenAuthentication` class provided by DRF to authenticate the request:

```python
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# example.com/test/ -> MyView
class MyView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        ...
```

Remember, you need to install Django Rest Framework to use token authentication. You can do this by running `pip install djangorestframework`.