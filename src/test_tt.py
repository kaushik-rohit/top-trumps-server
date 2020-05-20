import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_card_query(client):
    # test game cnt 1
    res_1 = client.get('/game/1')
    docs_1 = json.loads(res_1.data)
    assert(len(docs_1) == 20)

    # test game cnt 5
    res_2 = client.get('/game/2')
    docs_2 = json.loads(res_2.data)
    assert(len(docs_2) == 20)

    # returned object has at most 3 same movies
    # titles_1 = [docs_1[i]['title'] for i in range(20)]
    # titles_2 = [docs_2[i]['title'] for i in range(20)]
    # duplicates = list(set(titles_1) & set(titles_2))
    # assert(len(duplicates) == 0)