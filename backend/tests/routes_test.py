from api.src.models import Base
from tests.test_database import engine, override_get_db
from api.src.database import get_db
from fastapi import FastAPI
from fastapi.testclient import TestClient
from api.src.routers import bot, fields, reports, sensors, trajectory, waterbalance  
from mapping.core.networkx_grid_route import gen_grid, christofides_tsp_custom

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

app.include_router(bot.router)
app.include_router(fields.router)
app.include_router(reports.router)
app.include_router(sensors.router)
app.include_router(trajectory.router)
app.include_router(waterbalance.router)

@app.get("/")
def root():
	return {"message": "See API documentation at: /docs"}

client = TestClient(app)

app.dependency_overrides[get_db] = override_get_db

def test_bot():
    response = client.post("/commands/irrigate", json={'irrigate': True})
    assert response.status_code == 200
    assert response.json() == {'message': 'Start irrigation'}

    response = client.get("/commands/irrigate")
    assert response.status_code == 200
    assert response.json() == {'message': 'Start irrigation', 'data': True} 

    response = client.post("/commands/irrigate", json={'irrigate': False})
    assert response.status_code == 200
    assert response.json() == {'message': 'Stop irrigation'}

    response = client.get("/commands/irrigate")
    assert response.status_code == 200
    assert response.json() == {'message': 'Stop irrigation', 'data': False} 

    response = client.post("/commands/irrigate", json={'irrigat': False})
    assert response.status_code == 422

def test_fields():
    response = client.post("/fields", json = {"width": 30, "length": 30})
    assert response.status_code == 200
    assert response.json() == {"id": 3, "field_width": 30, "field_length": 30}

    response = client.get("/fields")
    assert response.status_code == 200
    assert response.json()[0] == {"id": 3, "field_width": 30, "field_length": 30}

    response = client.get("/fields/3")
    assert response.status_code == 200
    assert response.json() == {"id": 3, "field_width": 30, "field_length": 30}

    response = client.post("/fields", json = {})
    assert response.status_code == 422

    response = client.get("/fields/4")
    assert response.status_code == 404

def test_reports():
    response = client.post("/reports", json = {
                                "battery_level": 0,
                                "remaining_points": {},
                                "status_report": "INIT_CYCLE"
                                })

    assert response.status_code == 200
    assert response.json()['battery_level'] == 0
    assert response.json()['remaining_points'] == {}
    assert response.json()['status_report'] == "INIT_CYCLE"

    response = client.post("/reports", json = {
                                "battry_level": 0,
                                "remaining_points": {},
                                "status_report": "INIT_CYCLE"
                                })                        
    assert response.status_code == 422

def test_sensors():
    response = client.post("/sensors", json = {
                                    "temp_air": 10,
                                    "temp_soil": 11,
                                    "humidity_air": 12,
                                    "humidity_soil": 13
                                    })
    assert response.status_code == 200
    assert response.json()['temp_air'] == 10
    assert response.json()['temp_soil'] == 11
    assert response.json()['humidity_air'] == 12
    assert response.json()['humidity_soil'] == 13

    response = client.get("/sensors")
    assert response.status_code == 200
    assert response.json()[0]['temp_air'] == 10
    assert response.json()[0]['temp_soil'] == 11
    assert response.json()[0]['humidity_air'] == 12
    assert response.json()[0]['humidity_soil'] == 13

    response = client.post("/sensors", json = {})
    assert response.status_code == 422

def test_trajectory():
    response = client.post("/trajectory/", json = {
                                    "field_id": 3,
                                    "base_pos_x": 0,
                                    "base_pos_y": 0,
                                    "nodes_to_delete": []
                                    })
    field_response = client.get("/fields/3")
    G = gen_grid(field_response.json()['field_width'], \
        field_response.json()['field_length'], [])
    route = christofides_tsp_custom(G, (0, 0))

    assert response.status_code == 200
    assert response.json()['irrigation_route'] == {'irrigation_route': [list(x) for x in route]}
    
    response = client.get("/trajectory/")
    assert response.status_code == 200
    assert response.json()['route']['irrigation_route'] == {'irrigation_route': [list(x) for x in route]}
    
    response = client.get("/trajectory/2")
    assert response.status_code == 200
    assert response.json()['route']['irrigation_route'] == {'irrigation_route': [list(x) for x in route]}

def test_waterbalance():
    response = client.get("/waterbalance")
    assert response.status_code == 200
