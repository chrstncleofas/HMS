from app import views
from django.urls import path
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [
    # Frontend API
    url(r'^booking$',views.reservationApi),
    url(r'^booking/([0-9]+)$',views.reservationApi),

    # Backend URL
    path('admin/', admin.site.urls), 
    path('', views.home, name='home'),
    path('login_page', views.login_page, name='login_page'),
    path('logout/', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('allList', views.allList, name='allList'),
    path('allUser', views.allUser, name='allUser'),
    path('<int:id>/view_info/', views.view_info, name='view_info'),
    path('<int:id>/view_user_info/', views.view_user_info, name='view_user_info'),
    path('delete_list/<int:id>', views.delete_list, name='delete_list'),
    path('delete_users/<int:id>', views.delete_users, name='delete_users'),
    path('edit_user_details/<int:id>', views.edit_user_details, name='edit_user_details'),
    path('createSuperUser/', views.createSuperUser, name='createSuperUser'),
]
