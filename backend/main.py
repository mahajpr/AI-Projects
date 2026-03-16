from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import os
from crew import crew

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


class Job(BaseModel):
    query: str


@app.post("/upload-resume")
def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return {
        "message": "Resume uploaded successfully",
        "file_name": file.filename
    }


@app.post("/match-resume-agent")
def match_resume_agent(file_name: str, req: Job):

    resume_path = os.path.join(UPLOAD_DIR, file_name)

    if not os.path.exists(resume_path):
        return {"error": "Resume not found"}

    result = crew.kickoff(inputs={
        "resume_path": resume_path,
        "job_desc": req.query
    })

    return {"result": result}



