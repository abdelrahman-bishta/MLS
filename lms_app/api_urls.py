from rest_framework.routers import DefaultRouter
from .views import BookViewSet   # عدّل حسب اسمك

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls
