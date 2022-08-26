from fastapi import Body, APIRouter
from requests import post
import datetime as dt

router = APIRouter()


@router.get("/waterbalance", tags=["WaterBalance"])
def get_waterbalance_data():
    end_date = dt.datetime.today()
    start_date = end_date - dt.timedelta(days=30)

    end_date = end_date.strftime("%d/%m/%Y")
    start_date = start_date.strftime("%d/%m/%Y")
    station_id = '4792115781159100001'
    soil_id = 57
    data = {"dataInicial": start_date,
            "dataFinal": end_date,
            "estacaoId": station_id,
            "soloId": soil_id}
    data = post("http://sisdagro.inmet.gov.br/sisdagro/app/monitoramento/bhs.json", params=data)
    return data.json()['bhs']
