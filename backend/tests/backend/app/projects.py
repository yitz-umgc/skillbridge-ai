from fastapi import APIRouter, HTTPException

from .schemas import ProjectCreate, ProjectResponse


router = APIRouter(
    prefix="/projects",
    tags=["projects"],
)

projects: list[dict] = []


@router.post("/", response_model=ProjectResponse, status_code=201)
def create_project(project: ProjectCreate):
    new_project = {
        "id": len(projects) + 1,
        **project.model_dump(),
    }

    projects.append(new_project)
    return new_project


@router.get("/", response_model=list[ProjectResponse])
def get_projects():
    return projects


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int):
    for project in projects:
        if project["id"] == project_id:
            return project

    raise HTTPException(
        status_code=404,
        detail="Project not found",
    )
