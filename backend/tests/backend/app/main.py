from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "SkillBridge AI backend is running"}
