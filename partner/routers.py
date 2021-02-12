from rest_framework import routers
from .views import CategoryModelViewSet



router = routers.SimpleRouter()
router.register(r'categories', CategoryModelViewSet)
urlpatterns = router.urls



