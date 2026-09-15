from fastapi import FastAPI

from app.routes.matching import router as matching_router
from .employees import router as employees_router
from .projects import router as projects_router


app = FastAPI(title="SkillBridge AI")

app.include_router(employees_router)
app.include_router(projects_router)
app.include_router(matching_router)


@app.get("/")
def root():
    return {"message": "SkillBridge AI backend is running"}