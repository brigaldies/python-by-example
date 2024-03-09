"""
Database access examples using SQLAlchemy.
"""

import argparse
import logging

from examples.registry.registry import register_example
from examples.database.database_sqlalchemy import sqlalchemy_version, database_connect, database_run_sql, \
    database_insert_and_commit, database_run_sql_with_bound_params, database_run_sql_with_orm_session, \
    database_metadata_create_ddl, database_drop_all_dll, database_metadata_create_dll_with_orm


@register_example
def sql_database(args: argparse.Namespace) -> None:
    """
    The Database examples.
    :param args: Command-line args.
    :return: None.
    """
    logging.info("Running async SQL Database access examples (args=%s)", args)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    _ = sqlalchemy_version()
    engine = database_connect("sqlite+pysqlite:///:memory:")
    _ = database_run_sql(engine, "select 'hello world'")
    database_insert_and_commit(engine)
    _ = database_run_sql_with_bound_params(engine)
    _ = database_run_sql_with_orm_session(engine)
    metadata_obj = database_metadata_create_ddl(engine)
    database_drop_all_dll(engine, metadata_obj)
    database_metadata_create_dll_with_orm(engine)
