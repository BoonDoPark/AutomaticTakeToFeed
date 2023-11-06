from fastapi import FastAPI
from fastapi.responses import JSONResponse, StreamingResponse
from classify_image import image_classifiaction

from stream_cv import getCameraStream, load_image

app = FastAPI()

@app.get('/video')
def video():
    return JSONResponse(content={"messege": getCameraStream()})
    # return StreamingResponse(getCameraStream(), media_type="multipart/x-mixed-replace; boundary=frame")

@app.get("/")
def root() -> dict:
    return {"Hello": "world"}