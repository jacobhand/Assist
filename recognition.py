import speech_recognition as sr

# Initialisiere den Recognizer
recognizer = sr.Recognizer()

# Funktion, die das Mikrofon abhört und auf das Schlüsselwort reagiert
def listen_for_keyword(keyword):
    with sr.Microphone() as source:
        print("Bitte sprechen Sie...")
        while True:
            try:
                # Audio vom Mikrofon aufnehmen
                audio = recognizer.listen(source)

                # Sprache in Text umwandeln
                text = recognizer.recognize_google(audio, language="de-DE")
                print(f"Gesagt: {text}")

                # Überprüfen, ob das Schlüsselwort gesagt wurde
                if keyword.lower() in text.lower():
                    print("Schlüsselwort erkannt!")
                    return True  # Schlüsselwort erkannt, Funktion beendet sich

            except sr.UnknownValueError:
                print("Sprachunverständlichkeit. Bitte erneut versuchen.")
            except sr.RequestError as e:
                print(f"Konnte den Sprachdienst nicht erreichen; {e}")
                return False  # Bei Fehler Funktion beenden und False zurückgeben

    return False  # Falls die Schleife ohne Erkennung endet, gibt False zurück
