from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts),
    path('/subscribe/<cat_id>', views.subscribe),
    path('/unsubscribe/<cat_id>', views.unsubscribe),
]
