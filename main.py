import pygame
import random
import math
import numpy
#import AI

global ROWS, COLS, SQUARE_SIZE, HEIGHT, WIDTH
ROWS = COLS = 3
SQUARE_SIZE = 75
WIDTH = COLS * SQUARE_SIZE
HEIGHT = ROWS * SQUARE_SIZE

global RED, BLUE, WHITE, BLACK
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

global MODE
MODE = input("PVP or PVC: ").lower()

class Game:
	
	def __init__(self, screen):
		
		self.board = numpy.zeroes((COLS, ROWS), dtype=tuple)
		self.player = random.choice( [RED, BLUE] )
		
		self.screen = screen
		self.Graphics = Graphics(screen)
		
		self.Graphics.drawBoard(self.board)
	
	def free_squares(self, board):
		
		available_squares = []
		
		for row in range(ROWS):
			for col in range(COLS):
				
				if board[row][col] == 0:
					available_squares.append((row, col))
					
		return free_squares
	
	def make_move(self, row, col):
		
		if (row, col) in self.free_squares(board) and self.winner(self.board, RED) == None and self.winner(self.board, BLUE) == None:
			self.board[row][col] = self.player
			self.changePlayer()
			
		self.Graphics.drawBoard(self.board)
			
	def changePlayer(self):
		
		if self.player == RED:
			self.player = BLUE
			
		else:
			self.player = RED
			
	def winner(self, board, player):
		
		if self.free_squares(board) == 0:
			return -1
		
		for row in range(ROWS):
			if self.in_a_row(board[row], player) == 3:
				return True
				
		for col in range(COL):
			if self.in_a_row( numpy.transpose(board)[col], player ) == 3:
				return True
			
		if self.in_a_row( [board[i][i] for i in range(ROWS)], player ):
			return True
		
		if self.in_a_row( [board[i][COL - 1 - i] for i in range(COL)], player ):
			return True
		
	def in_a_row(self, window, player):
		return window.count(player)
	
	def print_board(self):
		for row in range(self.board):
			print(row)
			
	def __repr__(self):
		return {"board" : self.board, "player" : self.player}
	
class Graphics:
	
	PADDING = 5
	
	def __init__(self, screen):
		self.screen = screen
		self.radius = SQUARE_SIZE // 2 - PADDING
		
	def drawBoard(self, board):
		
		pygame.draw.line(self.screen, WHITE, (0, HEIGHT // 3), (WIDTH, HEIGHT // 3), PADDING)
		pygame.draw.line(self.screen, WHITE, (0, 2 * HEIGHT // 3), (WIDTH, 2 * HEIGHT // 3), PADDING)
		pygame.draw.line(self.screen, WHITE, (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), PADDING)
		pygame.draw.line(self.screen, WHITE, (2 * WIDTH // 3, 0), (2 * WIDTH // 3, HEIGHT), PADDING)
		
		for row in range(ROWS):
			for col in range(COLS):
				
				pos = ( col * SQUARE_SIZE + SQUARE_SIZE // 2, 
					    row * SQUARE_SIZE + SQUARE_SIZE // 2 )
				
				board[row][col] == RED:
					pygame.draw.circle(self.screen, RED, pos, self.radius)
					
				board[row][col] == BLUE:
					pygame.draw.circle(self.screen, BLUE, pos, self.radius)
					
	def blank_board(self, bgcolor):
		self.screen.fill(bgcolor)
		
	def text(self, text, pos, color, size):
		pass
	
	@staticmethod
	def update_screen(fps):
		pygame.display.update()
		pygame.time.Clock().tick(fps)
		
def main():
	
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	
	game = Game(window)
	graphics = Graphics(window)
	
	running = True
	winner = None
	
	while running:
		
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				running = False
				
			if event.type == pygame.MOUSEBUTTONDOWN:
				
				col, row = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE
				game.make_move(row, col)
				
				winner = "RED" * game.winner(game.board, RED) + "BLUE" * game.winner(game.board, BLUE)
				
		graphics.update_screen(30)
		
		if winner != None:
			pygame.time.Clock().wait(2000)
			running = False
		
	print("GOODBYE")
	pygame.quit()
	
main()
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
