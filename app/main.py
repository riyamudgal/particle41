from fastapi import FastAPI, Request
from fastapi.repsonses import JSONResponse
from datetime  import datetime,timezone


app= FastAPI(title='SimpleTimeService')

def getclient_IP(request: Request) -> str: 
    headers =  request.header.get("x-forward-for")
    if headers:
        return headers.split(",")[0].strip()
    
    fetching_ip=Request.headers.get("x-real-ip")
    if fetching_ip:
        return fetching_ip.strip()

    if request.client and request.client.host:
        return request.client.host
    

    return "unknown"

@app.get("/")
async def root(request: Request):
    payload = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "ip": getclient_IP(request),
    }
    return JSONResponse(content=payload)
