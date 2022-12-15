from rest_framework import routers

from .api import StudentViewSet, RegistrationViewSet

app_name = "registration"

router = routers.DefaultRouter()
router.register(r"student", StudentViewSet, basename="student")
router.register(r"registration", RegistrationViewSet, basename="registration")

urlpatterns = router.urls
