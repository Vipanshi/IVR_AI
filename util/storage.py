import os
import uuid

os.makedirs("static", exist_ok=True)

def save_temp_audio_and_get_url(audio_bytes: bytes) -> str:
    filename = f"response_{uuid.uuid4().hex}.mp3"
    filepath = os.path.join("static", filename)
    with open(filepath, "wb") as f:
        f.write(audio_bytes)
    return f"/static/{filename}"