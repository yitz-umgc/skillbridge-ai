from pydantic import BaseModel, Field


class EmployeeCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)
    skills: list[str] = []


class EmployeeResponse(EmployeeCreate):
    id: int


class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    required_skills: list[str] = []


class ProjectResponse(ProjectCreate):
    id: int
