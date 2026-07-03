#!/usr/bin/python
# -*- coding: utf-8 -*-
from asyncio import Event

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import *

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuBg.png").convert_alpha() # carregando imagem
        self.rect = self.surf.get_rect(left=0, top=0) # criando retangulo

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3') # Definindo arquivo de musica
        pygame.mixer_music.play(-1) # Tocando musica indefinidamente

        while True:
            pygame.display.flip()  # atualizando imagem no retangulo
            self.window.blit(source=self.surf, dest=self.rect) # desenhando imagem no retangulo
            self.menu_text(50, "Mountain", C_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", C_ORANGE, ((WIN_WIDTH / 2), 120))

            # Guia comandos jogadores
            self.menu_text(14, "Comandos - Player 1", C_ORANGE, (80, 10))
            self.menu_text(10, "Cima - seta para cima", C_GREY, (65, 30))
            self.menu_text(10, "Baixo - seta para baixo", C_GREY, (70, 40))
            self.menu_text(10, "Esquerda - seta para esquerda", C_GREY, (87, 50))
            self.menu_text(10, "Direita - seta para direita", C_GREY, (80, 60))
            self.menu_text(10, "Atirar - Espaço", C_GREY, (45, 70))

            self.menu_text(14, "Comandos - Player 2", C_ORANGE, (80, 100))
            self.menu_text(10, "Cima - w", C_GREY, (25, 120))
            self.menu_text(10, "Baixo - s", C_GREY, (27, 130))
            self.menu_text(10, "Esquerda - a", C_GREY, (35, 140))
            self.menu_text(10, "Direita - d", C_GREY, (35, 150))
            self.menu_text(10, "Atirar - CTRL", C_GREY, (40, 160))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # tecla para baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP: # tecla para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)