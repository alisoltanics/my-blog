from django.urls import path

from .views import (posts_api_view, get_post_detail_api_view)


urlpatterns = [
    path('', posts_api_view, name="posts"),
    path('<int:id>', get_post_detail_api_view, name="get_post"),
]
