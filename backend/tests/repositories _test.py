from dataclasses import field
from xxlimited import new
from tests.test_database import SessionLocal
from api.src.repositories import RepoFields, RepoRoute, RepoIrrigation, RepoReports, RepoSensors
from api.src.models import Base, irrigation_enum, reports_enum
from tests.test_database import engine

import networkx as nx
import networkx.algorithms.approximation as nx_app
from mapping.core.networkx_grid_route import gen_grid, complete_graph, irrigation_delimiter, flip_to_start_position, christofides_tsp_custom

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def test_repo_fields():
    repo = RepoFields(SessionLocal())
    field_1 = repo.create_field(width = 15, length = 15)

    field_2 = repo.create_field(width = 10, length = 10)

    rec_fields = repo.get_fields()
    
    first_field = repo.get_field_by_id(1)

    assert field_1 == first_field and first_field == rec_fields[1] and field_2 == rec_fields[0] 

def test_repo_irrigation():
    repo = RepoIrrigation(SessionLocal())
    state_enum = repo.set_irrigation_state(irrigation_enum.START)

    assert state_enum == True and irrigation_enum.START == repo.get_current_irrigation_state()

def test_repo_route():
    repo_field = RepoFields(SessionLocal())
    repo_route = RepoRoute(SessionLocal())
    field = repo_field.get_field_by_id(1)
    G = gen_grid(field.field_width ,field.field_length, [])
    H = G.copy()
    G = complete_graph(G, H)

    route = christofides_tsp_custom(G, (0,0))
    route = {
		'irrigation_route': route
	}
    
    repo_route.create_trajectory(0, 0, route, 1)

    
    assert repo_route.get_latest_trajectory() == repo_route.get_trajectory_by_id(1)

def test_repo_reports():
    repo_report = RepoReports(SessionLocal())
    report = repo_report.create_report(battery_level=0, remaining_points=None, status_report=reports_enum.INIT_CYCLE)

    assert report == repo_report.get_reports()[0]

def test_repo_sensors():
    repo_sensors = RepoSensors(SessionLocal())

    sensors = repo_sensors.record_sensor_data(temp_air=14, temp_soil=14, humidity_air=15, humidity_soil=15)

    assert sensors == repo_sensors.get_sensors_data()[0]