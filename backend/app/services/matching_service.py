def calculate_match(employee_skills, required_skills):
    """Compare employee skills with project requirements."""

    employee = {skill.lower() for skill in employee_skills}
    required = {skill.lower() for skill in required_skills}

    if not required:
        return {
            "match_score": 100,
            "matched_skills": [],
            "missing_skills": [],
        }

    matched = required.intersection(employee)
    missing = required.difference(employee)

    match_score = round((len(matched) / len(required)) * 100)

    return {
        "match_score": match_score,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
    }
