from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Welcome to My Flask Application!" in response.data


def test_about():
    client = app.test_client()

    response = client.get("/about")

    assert response.status_code == 200
    assert b"This is a Python Flask application using GitHub Actions." in response.data


def test_contact():
    client = app.test_client()

    response = client.get("/contact")

    assert response.status_code == 200
    assert b"Contact page of my Flask application." in response.data