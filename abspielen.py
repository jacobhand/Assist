import pygame

def play_mp3(file_path):
    """
    Spielt eine MP3-Datei ab.

    :param file_path: Pfad zur MP3-Datei
    """
    # Pygame initialisieren
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Warten, bis die Musik zu Ende ist
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


