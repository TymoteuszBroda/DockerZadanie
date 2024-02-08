import databases
import sqlalchemy

DATABASE_URL = "postgresql://user:password@localhost/packagemanagement"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
packages = sqlalchemy.Table(
    "packages",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("content", sqlalchemy.String),
    sqlalchemy.Column("assigned_to", sqlalchemy.String),
)

elves = sqlalchemy.Table(
    "elves",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("is_available", sqlalchemy.Boolean),
)