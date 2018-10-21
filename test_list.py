from sys import exit
import os
import pygame
from pygame.locals import *
os.system("cls")
import time

chess_field = pygame.image.load("Schachbrett_Nummerierung_1.png")
icon = pygame.image.load("Icon.png")
white_king = pygame.image.load("white_king.png")
white_queen = pygame.image.load("white_queen.png")
white_rook = pygame.image.load("white_rook.png")
white_bishop = pygame.image.load("white_bishop.png")
white_pawn = pygame.image.load("white_pawn.png")
white_knight = pygame.image.load("white_knight.png")

black_king = pygame.image.load("black_king.png")
black_queen = pygame.image.load("black_queen.png")
black_rook = pygame.image.load("black_rook.png")
black_bishop = pygame.image.load("black_bishop.png")
black_pawn = pygame.image.load("black_pawn.png")
black_knight = pygame.image.load("black_knight.png")

pawn_tausch = pygame.image.load("pawn_tausch_1.png")
pt_button_schatten = pygame.image.load("button_pawn_tausch_schatten.png")
pt_button = pygame.image.load("button_pawn_tausch.png")

def main():
    pygame.init()
    display = pygame.display.set_mode((1400, 800), HWSURFACE | DOUBLEBUF | RESIZABLE)
    pygame.display.set_caption("Schach")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)

    clock = pygame.time.Clock()

    display.fill((0, 0, 0))
    display.blit(pygame.transform.scale(chess_field, (800, 800)), (0, 0))
    display.blit(pygame.transform.scale(pawn_tausch, (500, 200)), (500, 200))

    white_queen_pr = False
    white_rook_pr = False
    white_bishop_pr = False
    white_knight_pr = False

    pt_button_pressed = False

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                exit()

            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE:
                     pygame.event.post(pygame.event.Event(pygame.QUIT))
            elif event.type == VIDEORESIZE:
                display = pygame.display.set_mode(event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                display.blit(pygame.transform.scale(chess_field, (800, 800)), (0, 0))
                display.blit(pygame.transform.scale(pawn_tausch, (500, 200)), (150, 300))
                display.blit(pygame.transform.scale(white_queen, (100, 100)), (170, 350))
                display.blit(pygame.transform.scale(white_rook, (100, 100)), (290, 350))
                display.blit(pygame.transform.scale(white_bishop, (100, 100)), (410, 350))
                display.blit(pygame.transform.scale(white_knight, (100, 100)), (530, 350))
                display.blit(pygame.transform.scale(pt_button_schatten, (180, 30)), (310, 460))
                display.blit(pygame.transform.scale(pt_button, (180, 30)), (305, 455))

                size_x = 100
                size_y = 100

            if pygame.mouse.get_pressed()[0] == True and pygame.mouse.get_pos()[0] in range(170, 270) and pygame.mouse.get_pos()[1] in range(350, 450) and white_queen_pr == False:
                display.blit(pygame.transform.scale(white_queen, (120, 120)), (160, 340))
                white_queen_pr = True
                print("Queen")
            elif pygame.mouse.get_pressed()[0] == True and pygame.mouse.get_pos()[0] in range(290, 390) and pygame.mouse.get_pos()[1] in range(350, 450):
                display.blit(pygame.transform.scale(white_rook, (120, 120)), (280, 340))
                white_rook_pr = True
                print("Rook")
            elif pygame.mouse.get_pressed()[0] == True and pygame.mouse.get_pos()[0] in range(410, 510) and pygame.mouse.get_pos()[1] in range(350, 450):
                display.blit(pygame.transform.scale(white_bishop, (120, 120)), (400, 340))
                white_bishop_pr = True
                print("Bishop")
            elif pygame.mouse.get_pressed()[0] == True and pygame.mouse.get_pos()[0] in range(530, 630) and pygame.mouse.get_pos()[1] in range(350, 450):
                display.blit(pygame.transform.scale(white_knight, (120, 120)), (520, 340))
                white_knight_pr = True
                print("Knight")
            if pygame.mouse.get_pressed()[0] == False and white_queen_pr == True:
                display.blit(pygame.transform.scale(chess_field, (800, 800)), (0, 0))
                display.blit(pygame.transform.scale(pawn_tausch, (500, 200)), (150, 300))
                display.blit(pygame.transform.scale(white_queen, (120, 120)), (160, 340))
                display.blit(pygame.transform.scale(white_rook, (100, 100)), (290, 350))
                display.blit(pygame.transform.scale(white_bishop, (100, 100)), (410, 350))
                display.blit(pygame.transform.scale(white_knight, (100, 100)), (530, 350))
                display.blit(pygame.transform.scale(pt_button_schatten, (180, 30)), (310, 460))
                display.blit(pygame.transform.scale(pt_button, (180, 30)), (305, 455))
                white_queen_pr = False
            elif pygame.mouse.get_pressed()[0] == False and white_rook_pr == True:
                display.blit(pygame.transform.scale(chess_field, (800, 800)), (0, 0))
                display.blit(pygame.transform.scale(pawn_tausch, (500, 200)), (150, 300))
                display.blit(pygame.transform.scale(white_queen, (100, 100)), (170, 350))
                display.blit(pygame.transform.scale(white_rook, (120, 120)), (280, 340))
                display.blit(pygame.transform.scale(white_bishop, (100, 100)), (410, 350))
                display.blit(pygame.transform.scale(white_knight, (100, 100)), (530, 350))
                display.blit(pygame.transform.scale(pt_button_schatten, (180, 30)), (310, 460))
                display.blit(pygame.transform.scale(pt_button, (180, 30)), (305, 455))
                white_rook_pr = False
            elif pygame.mouse.get_pressed()[0] == False and white_bishop_pr == True:
                display.blit(pygame.transform.scale(chess_field, (800, 800)), (0, 0))
                display.blit(pygame.transform.scale(pawn_tausch, (500, 200)), (150, 300))
                display.blit(pygame.transform.scale(white_queen, (100, 100)), (170, 350))
                display.blit(pygame.transform.scale(white_rook, (100, 100)), (290, 350))
                display.blit(pygame.transform.scale(white_bishop, (120, 120)), (400, 340))
                display.blit(pygame.transform.scale(white_knight, (100, 100)), (530, 350))
                display.blit(pygame.transform.scale(pt_button_schatten, (180, 30)), (310, 460))
                display.blit(pygame.transform.scale(pt_button, (180, 30)), (305, 455))
                white_bishop_pr = False
            elif pygame.mouse.get_pressed()[0] == False and white_knight_pr == True:
                display.blit(pygame.transform.scale(chess_field, (800, 800)), (0, 0))
                display.blit(pygame.transform.scale(pawn_tausch, (500, 200)), (150, 300))
                display.blit(pygame.transform.scale(white_queen, (100, 100)), (170, 350))
                display.blit(pygame.transform.scale(white_rook, (100, 100)), (290, 350))
                display.blit(pygame.transform.scale(white_bishop, (100, 100)), (410, 350))
                display.blit(pygame.transform.scale(white_knight, (120, 120)), (520, 340))
                display.blit(pygame.transform.scale(pt_button_schatten, (180, 30)), (310, 460))
                display.blit(pygame.transform.scale(pt_button, (180, 30)), (305, 455))
                white_knight_pr = False

            if pygame.mouse.get_pressed()[0] == True and pygame.mouse.get_pos()[0] in range(305, 485) and pygame.mouse.get_pos()[1] in range(455, 485):
                pt_button_pressed = True
                display.blit(pygame.transform.scale(chess_field, (800, 800)), (0, 0))
                display.blit(pygame.transform.scale(pawn_tausch, (500, 200)), (150, 300))
                if white_queen_pr == True:
                    display.blit(pygame.transform.scale(white_queen, (120, 120)), (160, 340))
                elif white_queen_pr == False:
                    display.blit(pygame.transform.scale(white_queen, (100, 100)), (170, 350))
                if white_rook_pr == True:
                    display.blit(pygame.transform.scale(white_rook, (120, 120)), (280, 340))
                elif white_rook_pr == False:
                    display.blit(pygame.transform.scale(white_rook, (100, 100)), (290, 350))
                if white_bishop_pr == True:
                    display.blit(pygame.transform.scale(white_bishop, (120, 120)), (400, 340))
                elif white_bishop_pr == False:
                    display.blit(pygame.transform.scale(white_bishop, (100, 100)), (410, 350))
                if white_knight_pr == True:
                    display.blit(pygame.transform.scale(white_knight, (120, 120)), (520, 340))
                elif white_knight_pr == False:
                    display.blit(pygame.transform.scale(white_knight, (100, 100)), (530, 350))
                display.blit(pygame.transform.scale(pt_button_schatten, (180, 30)), (310, 460))
                display.blit(pygame.transform.scale(pt_button, (180, 30)), (310, 460))
            if pygame.mouse.get_pressed()[0] == False and pt_button_pressed == True:
                pt_button_pressed = False
                display.blit(pygame.transform.scale(pt_button_schatten, (180, 30)), (310, 460))
                display.blit(pygame.transform.scale(pt_button, (180, 30)), (305, 455))


        pygame.display.flip()
main()
