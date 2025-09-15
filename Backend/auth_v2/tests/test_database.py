import pytest
from tortoise.contrib.test import finalizer, initializer


@pytest.fixture(scope="session", autouse=True)
async def initialize_tests():
    await initializer(
        ["app.models"],
        db_url="sqlite://:memory:",
        app_label="models",
    )
    yield
    await finalizer()



'''
@pytest.mark.asyncio
async def test_create_author():
    author = await Author.create(name="Тестовый автор")
    assert author.name == "Тестовый автор"
    assert author.id is not None
'''