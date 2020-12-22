from elasticapm.contrib.starlette import ElasticAPM, make_apm_client
from fastapi import FastAPI, Request

from app.elastic_config import elastic_config


apm = make_apm_client(elastic_config)
app = FastAPI()
app.add_middleware(ElasticAPM, client=apm)


@app.get("/")
async def index(request: Request):
    client_host = request.client.host
    return {"client_host": client_host}


@app.get("/elastic-apm")
async def elastic_apm_error():
    try:
        1 / 0
    except ZeroDivisionError:
        apm.capture_exception()
