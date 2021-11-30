from sqlalchemy import DateTime
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import expression


class utcnow(expression.FunctionElement):
    type = DateTime()


@compiles(utcnow, "postgresql")
def pg_utcnow(_element, _compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"
