from django.urls import path
from . import views

urlpatterns = [
    path('', views.TasksListView.as_view(), name='tasks'),
    path('create/', views.TasksCreateView.as_view(), name='tasks_create'),
    path('<int:pk>/update/', views.TasksUpdateView.as_view(), name='tasks_update'),
    path('<int:pk>/delete/', views.TasksDeleteView.as_view(), name='tasks_delete'),
    path('<int:pk>/', views.TaskDetailedView.as_view(), name='task_detail'),
]
