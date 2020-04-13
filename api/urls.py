from django.urls import path

from api import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'resources', views.ResourceViewSet, basename='resources')

urlpatterns = router.urls
urlpatterns += [
    path('total_cost/', views.TotalCostApiView.as_view())
]
