from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('',views.home,name="home"),
    path('logout/', views.logoutUser, name="logout"),
    path('home/', views.home, name='home'),
    path("room/<str:pk>/",views.room,name="room"),
    path("room/",views.room,name="room"),
    path("create-room/",views.createRoom,name="create-room"),
    path("update-room/<str:pk>/",views.updateRoom,name="update-room"),
    path("delete-room/<str:pk>/",views.deleteRoom,name="delete-room"),
    path("tryform/",views.tryform,name="tryform"),    
]