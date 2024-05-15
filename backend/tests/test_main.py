import pytest
from httpx import AsyncClient
from app.main import app

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://localhost") as ac:
        yield ac

@pytest.mark.asyncio
async def test_ask_endpoint(client):
    response = await client.post("/ask", json={"question": "O que é Produto A?"})
    assert response.status_code == 200
    assert "answer" in response.json()
    assert isinstance(response.json()["answer"], str)