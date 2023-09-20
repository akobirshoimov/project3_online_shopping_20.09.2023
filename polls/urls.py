from django.urls import path
from .views import CreateOnlineShoppingView,UpdateOnlineShoppingView,ListOnlineShoppingView

urlpatterns = [
    path('all/',ListOnlineShoppingView.as_view()),
    path('create/',CreateOnlineShoppingView.as_view()),
    path('update/<int:shopping_id>/',UpdateOnlineShoppingView.as_view())
]
