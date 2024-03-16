"""
Database SQL Database access using the tutorial in https://docs.sqlalchemy.org/en/20/tutorial/index.html
"""
import logging

import sqlalchemy
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, insert, select, \
    bindparam
from sqlalchemy.orm import Session
from examples.database.model.model import Base

LOG = logging.getLogger("examples")


def sqlalchemy_version() -> str:
    """
    Log SQLAlchemy version.
    :return: SQLAlchemy version.
    """
    version = sqlalchemy.__version__
    LOG.info("SQLAlchemy version: %s", version)
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
    LOG.info("Database engine created")
    return engine


def database_run_sql(engine: sqlalchemy.Engine, sql: str) -> sqlalchemy.Sequence:
    """
    Connect and run an SQL statement.
    :param engine: Database engine.
    :param sql: Sql Expression.
    :return: SQL statement result.
    """
    with engine.connect() as conn:
        sql_result = conn.execute(text(sql))
        results = sql_result.all()
        LOG.info("Result: %s", results)
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
            LOG.info("x=%d, y=%d", x, y)

        # Positional
        for row in results:
            LOG.info("x=%d, y=%d", row[0], row[1])

        # Tuple attribute name
        for row in results:
            LOG.info("x=%d, y=%d", row.x, row.y)

        # Via a map
        # Fetch the results again so that we can map them.
        result = conn.execute(text(f"select * from {table_name}"))
        for row in result.mappings():
            LOG.info("x=%d, y=%d", row['x'], row['y'])


def database_run_sql_with_bound_params(engine: sqlalchemy.Engine) -> sqlalchemy.Sequence:
    """
    Run a SQL select with "bound" parameters.
    :param engine: Database engine.
    :return: Results.
    """
    table_name = "test1"
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT x, y FROM {table_name} WHERE y > :y"), {"y": 2})
        results = result.all()
        for row in results:
            LOG.info("row: %s", row)
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
            LOG.info("row: %s", row)
        return results


def database_metadata_create_ddl(engine: sqlalchemy.Engine) -> sqlalchemy.MetaData:
    """
    Create a table and return the database's metadata.
    :param engine: Database engine.
    :return: Metadata
    """
    metadata_obj = MetaData()
    _ = Table(
        "user_account",
        metadata_obj,
        Column("id", Integer, primary_key=True),
        Column("name", String(30), nullable=False),
        Column("fullname", String, nullable=False)
    )

    _ = Table(
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


def database_metadata_read_table_ddl_from_db(engine: sqlalchemy.Engine) -> sqlalchemy.Table:
    """
    Read an existing table's DDL.
    :param engine: Database engine.
    :return: Table's DDL.
    """
    metadata_obj = Base.metadata
    test_table = Table("test1", metadata_obj, autoload_with=engine)
    LOG.info("Table: %s", repr(test_table))
    return test_table


def database_insert_record(engine: sqlalchemy.Engine) -> sqlalchemy.Result:
    """
    Insert a record.
    :param engine: Engine.
    :return: Insert's result.
    """
    metadata_obj = Base.metadata
    user_table = Table("user_account", metadata_obj, autoload_with=engine)
    stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")
    LOG.info("Insert SQL: %s", str(stmt))
    LOG.info("Insert params: %s", stmt.compile().params)
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()
        LOG.info("primary key: %s", str(result.inserted_primary_key))
        LOG.info("Rows count inserted: %d", len(result.inserted_primary_key_rows))
        return result


def database_insert_records(engine: sqlalchemy.Engine) -> None:
    """
    Insert several records.
    :param engine: Database engine.
    :return: None.
    """
    metadata_obj = Base.metadata
    user_table = Table("user_account", metadata_obj, autoload_with=engine)
    with engine.connect() as conn:
        result = conn.execute(
            insert(user_table),
            [
                {"name": "sandy", "fullname": "Sandy Cheeks"},
                {"name": "patrick", "fullname": "Patrick Star"},
            ],
        )
        LOG.info("Multi-record insert result: %s", str(result.inserted_primary_key_rows))
        conn.commit()

    scalar_subq = (
        select(user_table.c.id)
        .where(user_table.c.name == bindparam("username"))
        .scalar_subquery()
    )

    address_table = Table("address", metadata_obj, autoload_with=engine)
    with engine.connect() as conn:
        result = conn.execute(
            insert(address_table).values(user_id=scalar_subq),
            [
                {"username": "spongebob", "email_address": "spongebob@sqlalchemy.org"},
                {"username": "sandy", "email_address": "sandy@sqlalchemy.org"},
                {"username": "sandy", "email_address": "sandy@squirrelpower.org"},
            ],
        )
        conn.commit()
