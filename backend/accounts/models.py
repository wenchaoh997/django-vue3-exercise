from django.db import models, reset_queries
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import jwt
import datetime
import backend.settings as settings

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, isStaff=False, isAdmin=False, isActive=True):
        if not email:
            raise ValueError("Users must have an email")

        if not password:
            raise ValueError("Users must have an password")

        userObj = self.model(email=self.normalize_email(email))

        userObj.set_password(password)
        userObj.staff = isStaff
        userObj.admin = isAdmin
        userObj.active = isActive
        userObj.save(using=self._db)

        return userObj

    def create_staffuser(self, email, password):
        user = self.create_user(email, password, isStaff=True)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password, isStaff=True, isAdmin=True)

        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length=15, unique=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        token = jwt.encode({
            "exp": datetime.datetime.now() + datetime.timedelta(days=1),
            "iat": datetime.datetime.now(),
            "data":{
                "name": self.email
            }
        }, settings.SECRET_KEY, algorithm="HS256")
        return token.encode("utf-8").decode("utf-8")
    
    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_active(self):
        return self.active
