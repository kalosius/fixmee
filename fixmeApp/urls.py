from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('mechanic/', views.mechanic, name="mechanic"),
    path('repairlocation/', views.repairlocation, name="repairlocation"),
    path('washingbay/', views.washingbay, name="washingbay"),
    path('login/', views.loginUser, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_user, name='logout'),
    path('mechanic-api/', views.mechanic_list, name="mechanic-api"),
    path('car-api/', views.car_api, name="car_api"),
    path('mechanic-api/<int:id>', views.mechanic_detail, name="mechanic"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('mechanic_detail/<int:id>', views.about_mechanic, name="about_mechanic"),
    path('chat_with_mechanic/<int:mechanic_id>/', views.chat_with_mechanic, name='chat_with_mechanic'),
    path('send_message/<int:mechanic_id>/', views.send_message, name='send_message'),
    path('map/', views.map_view, name='map_view'),
    path('search/', views.search, name='search'),
    path('settings/', views.settings_page, name='settings'),
    path('notifications/', views.notifications, name='notifications'),
]