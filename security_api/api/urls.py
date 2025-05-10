from django.urls import path
from api.views import ScanAPIView

urlpatterns = [
    path('scan/', ScanAPIView.as_view(), name='scan'),
]
