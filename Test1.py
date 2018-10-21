
# -*- coding: UTF-8 -*-
from sys import exit
import os
import pygame
from pygame.locals import *
os.system("cls")
import time

white_king_pos_bg = [400, 700]
white_queen_pos_bg = [300, 700]
white_rook_pos_1_bg = [0, 700]
white_rook_pos_2_bg = [700, 700]
white_bishop_pos_1_bg = [200, 700]
white_bishop_pos_2_bg = [500, 700]
white_pawn_pos_1_bg = [0, 600]
white_pawn_pos_2_bg = [100, 600]
white_pawn_pos_3_bg = [200, 600]
white_pawn_pos_4_bg = [300, 600]
white_pawn_pos_5_bg = [400, 600]
white_pawn_pos_6_bg = [500, 600]
white_pawn_pos_7_bg = [600, 600]
white_pawn_pos_8_bg = [700, 600]
white_knight_pos_1_bg = [100, 700]
white_knight_pos_2_bg = [600, 700]

black_king_pos_bg = [400, 0]
black_queen_pos_bg = [300, 0]
black_rook_pos_1_bg = [0, 0]
black_rook_pos_2_bg = [700, 0]
black_bishop_pos_1_bg = [200, 0]
black_bishop_pos_2_bg = [500, 0]
black_pawn_pos_1_bg = [0, 100]
black_pawn_pos_2_bg = [100, 100]
black_pawn_pos_3_bg = [200, 100]
black_pawn_pos_4_bg = [300, 100]
black_pawn_pos_5_bg = [400, 100]
black_pawn_pos_6_bg = [500, 100]
black_pawn_pos_7_bg = [100, 100]
black_pawn_pos_8_bg = [700, 100]
black_knight_pos_1_bg = [100, 0]
black_knight_pos_2_bg = [600, 0]

button_pressed = False

felder_xy = [
	[0, 0],
	[100, 0],
	[200, 0],
	[300, 0],
	[400, 0],
	[500, 0],
	[600, 0],
	[700, 0],
	[0, 100],
	[100, 100],
	[200, 100],
	[300, 100],
	[400, 100],
	[500, 100],
	[600, 100],
	[700, 100],
	[0, 200],
	[100, 200],
	[200, 200],
	[300, 200],
	[400, 200],
	[500, 200],
	[600, 200],
	[700, 200],
	[0, 300],
	[100, 300],
	[200, 300],
	[300, 300],
	[400, 300],
	[500, 300],
	[600, 300],
	[700, 300],
	[0, 400],
	[100, 400],
	[200, 400],
	[300, 400],
	[400, 400],
	[500, 400],
	[600, 400],
	[700, 400],
	[0, 500],
	[100, 500],
	[200, 500],
	[300, 500],
	[400, 500],
	[500, 500],
	[600, 500],
	[700, 500],
	[0, 600],
	[100, 600],
	[200, 600],
	[300, 600],
	[400, 600],
	[500, 600],
	[600, 600],
	[700, 600],
	[0, 700],
	[100, 700],
	[200, 700],
	[300, 700],
	[400, 700],
	[500, 700],
	[600, 700],
	[700, 700]
]
felder = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
	11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
	21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
	31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
	41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
	51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
	61, 62, 63, 64]

grundreihe_black = [
	[0, 0],
	[100, 0],
	[200, 0],
	[300, 0],
	[400, 0],
	[500, 0],
	[600, 0],
	[700, 0]
]

grundreihe_white = [
	[0, 700],
	[100, 700],
	[200, 700],
	[300, 700],
	[400, 700],
	[500, 700],
	[600, 700],
	[700, 700]
]

pawn_gr_white = [
	33,
	34,
	35,
	36,
	37,
	38,
	39,
	40
]

pawn_gr_black = [
	25,
	26,
	27,
	28,
	29,
	30,
	31,
	32
]

xy_after = 0
xy_beginning = 0
feld_farbe = ""
wert_bauer = 1
wert_läufer = 3
wert_springer = 3
wert_turm = 5
wert_dame = 9
wert_könig = 10000
feld_schwarz = [2, 4, 6, 8, 9, 11, 13 ,15, 18, 20, 22, 24, 25, 27, 29, 31, 34, 36, 38, 40, 41, 43, 45, 47, 50, 52, 54, 56, 57, 59, 61, 63]
feld_weiß = [1, 3, 5, 7, 10, 12, 14, 16, 17, 19, 21, 23, 26, 28, 30, 32, 33, 35, 37, 39, 42, 44, 46, 48, 49, 51, 53, 55, 58, 60, 62, 64]

feld_weiß_xy = [
	[0, 0],

	[200, 0],

	[400, 0],

	[600, 0],


	[100, 100],

	[300, 100],

	[500, 100],

	[700, 100],
	[0, 200],

	[200, 200],

	[400, 200],

	[600, 200],


	[100, 300],

	[300, 300],

	[500, 300],

	[700, 300],
	[0, 400],

	[200, 400],

	[400, 400],

	[600, 400],


	[100, 500],

	[300, 500],

	[500, 500],

	[700, 500],
	[0, 600],

	[200, 600],

	[400, 600],

	[600, 600],


	[100, 700],

	[300, 700],

	[500, 700],

	[700, 700]
]
feld_schwarz_xy = [

	[100, 0],

	[300, 0],

	[500, 0],

	[700, 0],
	[0, 100],

	[200, 100],

	[400, 100],

	[600, 100],


	[100, 200],

	[300, 200],

	[500, 200],

	[700, 200],
	[0, 300],

	[200, 300],

	[400, 300],

	[600, 300],


	[100, 400],

	[300, 400],

	[500, 400],

	[700, 400],
	[0, 500],

	[200, 500],

	[400, 500],

	[600, 500],


	[100, 600],

	[300, 600],

	[500, 600],

	[700, 600],
	[0, 700],

	[200, 700],

	[400, 700],

	[600, 700],
]

ex_white_king = True
ex_white_queen = True
ex_white_rook_1 = True
ex_white_rook_2 = True
ex_white_bishop_1 = True
ex_white_bishop_2 = True
ex_white_knight_1 = True
ex_white_knight_2 = True
ex_white_pawn_1 = True
ex_white_pawn_2 = True
ex_white_pawn_3 = True
ex_white_pawn_4 = True
ex_white_pawn_5 = True
ex_white_pawn_6 = True
ex_white_pawn_7 = True
ex_white_pawn_8 = True

