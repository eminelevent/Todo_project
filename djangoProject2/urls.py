from django.urls import path
from . import views
from todo.views import loginview

urlpatterns = [
    path('', loginview, name="loginview"),
    path('home',views.home, name="home"),
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('create/', views.create, name="create"),
    path('delete/<todos_id>', views.delete, name="delete"),
    path('finish/<todos_id>', views.finish, name="finish"),
    path('nofinish/<todos_id>', views.nofinish, name="nofinish"),
    path('update/<todos_id>', views.update, name="update"),

]