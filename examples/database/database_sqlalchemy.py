"""
Database SQL Database access using the tutorial in https://docs.sqlalchemy.org/en/20/tutorial/index.html
"""
import importlib
import logging

import sqlalchemy
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session
from examples.database.model.model import Base


def sqlalchemy_version() -> str:
    """
    Log SQLAlchemy version.
    :return: SQLAlchemy version.
    """
    version = sqlalchemy.__version__
    logging.info("SQLAlchemy version: %s", version)
    return version


def database_connect(connection_string: str) -> sqlalchemy.Engine:
    """
    Connect to an in-memory SQLite database.

    "Connection" string:
    "sqlite+pysqlite:///:memory:"
    "sqlite": dialect.
    "pysqlite": DBA driver for SQLite.
    "/:memory:": In-memory database.

    :param connection_string: Database connection string.
    :return: Database engine
    """
    engine = create_engine(connection_string, echo=False)
    assert engine is not None
    logging.info("Database engine created")
    return engine


def database_run_sql(engine: sqlalchemy.Engine, sql: str) -> sqlalchemy.Sequence:
    """
    Connect and run the simplest SQL statement.
    :param engine: Database engine.
    :param sql: Sql Expression.
    :return: SQL statement result.
    """
    with engine.connect() as conn:
        sql_result = conn.execute(text(sql))
        results = sql_result.all()
        logging.info("Result: %s", results)
        return results


def database_insert_and_commit(engine: sqlalchemy.Engine) -> None:
    """
    Insert and commit a table record.
    :param engine: Database engine
    :return: None.
    """
    table_name = "test1"

    # Block with commit if successful, rollbar otherwise.
    with engine.begin() as conn:
        # Create a test table
        conn.execute(text(f"CREATE TABLE {table_name} (x int, y int)"))

        # Insert two records in the test table
        conn.execute(
            text(f"INSERT INTO {table_name} (x, y) VALUES (:x, :y)"),
            [
                {"x": 1, "y": 1},
                {"x": 2, "y": 4}
            ]
        )

    # Read the data back
    with engine.connect() as conn:
        result = conn.execute(text(f"select * from {table_name}"))

        # Different ways to access the rows

        # Save the results so that we can iterate over them several times
        results = list(result)

        # The most Python-esque
        for x, y in results:
            logging.info("x=%d, y=%d", x, y)

        # Positional
        for row in results:
            logging.info("x=%d, y=%d", row[0], row[1])

        # Tuple attribute name
        for row in results:
            logging.info("x=%d, y=%d", row.x, row.y)

        # Via a map
        # Fetch the results again so that we can map them.
        result = conn.execute(text(f"select * from {table_name}"))
        for row in result.mappings():
            logging.info("x=%d, y=%d", row['x'], row['y'])


def database_run_sql_with_bound_params(engine: sqlalchemy.Engine) -> sqlalchemy.Sequence:
    """
    Run a SQL select with "bound" parameters.
    :param engine: Basebase engine.
    :return: Results.
    """
    table_name = "test1"
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT x, y FROM {table_name} WHERE y > :y"), {"y": 2})
        results = result.all()
        for row in results:
            logging.info("row: %s", row)
        return results


def database_run_sql_with_orm_session(engine: sqlalchemy.Engine) -> sqlalchemy.Sequence:
    """
    Run a SQL select with the ORM Session object.
    :param engine: Database engine
    :return: Results.
    """
    table_name = "test1"
    stmt = text(f"SELECT x, y FROM {table_name} WHERE y > :y ORDER BY x, y")
    with Session(engine) as session:
        result = session.execute(stmt, {"y": 6})
        results = result.all()
        for row in results:
            logging.info("row: %s", row)
        return results


def database_metadata_create_ddl(engine: sqlalchemy.Engine) -> sqlalchemy.MetaData:
    """
    Create a table and return the database's metadata.
    :param engine: Database engine.
    :return: Metadata
    """
    metadata_obj = MetaData()
    user_table = Table(
        "user_account",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("name", String(30), nullable=False),
        Column("fullname", String, nullable=False)
    )

    address_table = Table(
        "address",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("user_id", ForeignKey("user_account.id"), nullable=False),
        Column("email_address", String, nullable=False),
    )
    metadata_obj.create_all(engine)
    return metadata_obj


def database_drop_all_dll(engine: sqlalchemy.Engine, metadata_obj: sqlalchemy.MetaData) -> None:
    """
    Drop all DDL.
    :param engine: Database engine.
    :param metadata_obj: Metadata object.
    :return: None.
    """
    metadata_obj.drop_all(engine)


def database_metadata_create_dll_with_orm(engine: sqlalchemy.Engine) -> None:
    """
    Create the DDL the ORM way.
    :param engine: Database engine.
    :return: None.
    """
    Base.metadata.create_all(engine)
