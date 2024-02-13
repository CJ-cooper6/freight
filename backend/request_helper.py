from flask import request


def get_pagination():
    current_page = int(request.args.get("currentPage", 1))
    current_page = max(current_page, 1)

    page_size = int(request.args.get("pageSize", 10))

    return current_page, page_size
