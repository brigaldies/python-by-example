"""
Database access examples using SQLAlchemy.
"""

import argparse
import logging

from examples.registry.registry import register_example
from examples.database.database_sqlalchemy import sqlalchemy_version, database_connect, database_run_sql, \
    database_insert_and_commit, database_run_sql_with_bound_params, database_run_sql_with_orm_session


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
