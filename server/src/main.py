from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from stream_cv import getCameraStream

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"Hello": "world"}

@app.get('/video')
def video():
    return StreamingResponse(getCameraStream(), 
                            media_type="multipart/x-mixed-replace; boundary=PNPframe")