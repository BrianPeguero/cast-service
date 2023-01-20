from fastapi import FastAPI
from app.apis.cast import casts

app=FastAPI(openapi_url="/api/v1/casts/openapi.json", docs_url="/api/v1/casts/docs")

app.include_router(casts, prefix='/api/v1/casts', tags=['Casts'])