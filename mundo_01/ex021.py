# Faça um programa em Python que abra e reproza o áudio de um archivo MP3.

import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.wait(1)
