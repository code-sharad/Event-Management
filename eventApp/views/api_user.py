
from ninja import Router

from ..models.user import User,UserCreate,UserOut,Error,UserIn
from ..models.event import Event,EventInSchema,EventOut
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import check_password
from datetime import datetime,timedelta
from django.conf import settings
from typing import List
from django.contrib.auth import login
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.contrib.auth import login

userRouter = Router()

# def create_jwt_token(user: User):
#     access_payload = {
#         "sub": user.username,
#         "exp": datetime.today() + timedelta(minutes=15)  # Short-lived access token
#     }
#     refresh_payload = {
#         "sub": user.username,
#         "exp": datetime.today() + timedelta(days=7)  # Long-lived refresh token
#     }
    
#     access_token = jwt.encode(access_payload, 'asfd', "HS256")
#     refresh_token = api_jwt.encode(refresh_payload, 'asdf', "HS256")
    
#     return access_token, refresh_token


@userRouter.get('/set-csrf-token',response={200:dict},tags=['user'],description="Get CSRF token")
def get_csrf_token(request):
    return {'csrf_token':get_token(request)}

# -------------------- USER API -------------------- #
@userRouter.post("/register", response={201: UserOut, 400: Error},tags=["user"],description="Register a new user")
def register(request, payload: UserCreate):
    if User.objects.filter(email=payload.email).exists():
        return 400, {"error": "Email already exists"}
    user = User.objects.create(
        username=payload.username,
        email=payload.email,
        password=payload.password,
        role=payload.role
    )
    return 201, user

@userRouter.post('/login',tags=['user'],description="Login a user")
def login_view(request, payload:UserIn):

    user = User.objects.filter(email=payload.email).first()
   
    response = JsonResponse({"message": "User registered successfully"})
    if user is not None:
        login(request, user)  # Use renamed auth_login
        # Return serialized user data
        return UserOut.from_orm(user)    
    else:
        return 400, {"message": "Invalid credentials"}
    


