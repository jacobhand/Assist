import os
from recognition import listen_for_keyword
from aufnehmen import record_audio_to_mp3
from transcription import transcribe_audio
from assistant import interact_with_assistant
from voice import voice
from abspielen import play_mp3



def conversation():
    mp3_filename = "aufnahme.mp3"
    record_seconds = 8

    record_audio_to_mp3(mp3_filename, record_seconds)

    audio_file_path = mp3_filename

    api_key=os.getenv("api_key")

    transcribed_text = transcribe_audio(api_key, audio_file_path)
    print(transcribed_text)

    model = "gpt-4o"
    assistant_id = "asst_GL4PRW37IinkSpURtiLosXEV"
    thread_id = "thread_ji1519WDgne5Xi97vjpGxXn8"
    user_message = transcribed_text

    response = interact_with_assistant(api_key, model, assistant_id, thread_id, user_message)
    voice(response, api_key)

    # Beispielaufruf
    play_mp3('speech.mp3')

    os.remove("aufnahme.mp3")
    os.remove("speech.mp3")

# Schlüsselwort festlegen
keyword = "Hey Siri"

# Überprüfen, ob das Schlüsselwort erkannt wurde, und conversation() ausführen
while True:
    if listen_for_keyword(keyword):
        conversation()

