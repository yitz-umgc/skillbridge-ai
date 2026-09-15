from pydantic import BaseModel


class Employee(BaseModel):
    id: int
    name: str
    email: str
    skills: list[str] = []


class Project(BaseModel):
    id: int
    name: str
    description: str
    required_skills: list[str] = []
