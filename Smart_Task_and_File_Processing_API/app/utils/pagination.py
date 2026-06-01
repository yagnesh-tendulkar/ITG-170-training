from math import ceil


def paginate(
    data: list,
    page: int = 1,
    limit: int = 10
):
    """
    Paginate a list of data.

    Args:
        data (list): Complete dataset
        page (int): Current page number
        limit (int): Records per page

    Returns:
        dict: Paginated response
    """

    total_records = len(data)

    total_pages = ceil(total_records / limit) if total_records > 0 else 1

    start = (page - 1) * limit

    end = start + limit

    paginated_data = data[start:end]

    return {
        "page": page,
        "limit": limit,
        "total_records": total_records,
        "total_pages": total_pages,
        "data": paginated_data
    }