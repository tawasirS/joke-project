import keyboard
import pygame

pygame.init()
pygame.mixer.music.load("keyboard_sound_1.mp3")

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        print(f'You Pressed the Key: {event.name}')
        pygame.mixer.music.play()

