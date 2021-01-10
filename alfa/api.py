from rest_framework import routers
from alfaapp import views as myapp_views

router = routers.DefaultRouter()
router.register(r'posts', myapp_views.SerPostView)