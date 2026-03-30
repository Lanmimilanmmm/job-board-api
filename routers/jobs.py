from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from models.job import Job
from schemas.job import JobCreate, JobResponse
from typing import List, Optional
from routers.dependencies import get_current_user
from models.user import User

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/", response_model=List[JobResponse])
def get_jobs(
    tech: Optional[str] = Query(None, description="Filtriraj po tech stacku"),
    location: Optional[str] = Query(None, description="Filtriraj po lokaciji"),
    db: Session = Depends(get_db)
):
    query = db.query(Job)
    if tech:
        query = query.filter(Job.tech_stack.ilike(f"%{tech}%"))
    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))
    return query.all()

@router.post("/", response_model=JobResponse)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_job = Job(**job.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

@router.get("/", response_model=List[JobResponse])
def get_jobs(
    tech: Optional[str] = Query(None, description="Filtriraj po tech stacku"),
    location: Optional[str] = Query(None, description="Filtriraj po lokaciji"),
    page: int = Query(1, ge=1, description="Broj stranice"),
    limit: int = Query(10, ge=1, le=100, description="Broj oglasa po stranici"),
    db: Session = Depends(get_db)
):
    query = db.query(Job)
    if tech:
        query = query.filter(Job.tech_stack.ilike(f"%{tech}%"))
    if location:
        query = query.filter(Job.location.ilike(f"%{location}%"))
    
    offset = (page - 1) * limit
    jobs = query.offset(offset).limit(limit).all()
    return jobs

@router.put("/{job_id}", response_model=JobResponse)
def update_job(job_id: int, updated: JobCreate, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Oglas nije pronađen")
    for key, value in updated.dict().items():
        setattr(job, key, value)
    db.commit()
    db.refresh(job)
    return job

@router.delete("/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Oglas nije pronađen")
    db.delete(job)
    db.commit()
    return {"message": "Oglas obrisan"}