def save_parsing_result(parsing_result, saver, mongo_db):
    """
    save parsing_result
    Args:
        parsing_result: parsing result
        saver: saver to save sub values
        mongo_db: mongo_db to use to save

    Returns:
    None(implicitly)
    """

    result_object_id = saver(parsing_result.result,
                             mongo_db=mongo_db)

    snapshot_object_id = saver(parsing_result.snapshot,
                               result_object_id=result_object_id,
                               parser_name=parsing_result.result.parser_name,
                               mongo_db=mongo_db)
    # save user
    saver(parsing_result.user,
          snapshot_object_id=snapshot_object_id,
          mongo_db=mongo_db)
    # save snapshot with user id


save_parsing_result.field = "RepresentationParsingResult"
