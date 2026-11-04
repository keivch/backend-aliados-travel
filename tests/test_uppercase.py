import io
import pytest

from app import create_app


@pytest.fixture
def client():
  
    app = create_app("testing")
  
    with app.test_client() as client:
        yield client


# 1. Archivo válido
def test_count_uppercase_success(client):

    content = "Hola Mundo".encode("utf-8")

    response = client.post(
        '/api/uppercase',
        data={
            'file': (io.BytesIO(content), 'prueba.txt')
        },
        content_type='multipart/form-data'
    )

    assert response.status_code == 200
    assert response.json['count'] == 2
    assert response.json['filename'] == 'prueba.txt'


# 2. Archivo sin mayúsculas
def test_count_uppercase_zero(client):

    content = b"hola mundo python"

    response = client.post(
        '/api/uppercase',
        data={
            'file': (io.BytesIO(content), 'minusculas.txt')
        },
        content_type='multipart/form-data'
    )

    assert response.status_code == 200
    assert response.json['count'] == 0


# 3. Archivo sin adjuntar
def test_missing_file(client):

    response = client.post('/api/uppercase')

    assert response.status_code == 400
    assert 'error' in response.json


# 4. Archivo con extensión incorrecta
def test_invalid_extension(client):

    response = client.post(
        '/api/uppercase',
        data={
            'file': (io.BytesIO(b"HOLA MUNDO"), 'documento.pdf')
        },
        content_type='multipart/form-data'
    )

    assert response.status_code == 400
    assert 'error' in response.json


# 5. Archivo superior a 2 MB
def test_file_exceeds_max_size(client):

    content = b'A' * (2 * 1024 * 1024 + 1)

    response = client.post(
        '/api/uppercase',
        data={
            'file': (io.BytesIO(content), 'grande.txt')
        },
        content_type='multipart/form-data'
    )

    assert response.status_code == 400
    assert 'error' in response.json


# 6. Archivo con codificación inválida
def test_invalid_encoding(client):

    content = b'\xff\xfe\xfa'

    response = client.post(
        '/api/uppercase',
        data={
            'file': (io.BytesIO(content), 'invalido.txt')
        },
        content_type='multipart/form-data'
    )

    assert response.status_code == 400
    assert 'error' in response.json


# 7. Archivo exactamente de 2 MB
def test_file_exactly_2mb(client):

    content = b'A' * (2 * 1024 * 1024)

    response = client.post(
        '/api/uppercase',
        data={
            'file': (io.BytesIO(content), 'limite.txt')
        },
        content_type='multipart/form-data'
    )

    assert response.status_code == 200
    assert response.json['count'] == 2 * 1024 * 1024