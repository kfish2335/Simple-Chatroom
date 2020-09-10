from rest_framework import routers
from .api import chatViewSet

router = routers.DefaultRouter()
router.register('api/chat', chatViewSet, 'chat')

urlpatterns = router.urls