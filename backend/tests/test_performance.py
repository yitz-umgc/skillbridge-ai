import time

from app.services.matching_service import calculate_match


def test_matching_performance():
    employee_skills = [
        "Python", "SQL", "Git", "FastAPI", "React",
        "JavaScript", "Docker", "AWS", "PostgreSQL", "Java"
    ]

    required_skills = [
        "Python", "SQL", "Git", "React", "Docker"
    ]

    iterations = 1000

    start_time = time.perf_counter()

    for _ in range(iterations):
        calculate_match(employee_skills, required_skills)

    elapsed_time = time.perf_counter() - start_time
    average_time = elapsed_time / iterations

    print(
        f"\nPerformance benchmark: {iterations} matches in "
        f"{elapsed_time:.6f} seconds; "
        f"average {average_time:.8f} seconds per match"
    )

    # Alpha performance requirement:
    # 1,000 matching operations should complete in under 1 second.
    assert elapsed_time < 1.0
