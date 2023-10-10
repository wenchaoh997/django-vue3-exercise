from rest_framework import serializers

from .models import User

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)

    def validate_email(self, value):
        if not self.context.get("login", False):
            user = User.objects.filter(email__iexact=value).exists()

            if user:
                raise serializers.ValidationError("Email is invalid")

            return value

    def save(self):
        email = self.validated_data["email"]
        password = self.validated_data["password"]

        user = User.objects.create_user(email=email, password=password)
        user.set_password(password)
        user.save()

        print("Create successfully", email, password)

        return user
