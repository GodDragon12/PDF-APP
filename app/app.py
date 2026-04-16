from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import uuid, shutil

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "files" / "uploads"
ANNOTATED_DIR = BASE_DIR / "files" / "annotated"
CONVERTED_DIR = BASE_DIR / "files" / "converted"

app = FastAPI()

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    dest = UPLOAD_DIR / f"{file_id}.pdf"
    with dest.open("wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"file_id": file_id}
