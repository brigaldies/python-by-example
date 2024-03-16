"""
Database access examples using SQLAlchemy.
"""

import argparse
import logging

from examples.registry.registry import register_example
from examples.database.database_sqlalchemy import sqlalchemy_version, database_connect, database_run_sql, \
    database_insert_and_commit, database_run_sql_with_bound_params, database_run_sql_with_orm_session, \
    database_metadata_create_ddl, database_drop_all_dll, database_metadata_create_dll_with_orm, \
    database_metadata_read_table_ddl_from_db, database_insert_record, database_insert_records

LOG = logging.getLogger("examples")


def setup_sqlalchemy_logging() -> None:
    """
    Set up the SQLAlchemy logging.
    :return: None.
    """
    logger = logging.getLogger("sqlalchemy.engine")
    logger.setLevel(logging.INFO)

    stdout_handler = logging.StreamHandler()
    logging_format = logging.Formatter("%(asctime)s | %(threadName)s | %(levelname)s | %(name).8s | %(message)s")
    stdout_handler.setFormatter(logging_format)
    logger.addHandler(stdout_handler)


@register_example
def sql_database(args: argparse.Namespace) -> None:
    """
    The Database examples.
    :param args: Command-line args.
    :return: None.
    """
    LOG.info("Running async SQL Database access examples (args=%s)", args)

    setup_sqlalchemy_logging()

    _ = sqlalchemy_version()
    engine = database_connect("sqlite+pysqlite:///:memory:")
    _ = database_run_sql(engine, "select 'hello world'")
    database_insert_and_commit(engine)
    _ = database_run_sql_with_bound_params(engine)
    _ = database_run_sql_with_orm_session(engine)
    metadata_obj = database_metadata_create_ddl(engine)
    database_drop_all_dll(engine, metadata_obj)
    database_metadata_create_dll_with_orm(engine)
    _ = database_metadata_read_table_ddl_from_db(engine)
    _ = database_insert_record(engine)
    database_insert_records(engine)
