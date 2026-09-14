from fastapi import APIRouter
from pydantic import BaseModel

from app.services.matching_service import calculate_match

router = APIRouter()


class MatchRequest(BaseModel):
    employee_skills: list[str]
    required_skills: list[str]


@router.post("/match")
def run_match(request: MatchRequest):
    return calculate_match(
        request.employee_skills,
        request.required_skills
    )
