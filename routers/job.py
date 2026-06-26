from fastapi import APIRouter 

router = APIRouter(prefix="/job",tags=["job"])

@router.get("/")
def read_job():
    return {"Job":"Job root"}

@router.get("/{job_id}")
def read_job(job_id:int):
    return {"job_id": job_id}