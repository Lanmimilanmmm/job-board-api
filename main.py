from fastapi import FastAPI
from database import engine, Base
from routers import jobs, auth
import models.user

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Board API")

app.include_router(jobs.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Job Board API radi!"}