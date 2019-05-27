def posts_list_serializer(posts):
    result_data = {
            "results": list(map(lambda post: {
                "id": post.id,
                "user": post.user.username,
                "title": post.title,
                "description": post.description,
                "image": post.image_absolute_url
            }, posts))
    }
    return result_data


def post_detail_serializer(post):
    result_data = {
        "id": post.id,
        "user": post.user.username,
        "title": post.title,
        "description": post.description,
        "image": post.image_absolute_url
    }
    return result_data
