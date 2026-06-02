MAX_FILE_SIZE = 5 * 1024 * 1024


def validate_file_size(
    file_size: int
):
    return file_size <= MAX_FILE_SIZE