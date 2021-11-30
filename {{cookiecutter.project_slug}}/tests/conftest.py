from typing import Generator

import pytest
from {{cookiecutter.package_name}}.db.base import Base

from tests.db import TestingSessionLocal, engine


@pytest.fixture(scope="session")
def db() -> Generator:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
