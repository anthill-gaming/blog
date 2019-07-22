# For more details about routing, see
# http://www.tornadoweb.org/en/stable/routing.html
from tornado.web import url
from . import handlers


route_patterns = [
    url(r'^/post/(?P<id>[^/]+)/?$', handlers.PostHandler, name='post'),
    url(r'^/post/?$', handlers.PostHandler, name='post_create'),
    url(r'^/posts/?$', handlers.PostListHandler, name='posts'),

    url(r'^/category/(?P<id>[^/]+)/posts/?$', handlers.CategoryPostListHandler, name='category_posts'),
    url(r'^/category/(?P<id>[^/]+)/?$', handlers.CategoryHandler, name='category'),
    url(r'^/category/?$', handlers.CategoryHandler, name='category_create'),
    url(r'^/categories/?$', handlers.CategoryListHandler, name='categories'),
]
