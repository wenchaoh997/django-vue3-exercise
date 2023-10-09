```bash
python manage.py createsuperuser
```

# Serializer



# Account

```py
# settings.py
AUTH_USER_MODEL = 'accounts.MyUser'

from django.contrib.auth import get_user_model
User = get_user_model() # User = accounts.MyUser
```

> `BaseUserManager` do not have `create_superuser`. Define one.


## django.contrib.auth.models.AbstractBaseUser


## django.contrib.auth.models.BaseUserManager


# Permission


# Order

----------------------

# Frontend

```
npm create vue@latest
```

