from django.urls import path
from .views import HomeView, ArticleView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<int:pk>/', ArticleView.as_view(), name='ArticleView'),
]
