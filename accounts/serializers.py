from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        read_only_fields = ("id",)


    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("user with this email already exists.")
        return value.lower()


    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("a user with this username already exists")
        return value


    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, token):
        token = super().get_token(user)
        token['email'] = user.email
        token['username'] = user.username


    def validate(self, attrs):
        """Customize the HTTP response body of POST /api/auth/login/."""
        # Let the parent do the actual auth (username/password check, etc.)
        data = super().validate(attrs)

        # `self.user` is set by the parent's validate() when auth succeeds.
        # We merge user info into the response alongside the tokens.
        data["user"] = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
        }
        return data