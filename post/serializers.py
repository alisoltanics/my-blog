def posts_list_serializer(posts):
    result_data = {
            "results": list(map(lambda post: {
                "id": post.id,
                "user": post.user.username,
                "title": post.title,
                "description": post.description
            }, posts))
    }
    return result_data
