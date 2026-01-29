
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from .pipeline import run_tryon
from .utils import device_info

app = FastAPI(title="VTON Commerce API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok", "device": device_info()}

@app.post("/tryon/image")
async def tryon_image(user_image: UploadFile = File(...), garment_image: UploadFile = File(...)):
    out_path = run_tryon(user_image, garment_image)
    return {"result": out_path}
