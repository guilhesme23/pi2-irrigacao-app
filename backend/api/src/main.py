from fastapi import FastAPI
from routers import sensors

app = FastAPI()

app.include_router(sensors.router)

@app.get("/")
def root():
	return {"message": "Running"}
