from ml_api.standardizer.api.views import StandardizeData
from django.urls import path

app_name = "standardize"

urlpatterns = [
    path("standardize/", StandardizeData.as_view())
]
