
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'categories', CategoryModelViewSet)
router.register(r'partner', PartnerModelViewSet)
router.register(r'socialnetwork', SocialNetworkViewSet)

urlpatterns = router.urls
