from fastapi.testclient import TestClient

from app.main import app
from app.services.matching_service import calculate_match


client = TestClient(app)


def test_calculate_match_partial():
    employee_skills = ["Python", "SQL", "Git"]
    required_skills = ["Python", "SQL", "Git", "React"]

    result = calculate_match(employee_skills, required_skills)

    assert result["match_score"] == 75
    assert result["matched_skills"] == ["git", "python", "sql"]
    assert result["missing_skills"] == ["react"]
    assert result["training_recommendations"] == [
        "Complete introductory training in React"
    ]


def test_calculate_match_full():
    employee_skills = ["Python", "SQL", "Git"]
    required_skills = ["Python", "SQL", "Git"]

    result = calculate_match(employee_skills, required_skills)

    assert result["match_score"] == 100
    assert result["missing_skills"] == []
    assert result["training_recommendations"] == []


def test_calculate_match_zero():
    employee_skills = ["Java"]
    required_skills = ["Python", "SQL"]

    result = calculate_match(employee_skills, required_skills)

    assert result["match_score"] == 0
    assert result["matched_skills"] == []
    assert result["missing_skills"] == ["python", "sql"]


def test_calculate_match_no_required_skills():
    employee_skills = ["Python", "SQL"]
    required_skills = []

    result = calculate_match(employee_skills, required_skills)

    assert result["match_score"] == 100
    assert result["matched_skills"] == []
    assert result["missing_skills"] == []
    assert result["training_recommendations"] == []


def test_match_endpoint():
    response = client.post(
        "/match",
        json={
            "employee_skills": ["Python", "SQL", "Git"],
            "required_skills": ["Python", "SQL", "Git", "React"],
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["match_score"] == 75
    assert data["matched_skills"] == ["git", "python", "sql"]
    assert data["missing_skills"] == ["react"]
    assert data["training_recommendations"] == [
        "Complete introductory training in React"
    ]
