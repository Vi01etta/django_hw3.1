from measurements import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# TODO: настройте роутер и подключите `ProjectViewSet` и `MeasurementViewSet`


router = DefaultRouter()
router.register("project", views.ProjectViewSet)
router.register("measurment", views.MeasurementViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
