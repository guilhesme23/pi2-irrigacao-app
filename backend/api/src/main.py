from fastapi import FastAPI
from routers import sensors, trajectory

app = FastAPI()

app.include_router(sensors.router)
app.include_router(trajectory.router)

@app.get("/")
def root():
	return {"message": "Running"}
