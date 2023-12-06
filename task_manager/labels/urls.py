from django.urls import path
from . import views

urlpatterns = [
    path('', views.LabelsListView.as_view(), name='labels'),
    path('create/', views.LabelsCreateView.as_view(), name='labels_create'),
    path(
        '<int:pk>/update/',
        views.LabelsUpdateView.as_view(),
        name='labels_update'
    ),
    path(
        '<int:pk>/delete/',
        views.LabelsDeleteView.as_view(),
        name='labels_delete'
    ),
]
