

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from utils.transcribe import transcribe_audio
from utils.chat import get_llm_response
from utils.synthesize import synthesize_speech
from utils.storage import save_temp_audio_and_get_url
import tempfile
from langchain_openai import ChatOpenAI 
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# Serve static files (audio & frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/ivr-handler")
async def handle_audio(audio: UploadFile = File(...)):
    # Save uploaded audio to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp:
        tmp.write(await audio.read())
        audio_path = tmp.name

    # Transcribe audio to text using Whisper
    text = transcribe_audio(audio_path)

    # Generate reply text using GPT-4
    response_text= get_llm_response(text)


    # Convert reply text to speech (mp3 bytes)
    synthesize_speech(response_text)

 
    return FileResponse(
        path='/Users/vipanshijain/Desktop/ivr',
        media_type="audio/mpeg",
        filename="audio.mp3"
    )