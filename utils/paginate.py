def paginate(objects, page, page_size):
    start = (int(page)-1)*page_size
    end = int(page)*page_size
    objects = objects[start:end]
    return objects
