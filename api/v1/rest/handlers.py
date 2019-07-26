from anthill.platform.api.rest.handlers.detail import DetailMixin
from anthill.platform.api.rest.handlers.edit import (
    CreatingMixin, UpdatingMixin, DeletionMixin, ModelFormHandler)
from anthill.platform.api.rest.handlers.list import ListHandler
from blog.models import Post, Category


class PostHandler(CreatingMixin, UpdatingMixin, DeletionMixin, DetailMixin,
                  ModelFormHandler):
    """Multiple operations with posts."""
    queryset = Post.query.filter_by(active=True)


class PostListHandler(ListHandler):
    """Get list of posts."""
    queryset = Post.query.filter_by(active=True)


class CategoryPostListHandler(PostListHandler):
    """Get list of posts belongs to some category."""
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter_by(category_id=self.path_kwargs['id'])
        return queryset


class CategoryHandler(CreatingMixin, UpdatingMixin, DeletionMixin, DetailMixin,
                      ModelFormHandler):
    """Multiple operations with post categories."""
    model = Category


class CategoryListHandler(ListHandler):
    """Get list of post categories."""
    model = Category
