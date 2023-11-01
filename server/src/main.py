from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from stream_cv import getCameraStream

app = FastAPI()

@app.get("/")
def root() -> dict:
    return {"Hello": "world"}

@app.get('/video')
def video():
    return StreamingResponse(getCameraStream(),
                            media_type="multipart/x-mixed-replace; boundary=frame")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)