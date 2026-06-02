def paginate(
    page: int,
    limit: int
):
    offset = (page - 1) * limit

    return {
        "offset": offset,
        "limit": limit
    }