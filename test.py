import pytest
from app import User, app

@pytest.fixture
def url():
    url = 'http://127.0.0.1:3000'
    return url

# 初始化
@pytest.fixture
def client():
    client = app.test_client()
    return client

# 使用app已建置的User創建一個新的table
@pytest.fixture
def mock_model():
    mock_model = User(
        name='test',
        username='test',
        password='test'
    )
    return mock_model

# 測試table的值
def test_sqlalchemy_model(mock_model):
    my_mock_model = mock_model
    assert my_mock_model.name == 'test'
    assert my_mock_model.username == 'test'
    assert my_mock_model.password == 'test'

def test_index(url, client):
    res = client.get(url + '/')
    assert res.status_code == 200

def test_signup(url, client):
    data = {
        'name': 'test',
        'username': 'test',
        'password': 'test'
    }
    res = client.post(url + '/signup', data=data)
    assert res.status_code == 302

def test_signin(url, client):
    data = {
        'username': 'test',
        'password': 'test'
    }
    res = client.post(url + '/signin', data=data)
    assert res.status_code == 302

def test_signout(url, client):
    res = client.get(url + '/signout')
    assert res.status_code == 302

def test_member(url, client):
    res = client.get(url + '/member/')
    assert res.status_code == 302

def test_error(url, client):
    res = client.get(url + '/error/')
    assert res.status_code == 200

