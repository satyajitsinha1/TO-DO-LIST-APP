from django.urls import path
from. import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.userlogin, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.userlogout,name='logout'),
    path('finished/<int:id>/',views.finished,name='finished'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
