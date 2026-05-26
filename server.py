import os
import uuid
import subprocess
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse

app = FastAPI()

UPLOAD_DIR = 'uploads'
OUTPUT_DIR = 'outputs'
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.post('/api/swap')
async def swap(face: UploadFile = File(...), video: UploadFile = File(...)):
    uid = str(uuid.uuid4())

    face_path = os.path.join(UPLOAD_DIR, f'{uid}_face.jpg')
    video_path = os.path.join(UPLOAD_DIR, f'{uid}_video.mp4')
    output_path = os.path.join(OUTPUT_DIR, f'{uid}_result.mp4')

    with open(face_path, 'wb') as f:
        f.write(await face.read())

    with open(video_path, 'wb') as f:
        f.write(await video.read())

    cmd = [
        'python', 'facefusion.py',
        '--source', face_path,
        '--target', video_path,
        '--output', output_path
    ]

    subprocess.run(cmd, check=True)

    return FileResponse(output_path, media_type='video/mp4')

# Run:
# uvicorn server:app --host 0.0.0.0 --port 8000
