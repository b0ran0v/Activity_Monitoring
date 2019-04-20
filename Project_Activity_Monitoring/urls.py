from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('accounts/login', views.login_view, name='login'),
    path('accounts/logout', views.logout_view, name='logout'),
    path('project_list', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/new/', views.project_new, name='project_new'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task_list', views.task_list, name='task_list'),
    path('task/new/', views.task_new, name='task_new'),
    path('task/<int:pk>/finish', views.task_finish, name='task_finish'),
]

