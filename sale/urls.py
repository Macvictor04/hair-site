from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('list_product/', views.list_product, name="products"),
    path('product_detail/<int:id>/', views.product_detail, name="product_detail"),
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('submit_feedback/', views.submit_feedback, name="submit_feedback"),
         
]
