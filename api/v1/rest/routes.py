# For more details about routing, see
# http://www.tornadoweb.org/en/stable/routing.html
from tornado.web import url
from . import handlers as h


route_patterns = [
    url(r'^/post/(?P<id>[^/]+)/?$', h.PostHandler, name='post'),
    url(r'^/post/?$', h.PostHandler, name='post_create'),
    url(r'^/posts/?$', h.PostListHandler, name='posts'),

    url(r'^/category/(?P<id>[^/]+)/posts/?$', h.CategoryPostListHandler, name='category_posts'),
    url(r'^/category/(?P<id>[^/]+)/?$', h.CategoryHandler, name='category'),
    url(r'^/category/?$', h.CategoryHandler, name='category_create'),
    url(r'^/categories/?$', h.CategoryListHandler, name='categories'),
]
