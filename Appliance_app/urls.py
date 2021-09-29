from rest_framework.routers import SimpleRouter

from .views import CategoryVievSet, AppliancesViewSet

router = SimpleRouter()
router.register('category', CategoryVievSet)
router.register('appliance', AppliancesViewSet)

urlpatterns = []

urlpatterns += router.urls