
import torch, tempfile, shutil, os

def device_info():
    return "cuda" if torch.cuda.is_available() else "cpu"

def save_upload(f):
    fd, path = tempfile.mkstemp(suffix=os.path.splitext(f.filename)[-1])
    with os.fdopen(fd, 'wb') as out:
        shutil.copyfileobj(f.file, out)
    return path
