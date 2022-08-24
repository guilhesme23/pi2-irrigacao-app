from fastapi import FastAPI
from api.src.routers import sensors, trajectory, bot, reports
from api.src.models import Base
from api.src.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

app.include_router(sensors.router)
app.include_router(trajectory.router)
app.include_router(bot.router)
app.include_router(reports.router)

@app.get("/")
def root():
	return {"message": "See API documentation at: /docs"}
