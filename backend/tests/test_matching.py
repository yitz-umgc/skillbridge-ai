from app.services.matching_service import calculate_match


def test_calculate_match():
    employee_skills = ["Python", "SQL", "Git"]
    required_skills = ["Python", "SQL", "Git", "React"]

    result = calculate_match(employee_skills, required_skills)

    assert result["match_score"] == 75
    assert result["matched_skills"] == ["git", "python", "sql"]
    assert result["missing_skills"] == ["react"]
