from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from api.src.routers import sensors, trajectory, bot, reports, fields
from api.src.models import Base
from api.src.database import engine

Base.metadata.create_all(bind=engine)

origins = ["*"]

middleware = [
	Middleware(
		CORSMiddleware,
		allow_origins=origins,
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
		expose_headers=["*"],
	)
]

app = FastAPI(debug=True, middleware=middleware)

app.include_router(sensors.router)
app.include_router(trajectory.router)
app.include_router(bot.router)
app.include_router(reports.router)
app.include_router(fields.router)

@app.get("/")
def root():
	return {"message": "See API documentation at: /docs"}