ex_black_king = True
ex_black_queen = True
ex_black_rook_1 = True
ex_black_rook_2 = True
ex_black_bishop_1 = True
ex_black_bishop_2 = True
ex_black_knight_1 = True
ex_black_knight_2 = True
ex_black_pawn_1 = True
ex_black_pawn_2 = True
ex_black_pawn_3 = True
ex_black_pawn_4 = True
ex_black_pawn_5 = True
ex_black_pawn_6 = True
ex_black_pawn_7 = True
ex_black_pawn_8 = True

zug = "white"

besetzt = []#1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]

schach = False

legal_pr = ""

roch_white_rook_1 = True
roch_white_rook_2 = True
roch_white_king = True
roch_black_rook_1 = True
roch_black_rook_2 = True
roch_black_king = True

roch_white_kurz = False
roch_white_lang = False
roch_black_kurz = False
roch_black_lang = False

ep_white_pawn_1 = False
ep_white_pawn_2 = False
ep_white_pawn_3 = False
ep_white_pawn_4 = False
ep_white_pawn_5 = False
ep_white_pawn_6 = False
ep_white_pawn_7 = False
ep_white_pawn_8 = False
ep_black_pawn_1 = False
ep_black_pawn_2 = False
ep_black_pawn_3 = False
ep_black_pawn_4 = False
ep_black_pawn_5 = False
ep_black_pawn_6 = False
ep_black_pawn_7 = False
ep_black_pawn_8 = False

