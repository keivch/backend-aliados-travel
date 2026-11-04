import pytest

from app import create_app


@pytest.fixture
def client():

    app = create_app("testing")
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


# 1. Lista desordenada
def test_sort_unsorted_numbers(client):

    response = client.post('/api/sort', json={
        "numbers": [4, 6, 2, 7]
    })

    assert response.status_code == 200
    assert response.json['sorted: '] == [2, 4, 6, 7]


# 2. Lista ya ordenada
def test_sort_already_sorted(client):

    response = client.post('/api/sort', json={
        "numbers": [1, 2, 3, 4, 5]
    })

    assert response.status_code == 200
    assert response.json['sorted: '] == [1, 2, 3, 4, 5]


# 3. Lista en orden inverso
def test_sort_reverse_numbers(client):

    response = client.post('/api/sort', json={
        "numbers": [5, 4, 3, 2, 1]
    })

    assert response.status_code == 200
    assert response.json['sorted: '] == [1, 2, 3, 4, 5]


# 4. Números negativos
def test_sort_negative_numbers(client):

    response = client.post('/api/sort', json={
        "numbers": [-5, 3, -1, 0]
    })

    assert response.status_code == 200
    assert response.json['sorted: '] == [-5, -1, 0, 3]


# 5. Números repetidos
def test_sort_repeated_numbers(client):

    response = client.post('/api/sort', json={
        "numbers": [4, 2, 4, 1, 2]
    })

    assert response.status_code == 200
    assert response.json['sorted: '] == [1, 2, 2, 4, 4]


# 6. Un solo elemento
def test_sort_single_number(client):

    response = client.post('/api/sort', json={
        "numbers": [8]
    })

    assert response.status_code == 200
    assert response.json['sorted: '] == [8]


# 7. Lista vacía
def test_sort_empty_list(client):

    response = client.post('/api/sort', json={
        "numbers": []
    })

    assert response.status_code == 200


# 8. Valores no numéricos
def test_sort_invalid_values(client):

    response = client.post('/api/sort', json={
        "numbers": [1, "hola", 3]
    })

    assert response.status_code == 400


# 9. Sin propiedad numbers
def test_sort_missing_numbers(client):

    response = client.post('/api/sort', json={})

    assert response.status_code == 400


# 10. JSON inválido
def test_sort_invalid_json(client):

    response = client.post(
        '/api/sort',
        data='esto no es json',
        content_type='application/json'
    )

    assert response.status_code == 400