from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from academics.views import DirectionViewSet, FacultyViewSet, GroupViewSet
from users.views import StudentViewSet

router = DefaultRouter()
router.register('faculties', FacultyViewSet)
router.register('directions', DirectionViewSet)
router.register('groups', GroupViewSet)
router.register('students', StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
