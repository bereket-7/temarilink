from django.urls import path
from .views import DownloadReportCardView

app_name = 'reports'

urlpatterns = [
    path('download/<uuid:pk>/', DownloadReportCardView.as_view(), name='download_pdf'),
]
