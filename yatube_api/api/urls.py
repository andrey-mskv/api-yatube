from rest_framework.authtoken import views
from rest_framework import routers
from django.urls import include, path

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
