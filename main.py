from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.mount('/', StaticFiles(directory='web', html=True), name='static')

@app.get('/{full_path:path}')
def catch_all(full_path: str):
    return FileResponse(os.path.join('web', 'index.html'))
