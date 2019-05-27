from django.http import JsonResponse

from .models import Post
from .serializers import posts_list_serializer, post_detail_serializer

from utils.paginate import paginate


def posts_api_view(request):

    if request.method == "GET":
        page = request.GET.get('page', 1)
        page_size = 10
        posts = Post.objects.all()
        posts = paginate(
            objects=posts,
            page=page,
            page_size=page_size
        )
        result_data = posts_list_serializer(posts)
        return JsonResponse(result_data)


def get_post_detail_api_view(request, id):

    if request.method == "GET":
        try:
            post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            return JsonResponse({'detail': 'Post not found'}, status=404)
        result_data = post_detail_serializer(post)
        return JsonResponse(result_data)
