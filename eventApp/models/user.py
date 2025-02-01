from django.db import models
from ninja import Schema,ModelSchema
from enum import Enum
# from django.contrib.auth.models import
from django.contrib.auth.models import AbstractBaseUser
from datetime import datetime
class UserRole(str,Enum):
    ATTENDEE= 'attendee'
    ORGANIZER = 'organizer'
    ADMIN = 'admin'



class User(AbstractBaseUser):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    role = models.CharField(
        max_length=20,
        choices=[(role.value,role.name) for role in UserRole],
        default=[UserRole.ATTENDEE.value]
    )
    created_at= models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'


class UserIn(Schema):
    email:str
    password: str

class UserCreate(Schema):
    username: str
    email: str
    password: str
    role: UserRole = UserRole.ATTENDEE



class UserOut(Schema):
    id:int
    username:str
    email:str
    role:str
    created_at:datetime
    # class Meta:
    #     model = User
    #     fields = ["id", "username", "email", "role", "created_at"]



# -------------------- AUTH -------------------- #
class AuthToken(Schema):
    """Schema for returning JWT tokens"""
    token: str

class Error(Schema):
    """Schema for error responses"""
    error: str
