from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='statuses'),
    path('', views.StatusesListView.as_view(), name='statuses'),
    path('create/', views.StatusesCreateView.as_view(), name='statuses_create'),
    path('<int:pk>/update/', views.StatusesUpdateView.as_view(), name='statuses_update'),
    path('<int:pk>/delete/', views.StatusesDeleteView.as_view(), name='statuses_delete'),
]
