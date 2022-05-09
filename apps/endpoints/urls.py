from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EndpointsViewSet, MLAlgorithmViewSet, MLAlgorithm_StatusViewSet, MLRequestViewSet, PredictView

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointsViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithm_StatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    path(r"api/v1/", include(router.urls)),
    path(r"api/v1/classifier/predict", PredictView.as_view(), name='predict')
]