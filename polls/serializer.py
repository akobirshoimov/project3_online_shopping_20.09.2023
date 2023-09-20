from rest_framework.serializers import ModelSerializer
from .models import OnlineShoppingModel

class OnlineShoppingSer(ModelSerializer):
    class Meta:
        model = OnlineShoppingModel
        fields = ('__all__')
        