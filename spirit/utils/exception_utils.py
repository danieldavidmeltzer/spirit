import logging


def retry_on_exception(exception_type, max_tries):
    """
    decorator creator (2nd order)
    Args:
        exception_type: exception type to retry for
        max_tries: max number of tries

    Returns:

    """

    def retry(f):
        def wrapper(*args, **kwargs):
            for i in range(max_tries):
                try:
                    f(*args, **kwargs)
                except exception_type as error:
                    logging.exception(f"{error}, but retrying."
                                      f"try number {i + 1} out of {max_tries}")
                    continue
                break  # if succeed to finish

        return wrapper

    return retry
