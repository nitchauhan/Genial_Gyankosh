from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'Login', Login)
router.register(r'Dashboard', Dashboard)
router.register(r'Question', Question)
router.register(r'Answer', Answer)

# router.register(r'Model', ModelAPIView)

urlpatterns = []
urlpatterns += router.urls