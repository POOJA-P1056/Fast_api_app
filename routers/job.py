from fastapi import APIRouter 
from schemas.job import JobCreate, JobUpdate
router = APIRouter(prefix="/job",tags=["job"])

# @router.get("/")
# def read_job():
#     return {"Job":"Job root"}

# @router.get("/{job_id}")
# def read_job(job_id:int):
#     return {"job_id": job_id} 


jobs = [] 

@router.post("/")
def JobCreate(job: JobCreate):
    jobs.append(job)
    return jobs

@router.get("/")
def get_all_job():
    return jobs

@router.get("/{job_id}")
def get_job_by_id(job_id: int,):
    return jobs[job_id]


@router.put("/{job_id}")
def update_jobs(job_id: int, job_update: JobUpdate):
    jobs[job_id] = job_update
    return jobs

@router.delete("/{job_id}")
def delete_company(job_id: int):
    jobs.pop(job_id)
    return jobs