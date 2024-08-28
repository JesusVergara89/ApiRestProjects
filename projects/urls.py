from rest_framework import routers
from .api import ProjectsViewStes

router = routers.DefaultRouter()

router.register('api/projects', ProjectsViewStes, 'projects')

urlpatterns = router.urls