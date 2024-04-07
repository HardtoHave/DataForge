from django.urls import path
from .views import DataFileListView, DataFileUploadedView

urlpatterns = [
    path('upload/', DataFileUploadedView.as_view(), name='data-file-uploaded'),
    path('list/', DataFileListView.as_view(), name='data-file-list'),
]
