from openai import OpenAI

def transcribe_audio(api_key, audio_file_path):
    # Initialisiere den OpenAI-Client
    client = OpenAI(api_key=api_key)
    
    # Öffne die Audiodatei
    with open(audio_file_path, "rb") as audio_file:
        # Erstelle die Transkription
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    
    # Gebe den transkribierten Text zurück
    return transcription.text

