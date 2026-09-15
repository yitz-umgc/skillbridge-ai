from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_employee():
    response = client.post(
        "/employees/",
        json={
            "name": "Walter Bibbins",
            "email": "walter@example.com",
            "skills": ["Python", "FastAPI"],
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Walter Bibbins"
    assert data["email"] == "walter@example.com"
    assert "id" in data


def test_employee_required_fields():
    response = client.post(
        "/employees/",
        json={
            "email": "walter@example.com"
        },
    )

    assert response.status_code == 422


def test_create_project():
    response = client.post(
        "/projects/",
        json={
            "name": "SkillBridge AI",
            "description": "AI-powered employee skill matching platform",
            "required_skills": ["Python", "FastAPI"],
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "SkillBridge AI"
    assert "id" in data


def test_project_required_fields():
    response = client.post(
        "/projects/",
        json={
            "description": "Missing project name"
        },
    )

    assert response.status_code == 422


def test_project_required_skills_not_empty():
    response = client.post(
        "/projects/",
        json={
            "name": "SkillBridge AI",
            "description": "AI-powered employee skill matching platform",
            "required_skills": [],
        },
    )

    assert response.status_code == 422
