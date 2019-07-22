from anthill.platform.api.rest.handlers.detail import DetailMixin
from anthill.platform.api.rest.handlers.edit import (
    CreatingMixin, UpdatingMixin, DeletionMixin, ModelFormHandler)
from anthill.platform.api.rest.handlers.list import ListHandler
from blog.models import Post, Category


class PostHandler(CreatingMixin, UpdatingMixin, DeletionMixin, DetailMixin,
                  ModelFormHandler):
    """
    Multiple operations with posts:
        fetching, creating, updating and deleting.
    """
    model = Post

    def get_form_class(self):
        """Return the form class to use in this handler."""
        form_class = super().get_form_class()
        if self.request.method in ('PUT',):  # Updating
            # Patching form meta
            setattr(form_class.Meta, 'all_fields_optional', True)
            setattr(form_class.Meta, 'assign_required', False)
        return form_class


class PostListHandler(ListHandler):
    """Get list of posts."""
    model = Post


class CategoryPostListHandler(PostListHandler):
    """Get list of posts belongs to some category."""
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter_by(category_id=self.path_kwargs['id'])
        return queryset


class CategoryHandler(CreatingMixin, UpdatingMixin, DeletionMixin, DetailMixin,
                      ModelFormHandler):
    """
    Multiple operations with post categories:
        fetching, creating, updating and deleting.
    """
    model = Category

    def get_form_class(self):
        """Return the form class to use in this handler."""
        form_class = super().get_form_class()
        if self.request.method in ('PUT',):  # Updating
            # Patching form meta
            setattr(form_class.Meta, 'all_fields_optional', True)
            setattr(form_class.Meta, 'assign_required', False)
        return form_class


class CategoryListHandler(ListHandler):
    """Get list of post categories."""
    model = Category
