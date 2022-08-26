from fastapi import Body, APIRouter
from requests import post
import datetime as dt

router = APIRouter()


@router.get("/waterbalance", tags=["WaterBalance"])
def get_waterbalance_data(dataInicial: dt.datetime, dataFinal: dt.datetime, estacaoId="4792115781159100001", soloId=57):
    data = {"dataInicial": dataInicial.strftime("%d/%m/%Y"),
            "dataFinal": dataFinal.strftime("%d/%m/%Y"),
            "estacaoId": estacaoId,
            "soloId": soloId}
    data = post("http://sisdagro.inmet.gov.br/sisdagro/app/monitoramento/bhs.json", params=data)
    return data.json()['bhs']
