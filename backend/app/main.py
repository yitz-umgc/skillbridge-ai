from fastapi import FastAPI

from app.routes.matching import router as matching_router

app = FastAPI(title="SkillBridge AI")

app.include_router(matching_router)


@app.get("/")
def root():
    return {"message": "SkillBridge AI backend is running"}
