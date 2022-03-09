from fastapi.testclient import TestClient
from ..src.main import app

client = TestClient(app)

def test_stores():
    response = client.get("/stores")
    assert response.status_code == 200
    assert response.json() == {
        'dd4cf820-f946-4f38-8492-ca5dfeed0d74','Djurjouren', 
        '75040436-56de-401b-8919-8d0063ac9dd7', 'Djuristen',
        'ff53d831-c2fe-4fe8-9f67-5d69118670f2', 'Den Lilla Djurbutiken',
        '676df1a1-f1d1-4ac5-9ee3-c58dfe820927', 'Den Stora Djurbutiken',
        'a04bb312-9738-4db2-a7a5-ed6be9938afd', 'Noahs Djur & Båtaffär'
    }