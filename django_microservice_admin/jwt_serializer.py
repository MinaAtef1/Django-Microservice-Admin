from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class jwt_serializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token