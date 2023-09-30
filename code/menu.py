import pygame
import pygame_menu
from config import screen_width,screen_height
from level import *

#INICIALIZADOR PYGAME
pygame.init()

#CONFIGURAÇÕES DE TELA
largura = screen_width
altura = screen_height
tela = pygame.display.set_mode((largura, altura))
nivel = Level(tela)


#FUNÇÃO PARA MOSTRAR O MENU INICIAL
def menu_inicial():
    
    #CRIA MENU PRINCIPAL
    menu = pygame_menu.Menu("Menu Principal", largura, altura, theme=pygame_menu.themes.THEME_DARK)

    #ADICIONANDO NOME DA MATÉRIA
    menu.add.label("PROJETO INTEGRADOR - COMPILADORES E GRAFOS \n")
    #ADICIONANDO NOME DA MATÉRIA
    menu.add.label("Engenharia da Computação - Modulo 4 \n")

    #ADICIONANDO NOME DO JOGO
    menu.add.label("BEEHIVE\n",font_color = "gold",font_size = 72)
    
    #FUNÇÃO INICIAR JOGO
    def iniciar_jogo():
            pass

    #FUNÇÃO PARA MOSTRAR OS INTEGRANTES
    def mostrar_integrantes():

        #ADICIONA OS NOMES DOS INTEGRANTES
        menu_integrantes.add.label("Gabriel Resende")
        menu_integrantes.add.label("(Lider) Luis Antonio de Albuquerque Adamski")
        menu_integrantes.add.label("Luis Filipe Giglio Frasão")
        menu_integrantes.add.label("Matheus Henrique de Oliveira")
        menu_integrantes.add.label("Matheus Setsuo Mihara de Siqueira")
        menu_integrantes.add.label("Pedro Ludovico Rodrigues \n")

        #BOTÃO VOLTAR MENU
        menu_integrantes.add.button("Voltar", menu_inicial)

        #EXECUTA O MENU INTEGRANTES
        menu_integrantes.mainloop(tela)
    
    #FUNÇÃO PARA SELECIONAR FASES

    def seleciona_fase():

        #MENU INTEGRANTES DO PROJETO
        menu_selecaofase = pygame_menu.Menu("Seleção de fase", largura, altura, theme=pygame_menu.themes.THEME_DARK)

        #ADICIONA OS BOTÕES DE SELEÇÃO DE FASE
        menu_selecaofase.add.button("Fase 1", nivel.level_1)
        menu_selecaofase.add.button("Fase 2", nivel.level_2)

        #BOTÃO VOLTAR MENU
        menu_selecaofase.add.button("Voltar", menu_inicial)

        #EXECUTA O MENU INTEGRANTES
        menu_selecaofase.mainloop(tela)

    #ITENS CLICAVEIS DO MENU
    menu.add.button("Iniciar Jogo", seleciona_fase)
    menu.add.button("Integrantes", mostrar_integrantes)
    menu.add.button("Sair", pygame_menu.events.EXIT)


    #ADICIONANDO NOME DA MATÉRIA
    menu.add.label("\n2023")

    #EXECUTA O MENU PRINCIPAL
    menu.mainloop(tela)

#ENCERRANDO PYGAME
#pygame.quit()
