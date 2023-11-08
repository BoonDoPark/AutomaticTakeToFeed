from fastapi import FastAPI
from fastapi.responses import JSONResponse, StreamingResponse

from stream_cv import getCameraStream

app = FastAPI()

@app.get('/video')
def video():
    return JSONResponse(content={"message": getCameraStream()})
    # return StreamingResponse(getCameraStream(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/")
def root() -> dict:
    return {"Hello": 180}