from rest_framework.routers import DefaultRouter
from .viewsets import ElementViewSet, CategoryViewSet, TypeViewSet, CommentViewSet

router_listelement = DefaultRouter()
router_category = DefaultRouter()
router_type = DefaultRouter()
router_comment = DefaultRouter()

router_listelement.register(prefix='element', basename='element', viewset=ElementViewSet)
router_category.register(prefix='category', basename='category', viewset=CategoryViewSet)
router_type.register(prefix='type', basename='type', viewset=TypeViewSet)
router_comment.register(prefix='comment', basename='comment', viewset=CommentViewSet)
