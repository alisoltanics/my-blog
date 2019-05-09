from django.http import JsonResponse

from .models import Post
from .serializers import posts_list_serializer

from utils.paginate import paginate


def posts_api_view(request):

    if request.method == "GET":
        page = request.GET.get('page', 1)
        page_size = 2
        posts = Post.objects.all()
        posts = paginate(
            objects=posts,
            page=page,
            page_size=page_size
        )
        result_data = posts_list_serializer(posts)
        return JsonResponse(result_data)
