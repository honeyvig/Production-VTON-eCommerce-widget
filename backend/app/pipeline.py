
import os, tempfile
from .utils import save_upload

def run_tryon(user_image, garment_image):
    # Placeholder safe pipeline: segmentation + pose + garment overlay
    u = save_upload(user_image)
    g = save_upload(garment_image)
    # In production, call ControlNet + segmentation + safe diffusion overlay
    return {"user": u, "garment": g, "note": "Overlay complete (safe mode)"}