def main():
	default_aufstellung = input("Normale Aufstellung? ")
	if default_aufstellung.lower() == "nein":
		print("Coming Soon")
	else:
		pass

	pygame.init()
	display = pygame.display.set_mode((1700, 800), HWSURFACE | DOUBLEBUF | RESIZABLE)
	pygame.display.set_caption("Schach")
	pygame.mouse.set_visible(1)
	pygame.key.set_repeat(1, 30)

	clock = pygame.time.Clock()

	global schach

	global grundreihe_black
	global grundreihe_white

	global besetzt

	global feld_weiß
	global feld_schwarz

	global ex_white_king
	global ex_white_queen
	global ex_white_rook_1
	global ex_white_rook_2
	global ex_white_bishop_1
	global ex_white_bishop_2
	global ex_white_knight_1
	global ex_white_knight_2
	global ex_white_pawn_1
	global ex_white_pawn_2
	global ex_white_pawn_3
	global ex_white_pawn_4
	global ex_white_pawn_5
	global ex_white_pawn_6
	global ex_white_pawn_7
	global ex_white_pawn_8

	global ex_black_king
	global ex_black_queen
	global ex_black_rook_1
	global ex_black_rook_2
	global ex_black_bishop_1
	global ex_black_bishop_2
	global ex_black_knight_1
	global ex_black_knight_2
	global ex_black_pawn_1
	global ex_black_pawn_2
	global ex_black_pawn_3
	global ex_black_pawn_4
	global ex_black_pawn_5
	global ex_black_pawn_6
	global ex_black_pawn_7
	global ex_black_pawn_8

	global zug
	global legal_pr

	global roch_white_rook_1
	global roch_white_rook_2
	global roch_white_king
	global roch_black_rook_1
	global roch_black_rook_2
	global roch_black_king

	global roch_white_kurz
	global roch_white_lang
	global roch_black_kurz
	global roch_black_lang

	running = True

	timeout_x = open("zahlen.dat", "r")
	timeout = timeout_x.read().splitlines()
	timeout_x.close

	white_king_pos_bg = [400, 700]
	white_queen_pos_bg = [300, 700]
	white_rook_pos_1_bg = [0, 700]
	white_rook_pos_2_bg = [700, 700]
	white_bishop_pos_1_bg = [200, 700]
	white_bishop_pos_2_bg = [500, 700]
	white_pawn_pos_1_bg = [0, 600]
	white_pawn_pos_2_bg = [100, 600]
	white_pawn_pos_3_bg = [200, 600]
	white_pawn_pos_4_bg = [300, 600]
	white_pawn_pos_5_bg = [400, 600]
	white_pawn_pos_6_bg = [500, 600]
	white_pawn_pos_7_bg = [600, 600]
	white_pawn_pos_8_bg = [700, 600]
	white_knight_pos_1_bg = [100, 700]
	white_knight_pos_2_bg = [600, 700]

	black_king_pos_bg = [400, 0]
	black_queen_pos_bg = [300, 0]
	black_rook_pos_1_bg = [0, 0]
	black_rook_pos_2_bg = [700, 0]
	black_bishop_pos_1_bg = [200, 0]
	black_bishop_pos_2_bg = [500, 0]
	black_pawn_pos_1_bg = [0, 100]
	black_pawn_pos_2_bg = [100, 100]
	black_pawn_pos_3_bg = [200, 100]
	black_pawn_pos_4_bg = [300, 100]
	black_pawn_pos_5_bg = [400, 100]
	black_pawn_pos_6_bg = [500, 100]
	black_pawn_pos_7_bg = [100, 100]
	black_pawn_pos_8_bg = [700, 100]
	black_knight_pos_1_bg = [100, 0]
	black_knight_pos_2_bg = [600, 0]

	white_king_pos = [400, 700]
	white_queen_pos = [300, 700]
	white_rook_pos_1 = [0, 700]
	white_rook_pos_2 = [700, 700]
	white_bishop_pos_1 = [200, 700]
	white_bishop_pos_2 = [500, 700]
	white_pawn_pos_1 = [0, 600]
	white_pawn_pos_2 = [100, 600]
	white_pawn_pos_3 = [200, 600]
	white_pawn_pos_4 = [300, 600]
	white_pawn_pos_5 = [400, 600]
	white_pawn_pos_6 = [500, 600]
	white_pawn_pos_7 = [600, 600]
	white_pawn_pos_8 = [700, 600]
	white_knight_pos_1 = [100, 700]
	white_knight_pos_2 = [600, 700]

	black_king_pos = [400, 0]
	black_queen_pos = [300, 0]
	black_rook_pos_1 = [0, 0]
	black_rook_pos_2 = [700, 0]
	black_bishop_pos_1 = [200, 0]
	black_bishop_pos_2 = [500, 0]
	black_pawn_pos_1 = [0, 100]
	black_pawn_pos_2 = [100, 100]
	black_pawn_pos_3 = [200, 100]
	black_pawn_pos_4 =  [300, 100]
	black_pawn_pos_5 = [400, 100]
	black_pawn_pos_6 = [500, 100]
	black_pawn_pos_7 = [600, 100]
	black_pawn_pos_8 = [700, 100]
	black_knight_pos_1 = [100, 0]
	black_knight_pos_2 = [600, 0]

	white_king_bw = False
	white_queen_bw = False
	white_rook_1_bw = False
	white_rook_2_bw = False
	white_bishop_1_bw = False
	white_bishop_2_bw = False
	white_knight_1_bw = False
	white_knight_2_bw = False
	white_pawn_1_bw = False
	white_pawn_2_bw = False
	white_pawn_3_bw = False
	white_pawn_4_bw = False
	white_pawn_5_bw = False
	white_pawn_6_bw = False
	white_pawn_7_bw = False
	white_pawn_8_bw = False

	black_king_bw = False
	black_queen_bw = False
	black_rook_1_bw = False
	black_rook_2_bw = False
	black_bishop_1_bw = False
	black_bishop_2_bw = False
	black_knight_1_bw = False
	black_knight_2_bw = False
	black_pawn_1_bw = False
	black_pawn_2_bw = False
	black_pawn_3_bw = False
	black_pawn_4_bw = False
	black_pawn_5_bw = False
	black_pawn_6_bw = False
	black_pawn_7_bw = False
	black_pawn_8_bw = False

	white_pawn_1_gr = False
	white_pawn_2_gr = False
	white_pawn_3_gr = False
	white_pawn_4_gr = False
	white_pawn_5_gr = False
	white_pawn_6_gr = False
	white_pawn_7_gr = False
	white_pawn_8_gr = False

	black_pawn_1_gr = False
	black_pawn_2_gr = False
	black_pawn_3_gr = False
	black_pawn_4_gr = False
	black_pawn_5_gr = False
	black_pawn_6_gr = False
	black_pawn_7_gr = False
	black_pawn_8_gr = False

	pawn_gr = False

	chess_field = pygame.image.load("Schachbrett_Nummerierung_1.png")
	right_field = pygame.image.load("PySchachBildRechts.png")

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

	if icon.get_alpha() is None:
		icon = icon.convert()
	else:
		icon = icon.convert_alpha()
	pygame.display.set_icon(icon)
	display.fill((0, 0, 0))
	display.blit(pygame.transform.scale(chess_field, (800, 800)), (0, 0))
	display.blit(pygame.transform.scale(right_field, (900, 800)), (800, 0))

	play_pers = ""
	ausführen = True
	button_pressed = False
	legal_ausführen = True
	feld_farbe = ""
	xy_beginning = None
	xy_after = None
	legal_sp = False
	xy_after_fig = ""

	figures_af_str = ["white_king",
			   "white_queen",
			   "white_rook_1",
			   "white_rook_2",
			   "white_bishop_1",
			   "white_bishop_2",
			   "white_knight_1",
			   "white_knight_2",
			   "white_pawn_1",
			   "white_pawn_2",
			   "white_pawn_3",
			   "white_pawn_4",
			   "white_pawn_5",
			   "white_pawn_6",
			   "white_pawn_7",
			   "white_pawn_8",
			   "black_king",
			   "black_queen",
			   "black_rook_1",
			   "black_rook_2",
			   "black_bishop_1",
			   "black_bishop_2",
			   "black_knight_1",
			   "black_knight_2",
			   "black_pawn_1",
			   "black_pawn_2",
			   "black_pawn_3",
			   "black_pawn_4",
			   "black_pawn_5",
			   "black_pawn_6",
			   "black_pawn_7",
			   "black_pawn_8"]

	white_pawn_gr = False
	black_pawn_gr = False
	white_queen_pr = False
	white_rook_pr = False
	white_bishop_pr = False
	white_knight_pr = False
	black_queen_pr = False
	black_rook_pr = False
	black_bishop_pr = False
	black_knight_pr = False
	pt_button_pressed = False
	pt_figur = ""
	white_pawn_gr_aus = False
	black_pawn_gr_aus = False
	white_queen_pt = False
	white_rook_pt = False
	white_bishop_pt = False
	white_knight_pt = False
	black_queen_pt = False
	black_rook_pt = False
	black_bishop_pt = False
	black_knight_pt = False

	gr_white_pawn_1 = False
	gr_white_pawn_2 = False
	gr_white_pawn_3 = False
	gr_white_pawn_4 = False
	gr_white_pawn_5 = False
	gr_white_pawn_6 = False
	gr_white_pawn_7 = False
	gr_white_pawn_8 = False

	gr_black_pawn_1 = False
	gr_black_pawn_2 = False
	gr_black_pawn_3 = False
	gr_black_pawn_4 = False
	gr_black_pawn_5 = False
	gr_black_pawn_6 = False
	gr_black_pawn_7 = False
	gr_black_pawn_8 = False

	pt_white_pawn_1 = ""
	pt_white_pawn_2 = ""
	pt_white_pawn_3 = ""
	pt_white_pawn_4 = ""
	pt_white_pawn_5 = ""
	pt_white_pawn_6 = ""
	pt_white_pawn_7 = ""
	pt_white_pawn_8 = ""

	pt_black_pawn_1 = ""
	pt_black_pawn_2 = ""
	pt_black_pawn_3 = ""
	pt_black_pawn_4 = ""
	pt_black_pawn_5 = ""
	pt_black_pawn_6 = ""
	pt_black_pawn_7 = ""
	pt_black_pawn_8 = ""

	while running:

		figures = [white_king_bw,
		           white_queen_bw,
		           white_rook_1_bw,
		           white_rook_2_bw,
		           white_bishop_1_bw,
		           white_bishop_2_bw,
				   white_knight_1_bw,
		           white_knight_2_bw,
		           white_pawn_1_bw,
		           white_pawn_2_bw,
		           white_pawn_3_bw,
		           white_pawn_4_bw,
		           white_pawn_5_bw,
		           white_pawn_6_bw,
		           white_pawn_7_bw,
		           white_pawn_8_bw,
		           black_king_bw,
		           black_queen_bw,
		           black_rook_1_bw,
		           black_rook_2_bw,
		           black_bishop_1_bw,
		           black_bishop_2_bw,
				   black_knight_1_bw,
				   black_knight_2_bw,
		           black_pawn_1_bw,
		           black_pawn_2_bw,
		           black_pawn_3_bw,
		           black_pawn_4_bw,
		           black_pawn_5_bw,
		           black_pawn_6_bw,
		           black_pawn_7_bw,
		           black_pawn_8_bw]

		figures_bg = [white_king_pos_bg,
		           white_queen_pos_bg,
		           white_rook_pos_1_bg,
		           white_rook_pos_2_bg,
		           white_bishop_pos_1_bg,
		           white_bishop_pos_2_bg,
				   white_knight_pos_1_bg,
 		           white_knight_pos_2_bg,
		           white_pawn_pos_1_bg,
		           white_pawn_pos_2_bg,
		           white_pawn_pos_3_bg,
		           white_pawn_pos_4_bg,
		           white_pawn_pos_5_bg,
		           white_pawn_pos_6_bg,
		           white_pawn_pos_7_bg,
		           white_pawn_pos_8_bg,
		           black_king_pos_bg,
		           black_queen_pos_bg,
		           black_rook_pos_1_bg,
		           black_rook_pos_2_bg,
		           black_bishop_pos_1_bg,
		           black_bishop_pos_2_bg,
				    black_knight_pos_1_bg,
 				   black_knight_pos_2_bg,
		           black_pawn_pos_1_bg,
		           black_pawn_pos_2_bg,
		           black_pawn_pos_3_bg,
		           black_pawn_pos_4_bg,
		           black_pawn_pos_5_bg,
		           black_pawn_pos_6_bg,
		           black_pawn_pos_7_bg,
		           black_pawn_pos_8_bg]

		figures_af = [white_king_pos,
		           white_queen_pos,
		           white_rook_pos_1,
		           white_rook_pos_2,
		           white_bishop_pos_1,
		           white_bishop_pos_2,
				   white_knight_pos_1,
		           white_knight_pos_2,
		           white_pawn_pos_1,
		           white_pawn_pos_2,
		           white_pawn_pos_3,
		           white_pawn_pos_4,
		           white_pawn_pos_5,
		           white_pawn_pos_6,
		           white_pawn_pos_7,
		           white_pawn_pos_8,
		           black_king_pos,
		           black_queen_pos,
		           black_rook_pos_1,
		           black_rook_pos_2,
		           black_bishop_pos_1,
		           black_bishop_pos_2,
				   black_knight_pos_1,
				   black_knight_pos_2,
		           black_pawn_pos_1,
		           black_pawn_pos_2,
		           black_pawn_pos_3,
		           black_pawn_pos_4,
		           black_pawn_pos_5,
		           black_pawn_pos_6,
		           black_pawn_pos_7,
		           black_pawn_pos_8]

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
				display.blit(pygame.transform.scale(right_field, (900, 800)), (800, 0))

				size_x = 100
				size_y = 100

				if ex_white_king == True:
					display.blit(pygame.transform.scale(white_king, (int(size_x), int(size_y))), (white_king_pos))
				if ex_white_queen == True:
					display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_queen_pos))
				if ex_white_rook_1 == True:
					display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_rook_pos_1))
				if ex_white_rook_2 == True:
					display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_rook_pos_2))
				if ex_white_bishop_1 == True:
					display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_bishop_pos_1))
				if ex_white_bishop_2 == True:
					display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_bishop_pos_2))
				if ex_white_knight_1 == True:
					display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_knight_pos_1))
				if ex_white_knight_2 == True:
					display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_knight_pos_2))
				if ex_white_pawn_1 == True:
					if gr_white_pawn_1 == False:
						display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_1))
					else:
						if pt_white_pawn_1 == "white_queen":
							display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_pawn_pos_1))
						elif pt_white_pawn_1 == "white_rook":
							display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_pawn_pos_1))
						elif pt_white_pawn_1 == "white_bishop":
							display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_pawn_pos_1))
						elif pt_white_pawn_1 == "white_knight":
							display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_pawn_pos_1))
				if ex_white_pawn_2 == True:
					if gr_white_pawn_2 == False:
						display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_2))
					else:
						if pt_white_pawn_2 == "white_queen":
							display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_pawn_pos_2))
						elif pt_white_pawn_2 == "white_rook":
							display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_pawn_pos_2))
						elif pt_white_pawn_2 == "white_bishop":
							display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_pawn_pos_2))
						elif pt_white_pawn_2 == "white_knight":
							display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_pawn_pos_2))
				if ex_white_pawn_3 == True:
					if gr_white_pawn_3 == False:
						display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_3))
					else:
						if pt_white_pawn_3 == "white_queen":
							display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_pawn_pos_3))
						elif pt_white_pawn_3 == "white_rook":
							display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_pawn_pos_3))
						elif pt_white_pawn_3 == "white_bishop":
							display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_pawn_pos_3))
						elif pt_white_pawn_3 == "white_knight":
							display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_pawn_pos_3))
				if ex_white_pawn_4 == True:
					if gr_white_pawn_4 == False:
						display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_4))
					else:
						if pt_white_pawn_4 == "white_queen":
							display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_pawn_pos_4))
						elif pt_white_pawn_4 == "white_rook":
							display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_pawn_pos_4))
						elif pt_white_pawn_4 == "white_bishop":
							display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_pawn_pos_4))
						elif pt_white_pawn_4 == "white_knight":
							display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_pawn_pos_4))
				if ex_white_pawn_5 == True:
					if gr_white_pawn_5 == False:
						display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_5))
					else:
						if pt_white_pawn_5 == "white_queen":
							display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_pawn_pos_5))
						elif pt_white_pawn_5 == "white_rook":
							display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_pawn_pos_5))
						elif pt_white_pawn_5 == "white_bishop":
							display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_pawn_pos_5))
						elif pt_white_pawn_5 == "white_knight":
							display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_pawn_pos_5))
				if ex_white_pawn_6 == True:
					if gr_white_pawn_6 == False:
						display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_6))
					else:
						if pt_white_pawn_6 == "white_queen":
							display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_pawn_pos_6))
						elif pt_white_pawn_6 == "white_rook":
							display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_pawn_pos_6))
						elif pt_white_pawn_6 == "white_bishop":
							display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_pawn_pos_6))
						elif pt_white_pawn_6 == "white_knight":
							display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_pawn_pos_6))
				if ex_white_pawn_7 == True:
					if gr_white_pawn_7 == False:
						display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_7))
					else:
						if pt_white_pawn_7 == "white_queen":
							display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_pawn_pos_7))
						elif pt_white_pawn_7 == "white_rook":
							display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_pawn_pos_7))
						elif pt_white_pawn_7 == "white_bishop":
							display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_pawn_pos_7))
						elif pt_white_pawn_7 == "white_knight":
							display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_pawn_pos_7))
				if ex_white_pawn_8 == True:
					if gr_white_pawn_8 == False:
						display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_8))
					else:
						if pt_white_pawn_8 == "white_queen":
							display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_pawn_pos_8))
						elif pt_white_pawn_8 == "white_rook":
							display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_pawn_pos_8))
						elif pt_white_pawn_8 == "white_bishop":
							display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_pawn_pos_8))
						elif pt_white_pawn_8 == "white_knight":
							display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_pawn_pos_8))

				if ex_black_king == True:
					display.blit(pygame.transform.scale(black_king, (int(size_x), int(size_y))), (black_king_pos))
				if ex_black_queen == True:
					display.blit(pygame.transform.scale(black_queen, (int(size_x), int(size_y))), (black_queen_pos))
				if ex_black_rook_1 == True:
					display.blit(pygame.transform.scale(black_rook, (int(size_x), int(size_y))), (black_rook_pos_1))
				if ex_black_rook_2 == True:
					display.blit(pygame.transform.scale(black_rook, (int(size_x), int(size_y))), (black_rook_pos_2))
				if ex_black_bishop_1 == True:
					display.blit(pygame.transform.scale(black_bishop, (int(size_x), int(size_y))), (black_bishop_pos_1))
				if ex_black_bishop_2 == True:
					display.blit(pygame.transform.scale(black_bishop, (int(size_x), int(size_y))), (black_bishop_pos_2))
				if ex_black_knight_1 == True:
					display.blit(pygame.transform.scale(black_knight, (int(size_x), int(size_y))), (black_knight_pos_1))
				if ex_black_knight_2 == True:
					display.blit(pygame.transform.scale(black_knight, (int(size_x), int(size_y))), (black_knight_pos_2))
				if ex_black_pawn_1 == True:
					if gr_black_pawn_1 == False:
						display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_1))
					else:
						if pt_black_pawn_1 == "black_queen":
							display.blit(pygame.transform.scale(black_queen, (int(size_x), int(size_y))), (black_pawn_pos_1))
						elif pt_black_pawn_1 == "black_rook":
							display.blit(pygame.transform.scale(black_rook, (int(size_x), int(size_y))), (black_pawn_pos_1))
						elif pt_black_pawn_1 == "black_bishop":
							display.blit(pygame.transform.scale(black_bishop, (int(size_x), int(size_y))), (black_pawn_pos_1))
						elif pt_black_pawn_1 == "black_knight":
							display.blit(pygame.transform.scale(black_knight, (int(size_x), int(size_y))), (black_pawn_pos_1))
				if ex_black_pawn_2 == True:
					if gr_black_pawn_2 == False:
						display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_2))
					else:
						if pt_black_pawn_2 == "black_queen":
							display.blit(pygame.transform.scale(black_queen, (int(size_x), int(size_y))), (black_pawn_pos_2))
						elif pt_black_pawn_2 == "black_rook":
							display.blit(pygame.transform.scale(black_rook, (int(size_x), int(size_y))), (black_pawn_pos_2))
						elif pt_black_pawn_2 == "black_bishop":
							display.blit(pygame.transform.scale(black_bishop, (int(size_x), int(size_y))), (black_pawn_pos_2))
						elif pt_black_pawn_2 == "black_knight":
							display.blit(pygame.transform.scale(black_knight, (int(size_x), int(size_y))), (black_pawn_pos_2))
				if ex_black_pawn_3 == True:
					if gr_black_pawn_3 == False:
						display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_3))
					else:
						if pt_black_pawn_3 == "black_queen":
							display.blit(pygame.transform.scale(black_queen, (int(size_x), int(size_y))), (black_pawn_pos_3))
						elif pt_black_pawn_3 == "black_rook":
							display.blit(pygame.transform.scale(black_rook, (int(size_x), int(size_y))), (black_pawn_pos_3))
						elif pt_black_pawn_3 == "black_bishop":
							display.blit(pygame.transform.scale(black_bishop, (int(size_x), int(size_y))), (black_pawn_pos_3))
						elif pt_black_pawn_3 == "black_knight":
							display.blit(pygame.transform.scale(black_knight, (int(size_x), int(size_y))), (black_pawn_pos_3))
				if ex_black_pawn_4 == True:
					if gr_black_pawn_4 == False:
						display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_4))
					else:
						if pt_black_pawn_4 == "black_queen":
							display.blit(pygame.transform.scale(black_queen, (int(size_x), int(size_y))), (black_pawn_pos_4))
						elif pt_black_pawn_4 == "black_rook":
							display.blit(pygame.transform.scale(black_rook, (int(size_x), int(size_y))), (black_pawn_pos_4))
						elif pt_black_pawn_4 == "black_bishop":
							display.blit(pygame.transform.scale(black_bishop, (int(size_x), int(size_y))), (black_pawn_pos_4))
						elif pt_black_pawn_4 == "black_knight":
							display.blit(pygame.transform.scale(black_knight, (int(size_x), int(size_y))), (black_pawn_pos_4))
				if ex_black_pawn_5 == True:
					if gr_black_pawn_5 == False:
						display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_5))
					else:
						if pt_black_pawn_5 == "black_queen":
							display.blit(pygame.transform.scale(black_queen, (int(size_x), int(size_y))), (black_pawn_pos_5))
						elif pt_black_pawn_5 == "black_rook":
							display.blit(pygame.transform.scale(black_rook, (int(size_x), int(size_y))), (black_pawn_pos_5))
						elif pt_black_pawn_5 == "black_bishop":
							display.blit(pygame.transform.scale(black_bishop, (int(size_x), int(size_y))), (black_pawn_pos_5))
						elif pt_black_pawn_5 == "black_knight":
							display.blit(pygame.transform.scale(black_knight, (int(size_x), int(size_y))), (black_pawn_pos_5))
				if ex_black_pawn_6 == True:
					if gr_black_pawn_6 == False:
						display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_6))
					else:
						if pt_black_pawn_6 == "black_queen":
							display.blit(pygame.transform.scale(black_queen, (int(size_x), int(size_y))), (black_pawn_pos_6))
						elif pt_black_pawn_6 == "black_rook":
							display.blit(pygame.transform.scale(black_rook, (int(size_x), int(size_y))), (black_pawn_pos_6))
						elif pt_black_pawn_6 == "black_bishop":
							display.blit(pygame.transform.scale(black_bishop, (int(size_x), int(size_y))), (black_pawn_pos_6))
						elif pt_black_pawn_6 == "black_knight":
							display.blit(pygame.transform.scale(black_knight, (int(size_x), int(size_y))), (black_pawn_pos_6))
				if ex_black_pawn_7 == True:
					if gr_black_pawn_7 == False:
						display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_7))
					else:
						if pt_black_pawn_7 == "black_queen":
							display.blit(pygame.transform.scale(black_queen, (int(size_x), int(size_y))), (black_pawn_pos_7))
						elif pt_black_pawn_7 == "black_rook":
							display.blit(pygame.transform.scale(black_rook, (int(size_x), int(size_y))), (black_pawn_pos_7))
						elif pt_black_pawn_7 == "black_bishop":
							display.blit(pygame.transform.scale(black_bishop, (int(size_x), int(size_y))), (black_pawn_pos_7))
						elif pt_black_pawn_7 == "black_knight":
							display.blit(pygame.transform.scale(black_knight, (int(size_x), int(size_y))), (black_pawn_pos_7))
				if ex_black_pawn_8 == True:
					if gr_black_pawn_8 == False:
						display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_8))
					else:
						if pt_black_pawn_8 == "black_queen":
							display.blit(pygame.transform.scale(black_queen, (int(size_x), int(size_y))), (black_pawn_pos_8))
						elif pt_black_pawn_8 == "black_rook":
							display.blit(pygame.transform.scale(black_rook, (int(size_x), int(size_y))), (black_pawn_pos_8))
						elif pt_black_pawn_8 == "black_bishop":
							display.blit(pygame.transform.scale(black_bishop, (int(size_x), int(size_y))), (black_pawn_pos_8))
						elif pt_black_pawn_8 == "black_knight":
							display.blit(pygame.transform.scale(black_knight, (int(size_x), int(size_y))), (black_pawn_pos_8))

			if pygame.mouse.get_pressed()[0] == True and ausführen == True:
				button_pressed_xy = pygame.mouse.get_pos()

				if ex_white_king == True and button_pressed_xy[0] in range(white_king_pos[0], (white_king_pos[0] + 100)) and button_pressed_xy[1] in range(white_king_pos[1], (white_king_pos[1] + 100)):
					play_pers = "white_king"
					button_pressed = True
					break
				elif ex_white_queen == True and button_pressed_xy[0] in range(white_queen_pos[0], (white_queen_pos[0] + 100)) and button_pressed_xy[1] in range(white_queen_pos[1], (white_queen_pos[1] + 100)):
					play_pers = "white_queen"
					button_pressed = True
					break
				elif ex_white_rook_1 == True and button_pressed_xy[0] in range(white_rook_pos_1[0], (white_rook_pos_1[0] + 100)) and button_pressed_xy[1] in range(white_rook_pos_1[1], (white_rook_pos_1[1] + 100)):
					play_pers = "white_rook_1"
					button_pressed = True
					break
				elif ex_white_rook_2 == True and button_pressed_xy[0] in range(white_rook_pos_2[0], (white_rook_pos_2[0] + 100)) and button_pressed_xy[1] in range(white_rook_pos_2[1], (white_rook_pos_2[1] + 100)):
					play_pers = "white_rook_2"
					button_pressed = True
					break
				elif ex_white_bishop_1 == True and button_pressed_xy[0] in range(white_bishop_pos_1[0], (white_bishop_pos_1[0] + 100)) and button_pressed_xy[1] in range(white_bishop_pos_1[1], (white_bishop_pos_1[1] + 100)):
					play_pers = "white_bishop_1"
					button_pressed = True
					break
				elif ex_white_bishop_2 == True and button_pressed_xy[0] in range(white_bishop_pos_2[0], (white_bishop_pos_2[0] + 100)) and button_pressed_xy[1] in range(white_bishop_pos_2[1], (white_bishop_pos_2[1] + 100)):
					play_pers = "white_bishop_2"
					button_pressed = True
					break
				elif ex_white_knight_1 == True and button_pressed_xy[0] in range(white_knight_pos_1[0], (white_knight_pos_1[0] + 100)) and button_pressed_xy[1] in range(white_knight_pos_1[1], (white_knight_pos_1[1] + 100)):
					play_pers = "white_knight_1"
					button_pressed = True
					break
				elif ex_white_knight_2 == True and button_pressed_xy[0] in range(white_knight_pos_2[0], (white_knight_pos_2[0] + 100)) and button_pressed_xy[1] in range(white_knight_pos_2[1], (white_knight_pos_2[1] + 100)):
					play_pers = "white_knight_2"
					button_pressed = True
					break
				elif ex_white_pawn_1 == True and button_pressed_xy[0] in range(white_pawn_pos_1[0], (white_pawn_pos_1[0] + 100)) and button_pressed_xy[1] in range(white_pawn_pos_1[1], (white_pawn_pos_1[1] + 100)):
					play_pers = "white_pawn_1"
					button_pressed = True
					break
				elif ex_white_pawn_2 == True and button_pressed_xy[0] in range(white_pawn_pos_2[0], (white_pawn_pos_2[0] + 100)) and button_pressed_xy[1] in range(white_pawn_pos_2[1], (white_pawn_pos_2[1] + 100)):
					play_pers = "white_pawn_2"
					button_pressed = True
					break
				elif ex_white_pawn_3 == True and button_pressed_xy[0] in range(white_pawn_pos_3[0], (white_pawn_pos_3[0] + 100)) and button_pressed_xy[1] in range(white_pawn_pos_3[1], (white_pawn_pos_3[1] + 100)):
					play_pers = "white_pawn_3"
					button_pressed = True
					break
				elif ex_white_pawn_4 == True and button_pressed_xy[0] in range(white_pawn_pos_4[0], (white_pawn_pos_4[0] + 100)) and button_pressed_xy[1] in range(white_pawn_pos_4[1], (white_pawn_pos_4[1] + 100)):
					play_pers = "white_pawn_4"
					button_pressed = True
					break
				elif ex_white_pawn_5 == True and button_pressed_xy[0] in range(white_pawn_pos_5[0], (white_pawn_pos_5[0] + 100)) and button_pressed_xy[1] in range(white_pawn_pos_5[1], (white_pawn_pos_5[1] + 100)):
					play_pers = "white_pawn_5"
					button_pressed = True
					break
				elif ex_white_pawn_6 == True and button_pressed_xy[0] in range(white_pawn_pos_6[0], (white_pawn_pos_6[0] + 100)) and button_pressed_xy[1] in range(white_pawn_pos_6[1], (white_pawn_pos_6[1] + 100)):
					play_pers = "white_pawn_6"
					button_pressed = True
					break
				elif ex_white_pawn_7 == True and button_pressed_xy[0] in range(white_pawn_pos_7[0], (white_pawn_pos_7[0] + 100)) and button_pressed_xy[1] in range(white_pawn_pos_7[1], (white_pawn_pos_7[1] + 100)):
					play_pers = "white_pawn_7"
					button_pressed = True
					break
				elif ex_white_pawn_8 == True and button_pressed_xy[0] in range(white_pawn_pos_8[0], (white_pawn_pos_8[0] + 100)) and button_pressed_xy[1] in range(white_pawn_pos_8[1], (white_pawn_pos_8[1] + 100)):
					play_pers = "white_pawn_8"
					button_pressed = True
					break
				elif ex_black_king == True and button_pressed_xy[0] in range(black_king_pos[0], (black_king_pos[0] + 100)) and button_pressed_xy[1] in range(black_king_pos[1], (black_king_pos[1] + 100)):
					play_pers = "black_king"
					button_pressed = True
					break
				elif ex_black_queen == True and button_pressed_xy[0] in range(black_queen_pos[0], (black_queen_pos[0] + 100)) and button_pressed_xy[1] in range(black_queen_pos[1], (black_queen_pos[1] + 100)):
					play_pers = "black_queen"
					button_pressed = True
					break
				elif ex_black_rook_1 == True and button_pressed_xy[0] in range(black_rook_pos_1[0], (black_rook_pos_1[0] + 100)) and button_pressed_xy[1] in range(black_rook_pos_1[1], (black_rook_pos_1[1] + 100)):
					play_pers = "black_rook_1"
					button_pressed = True
					break
				elif ex_black_rook_2 == True and button_pressed_xy[0] in range(black_rook_pos_2[0], (black_rook_pos_2[0] + 100)) and button_pressed_xy[1] in range(black_rook_pos_2[1], (black_rook_pos_2[1] + 100)):
					play_pers = "black_rook_2"
					button_pressed = True
					break
				elif ex_black_bishop_1 == True and button_pressed_xy[0] in range(black_bishop_pos_1[0], (black_bishop_pos_1[0] + 100)) and button_pressed_xy[1] in range(black_bishop_pos_1[1], (black_bishop_pos_1[1] + 100)):
					play_pers = "black_bishop_1"
					button_pressed = True
					break
				elif ex_black_bishop_2 == True and button_pressed_xy[0] in range(black_bishop_pos_2[0], (black_bishop_pos_2[0] + 100)) and button_pressed_xy[1] in range(black_bishop_pos_2[1], (black_bishop_pos_2[1] + 100)):
					play_pers = "black_bishop_2"
					button_pressed = True
					break
				elif ex_black_knight_1 == True and button_pressed_xy[0] in range(black_knight_pos_1[0], (black_knight_pos_1[0] + 100)) and button_pressed_xy[1] in range(black_knight_pos_1[1], (black_knight_pos_1[1] + 100)):
					play_pers = "black_knight_1"
					button_pressed = True
					break
				elif ex_black_knight_2 == True and button_pressed_xy[0] in range(black_knight_pos_2[0], (black_knight_pos_2[0] + 100)) and button_pressed_xy[1] in range(black_knight_pos_2[1], (black_knight_pos_2[1] + 100)):
					play_pers = "black_knight_2"
					button_pressed = True
					break
				elif ex_black_pawn_1 == True and button_pressed_xy[0] in range(black_pawn_pos_1[0], (black_pawn_pos_1[0] + 100)) and button_pressed_xy[1] in range(black_pawn_pos_1[1], (black_pawn_pos_1[1] + 100)):
					play_pers = "black_pawn_1"
					button_pressed = True
					break
				elif ex_black_pawn_2 == True and button_pressed_xy[0] in range(black_pawn_pos_2[0], (black_pawn_pos_2[0] + 100)) and button_pressed_xy[1] in range(black_pawn_pos_2[1], (black_pawn_pos_2[1] + 100)):
					play_pers = "black_pawn_2"
					button_pressed = True
					break
				elif ex_black_pawn_3 == True and button_pressed_xy[0] in range(black_pawn_pos_3[0], (black_pawn_pos_3[0] + 100)) and button_pressed_xy[1] in range(black_pawn_pos_3[1], (black_pawn_pos_3[1] + 100)):
					play_pers = "black_pawn_3"
					button_pressed = True
					break
				elif ex_black_pawn_4 == True and button_pressed_xy[0] in range(black_pawn_pos_4[0], (black_pawn_pos_4[0] + 100)) and button_pressed_xy[1] in range(black_pawn_pos_4[1], (black_pawn_pos_4[1] + 100)):
					play_pers = "black_pawn_4"
					button_pressed = True
					break
				elif ex_black_pawn_5 == True and button_pressed_xy[0] in range(black_pawn_pos_5[0], (black_pawn_pos_5[0] + 100)) and button_pressed_xy[1] in range(black_pawn_pos_5[1], (black_pawn_pos_5[1] + 100)):
					play_pers = "black_pawn_5"
					button_pressed = True
					break
				elif ex_black_pawn_6 == True and button_pressed_xy[0] in range(black_pawn_pos_6[0], (black_pawn_pos_6[0] + 100)) and button_pressed_xy[1] in range(black_pawn_pos_6[1], (black_pawn_pos_6[1] + 100)):
					play_pers = "black_pawn_6"
					button_pressed = True
					break
				elif ex_black_pawn_7 == True and button_pressed_xy[0] in range(black_pawn_pos_7[0], (black_pawn_pos_7[0] + 100)) and button_pressed_xy[1] in range(black_pawn_pos_7[1], (black_pawn_pos_7[1] + 100)):
					play_pers = "black_pawn_7"
					button_pressed = True
					break
				elif ex_black_pawn_8 == True and button_pressed_xy[0] in range(black_pawn_pos_8[0], (black_pawn_pos_8[0] + 100)) and button_pressed_xy[1] in range(black_pawn_pos_8[1], (black_pawn_pos_8[1] + 100)):
					play_pers = "black_pawn_8"
					button_pressed = True
					break

		if white_pawn_gr == True and white_pawn_gr_aus == False and pawn_gr == True:
			white_pawn_gr_aus = True
			display.blit(pygame.transform.scale(chess_field, (800, 800)), (0, 0))
			display.blit(pygame.transform.scale(right_field, (900, 800)), (800, 0))
			if ex_white_king == False:
				white_king_pos = [850, 50]
				display.blit(pygame.transform.scale(white_king, (int(size_x), int(size_y))), (white_king_pos))
			if ex_white_queen == False:
				white_queen_pos = [950, 50]
				display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_queen_pos))
			if ex_white_rook_1 == False:
				white_rook_pos_1 = [1050, 50]
				display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_rook_pos_1))
			if ex_white_rook_2 == False:
				white_rook_pos_2 = [1150, 50]
				display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_rook_pos_2))
			if ex_white_bishop_1 == False:
				white_bishop_pos_1 = [1250, 50]
				display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_bishop_pos_1))
			if ex_white_bishop_2 == False:
				white_bishop_pos_2 = [1350, 50]
				display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_bishop_pos_2))
			if ex_white_knight_1 == False:
				white_knight_pos_1 = [1450, 50]
				display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_knight_pos_1))
			if ex_white_knight_2 == False:
				white_knight_pos_2 = [1550, 50]
				display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_knight_pos_2))
			if ex_white_pawn_1 == False:
				white_pawn_pos_1 = [850, 150]
				display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_1))
			if ex_white_pawn_2 == False:
				white_pawn_pos_2 = [950, 150]
				display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_2))
			if ex_white_pawn_3 == False:
				white_pawn_pos_3 = [1050, 150]
				display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_3))
			if ex_white_pawn_4 == False:
				white_pawn_pos_4 = [1150, 150]
				display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_4))
			if ex_white_pawn_5 == False:
				white_pawn_pos_5 = [1250, 150]
				display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_5))
			if ex_white_pawn_6 == False:
				white_pawn_pos_6 = [1350, 150]
				display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_6))
			if ex_white_pawn_7 == False:
				white_pawn_pos_7 = [1450, 150]
				display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_7))
			if ex_white_pawn_8 == False:
				white_pawn_pos_8 = [1550, 150]
				display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_8))

			if ex_black_king == False:
				black_king_pos = [850, 550]
				display.blit(pygame.transform.scale(black_king, (int(size_x), int(size_y))), (black_king_pos))
			if ex_black_queen == False:
				black_queen_pos = [950, 550]
				display.blit(pygame.transform.scale(black_queen, (int(size_x), int(size_y))), (black_queen_pos))
			if ex_black_rook_1 == False:
				black_rook_pos_1 = [1050, 550]
				display.blit(pygame.transform.scale(black_rook, (int(size_x), int(size_y))), (black_rook_pos_1))
			if ex_black_rook_2 == False:
				black_rook_pos_2 = [1150, 550]
				display.blit(pygame.transform.scale(black_rook, (int(size_x), int(size_y))), (black_rook_pos_2))
			if ex_black_bishop_1 == False:
				black_bishop_pos_1 = [1250, 550]
				display.blit(pygame.transform.scale(black_bishop, (int(size_x), int(size_y))), (black_bishop_pos_1))
			if ex_black_bishop_2 == False:
				black_bishop_pos_2 = [1350, 550]
				display.blit(pygame.transform.scale(black_bishop, (int(size_x), int(size_y))), (black_bishop_pos_2))
			if ex_black_knight_1 == False:
				black_knight_pos_1 = [1450, 550]
				display.blit(pygame.transform.scale(black_knight, (int(size_x), int(size_y))), (black_knight_pos_1))
			if ex_black_knight_2 == False:
				black_knight_pos_2 = [1550, 550]
				display.blit(pygame.transform.scale(black_knight, (int(size_x), int(size_y))), (black_knight_pos_2))
			if ex_black_pawn_1 == False:
				black_pawn_pos_1 = [850, 650]
				display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_1))
			if ex_black_pawn_2 == False:
				black_pawn_pos_2 = [950, 650]
				display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_2))
			if ex_black_pawn_3 == False:
				black_pawn_pos_3 = [1050, 650]
				display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_3))
			if ex_black_pawn_4 == False:
				black_pawn_pos_4 = [1150, 650]
				display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_4))
			if ex_black_pawn_5 == False:
				black_pawn_pos_5 = [1250, 650]
				display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_5))
			if ex_black_pawn_6 == False:
				black_pawn_pos_6 = [1350, 650]
				display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_6))
			if ex_black_pawn_7 == False:
				black_pawn_pos_7 = [1450, 650]
				display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_7))
			if ex_black_pawn_8 == False:
				black_pawn_pos_8 = [1550, 650]
				display.blit(pygame.transform.scale(black_pawn, (int(size_x), int(size_y))), (black_pawn_pos_8))

			if ex_white_king == True:
				display.blit(pygame.transform.scale(white_king, (int(size_x), int(size_y))), (white_king_pos))
			if ex_white_queen == True:
				display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_queen_pos))
			if ex_white_rook_1 == True:
				display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_rook_pos_1))
			if ex_white_rook_2 == True:
				display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_rook_pos_2))
			if ex_white_bishop_1 == True:
				display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_bishop_pos_1))
			if ex_white_bishop_2 == True:
				display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_bishop_pos_2))
			if ex_white_knight_1 == True:
				display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_knight_pos_1))
			if ex_white_knight_2 == True:
				display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_knight_pos_2))
			if ex_white_pawn_1 == True:
				if gr_white_pawn_1 == False:
					display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_1))
				else:
					if pt_white_pawn_1 == "white_queen":
						display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_pawn_pos_1))
					elif pt_white_pawn_1 == "white_rook":
						display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_pawn_pos_1))
					elif pt_white_pawn_1 == "white_bishop":
						display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_pawn_pos_1))
					elif pt_white_pawn_1 == "white_knight":
						display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_pawn_pos_1))
			if ex_white_pawn_2 == True:
				if gr_white_pawn_2 == False:
					display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_2))
				else:
					if pt_white_pawn_2 == "white_queen":
						display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_pawn_pos_2))
					elif pt_white_pawn_2 == "white_rook":
						display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_pawn_pos_2))
					elif pt_white_pawn_2 == "white_bishop":
						display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_pawn_pos_2))
					elif pt_white_pawn_2 == "white_knight":
						display.blit(pygame.transform.scale(white_knight, (int(size_x), int(size_y))), (white_pawn_pos_2))
			if ex_white_pawn_3 == True:
				if gr_white_pawn_3 == False:
					display.blit(pygame.transform.scale(white_pawn, (int(size_x), int(size_y))), (white_pawn_pos_3))
				else:
					if pt_white_pawn_3 == "white_queen":
						display.blit(pygame.transform.scale(white_queen, (int(size_x), int(size_y))), (white_pawn_pos_3))
					elif pt_white_pawn_3 == "white_rook":
						display.blit(pygame.transform.scale(white_rook, (int(size_x), int(size_y))), (white_pawn_pos_3))
					elif pt_white_pawn_3 == "white_bishop":
						display.blit(pygame.transform.scale(white_bishop, (int(size_x), int(size_y))), (white_pawn_pos_3))
					elif pt_white_pawn_3 == "white_knight":
