import pygame
import pygame_menu
from level import *

#CLASSE PARA MOSTRAR O MENU INICIAL

class Menu:
    def __init__(self,screen,screen_width,screen_height):
        #CONFIGURAÇÕES DE TELA
        self.screen_width = screen_width
        self.screen_height =screen_height
        self.screen =screen
        self.nivel = Level(self.screen)

    def menu_inicial(self):

        #CRIA MENU PRINCIPAL
        menu = pygame_menu.Menu("Menu Principal", self.screen_width, self.screen_height, theme=pygame_menu.themes.THEME_DARK)

        #ADICIONANDO NOME DA MATÉRIA
        menu.add.label("PROJETO INTEGRADOR - COMPILADORES E GRAFOS \n")
        #ADICIONANDO NOME DA MATÉRIA
        menu.add.label("Engenharia da Computação - Modulo 4 \n")

        #ADICIONANDO NOME DO JOGO
        menu.add.label("BEEHIVE\n",font_color = "gold",font_size = 72)
        
        #FUNÇÃO PARA MOSTRAR OS INTEGRANTES
        def mostrar_integrantes():

            #MENU INTEGRANTES DO PROJETO
            menu_integrantes = pygame_menu.Menu("Integrantes", self.screen_width, self.screen_height, theme=pygame_menu.themes.THEME_DARK)

            #ADICIONA OS NOMES DOS INTEGRANTES
            menu_integrantes.add.label("Gabriel Resende")
            menu_integrantes.add.label("(Lider) Luis Antonio de Albuquerque Adamski")
            menu_integrantes.add.label("Luis Filipe Giglio Frasão")
            menu_integrantes.add.label("Matheus Henrique de Oliveira")
            menu_integrantes.add.label("Matheus Setsuo Mihara de Siqueira")
            menu_integrantes.add.label("Pedro Ludovico Rodrigues \n")

            #BOTÃO VOLTAR MENU
            menu_integrantes.add.button("Voltar", menu)

            #EXECUTA O MENU INTEGRANTES
            menu_integrantes.mainloop(self.screen)
        
        #FUNÇÃO PARA SELECIONAR FASES

        def seleciona_fase():

            #MENU INTEGRANTES DO PROJETO
            menu_selecaofase = pygame_menu.Menu("Seleção de fase", self.screen_width, self.screen_height, theme=pygame_menu.themes.THEME_DARK)

            #ADICIONA OS BOTÕES DE SELEÇÃO DE FASE
            menu_selecaofase.add.button("Fase 1", self.nivel.level_1)
            menu_selecaofase.add.button("Fase 2", self.nivel.level_2)

            #BOTÃO VOLTAR MENU
            menu_selecaofase.add.button("Voltar", menu)

            #EXECUTA O MENU INTEGRANTES
            menu_selecaofase.mainloop(self.screen)

        #ITENS CLICAVEIS DO MENU
        menu.add.button("Iniciar Jogo", seleciona_fase)
        menu.add.button("Integrantes", mostrar_integrantes)
        menu.add.button("Sair", pygame_menu.events.EXIT)


        #ADICIONANDO NOME DA MATÉRIA
        menu.add.label("\n2023")

        #EXECUTA O MENU PRINCIPAL
        menu.mainloop(self.screen)

#ENCERRANDO PYGAME
#pygame.quit()
