from elasticapm.contrib.starlette import ElasticAPM, make_apm_client
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder

from app.elastic_config import elastic_config


apm = make_apm_client(elastic_config)
app = FastAPI()
app.add_middleware(ElasticAPM, client=apm)


@app.get("/")  # a normal GET route
async def index(request: Request):
    client_host = request.client.host
    return {"client_host": client_host}


@app.get("/elastic-apm")  # a GET route with a manually caught exception, sent to Elastic APM
async def elastic_apm_error():
    try:
        1 / 0
    except ZeroDivisionError:
        apm.capture_exception()


@app.get("/5xx")  # a GET route that causes a 500 response code that is automatically sent to Elastic APM
async def fail_with_5xx():
    value = "a" + 1
    return jsonable_encoder({"message": value})
