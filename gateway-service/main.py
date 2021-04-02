from fastapi import FastAPI, Response, Request
import httpx

from services import services


app = FastAPI()


@app.get("/{service_name}")
async def get_service(service_name: str, response: Response, request: Request):
    if service_name in services:
        service = services.get(service_name)
        url = service.get('url')
        port = service.get("port", 80)
        async with httpx.AsyncClient() as client:
            r = await client.get(
                f"http://{url}:{port}/",
                headers=dict(request.headers),
                params=request.query_params
            )
            return r
    return "Unknown Service"

