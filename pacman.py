import pygame, sys, random

# Started on August 3rd, 2020, at 8:42 AM, finished on 0/00/2020 at 00:00 _M. 

""" TO DO:
	- Add Cherry Fruit
	- Add Enemy
"""

pygame.init()

# Define variables.
backgroundColour = (0, 0, 0)

runLoop = True
tileSize = 30
ROWS =  11
COLS = 10
w_width = tileSize + (tileSize * COLS)
w_height = tileSize + (tileSize * ROWS) + tileSize

screen = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("Pacman")

# Define mouse event variable.
cursorEvent = pygame.event.poll()

# Set up the game clock.
clock = pygame.time.Clock()

# Reusable function to return desired text object, which can be displayed.
def drawText(labelText, xPos, yPos, labelType, size):
	if labelType == "gray":
		color = (255, 255, 255)
	else: 
		color = (120, 111, 102)

	font = pygame.font.Font('freesansbold.ttf', size)
	text = font.render(labelText, True, color)
	textRect = text.get_rect()
	#textRect.center = (xPos // 2, yPos // 2)
	textRect.center = (int(xPos), int(yPos))
	return screen.blit(text, textRect)


def positionInArray(coordinates): # Pass in coordinates as array: [c, r]
	colPos = coordinates[0]
	rowPos = coordinates[1]

	if colPos >= 0 and colPos <= COLS-1 and rowPos >= 0 and rowPos <= ROWS-1:
		return True
	else: return False


def getNewCoords(coordinates, direction): # Return new coordinates based on direction
	newC = coordinates[0] + direction[0]
	newR = coordinates[1] + direction[1]
	newCoords = [newC, newR]

	return newCoords


def getDirList(coordinates):
	global wallArray

	possDirList = [] #[[0, -1], [0, 1], [-1, 0], [1, 0]] # U, D, L, R

	if positionInArray(coordinates):
		# Cannot check outer layer if this block IS the boundary.

		if wallArray[coordinates[1]][coordinates[0]].topWall == False:
			if coordinates[1] > 0:
				if wallArray[coordinates[1]-1][coordinates[0]].botWall == False:
					possDirList.append([0, -1])

		if wallArray[coordinates[1]][coordinates[0]].botWall == False:
			if coordinates[1] < ROWS-1:
				if wallArray[coordinates[1]+1][coordinates[0]].topWall == False:
					possDirList.append([0, 1])
				
		if wallArray[coordinates[1]][coordinates[0]].lefWall == False:
			if coordinates[0] < COLS-1:
				if wallArray[coordinates[1]][coordinates[0]+1].rigWall == False:
					possDirList.append([-1, 0])			
			
		if wallArray[coordinates[1]][coordinates[0]].rigWall == False:
			if coordinates[0] > 0:
				if wallArray[coordinates[1]][coordinates[0]-1].lefWall == False:
					possDirList.append([1, 0])

	return possDirList


def testForEdge(coordinates): # Pass in corrdinates as array: [c, r]
	colPos = coordinates[0]
	rowPos = coordinates[1]

	# Return true if this position is inside the array.
	if colPos < 0 or colPos > COLS-1 or rowPos < 0 or rowPos > ROWS-1:
		return False
	else:
		return True


def getOppositeDirection(direction):
	for elem in range(2):
		direction[elem] = -1 * int(direction[elem])
	
	return direction


# Return the distance between two coordinates.
def getDistance(coordinates, target):
	xDis = abs(coordinates[0] - target[0])
	yDis = abs(coordinates[1] - target[1])

	if xDis > yDis:
		return xDis
	elif yDis >= xDis:
		return yDis


def pacmanWalls(array):
	array[0][0].topWall = True
	array[0][0].lefWall = True
	array[0][1].topWall = True
	array[0][1].botWall = True
	array[0][2].topWall = True
	array[0][3].topWall = True
	array[0][3].botWall = True
	array[0][4].topWall = True
	array[0][4].rigWall = True
	array[0][5].topWall = True
	array[0][5].lefWall = True
	array[0][6].topWall = True
	array[0][6].botWall = True
	array[0][7].topWall = True
	array[0][8].topWall = True
	array[0][8].botWall = True
	array[0][9].topWall = True
	array[0][9].rigWall = True

	array[1][0].lefWall = True
	array[1][0].rigWall = True
	array[1][1].lefWall = True
	array[1][1].rigWall = True
	array[1][1].topWall = True
	array[1][1].botWall = True
	array[1][2].lefWall = True
	array[1][2].rigWall = True
	array[1][3].lefWall = True
	array[1][3].rigWall = True
	array[1][3].topWall = True
	array[1][3].botWall = True
	array[1][4].lefWall = True
	array[1][4].rigWall = True
	array[1][5].lefWall = True
	array[1][5].rigWall = True
	array[1][6].lefWall = True
	array[1][6].rigWall = True
	array[1][6].topWall = True
	array[1][6].botWall = True
	array[1][7].lefWall = True
	array[1][7].rigWall = True
	array[1][8].lefWall = True
	array[1][8].rigWall = True
	array[1][8].topWall = True
	array[1][8].botWall = True
	array[1][9].lefWall = True
	array[1][9].rigWall = True

	array[2][0].lefWall = True
	array[2][1].topWall = True
	array[2][1].botWall = True
	array[2][3].topWall = True
	array[2][4].botWall = True
	array[2][5].botWall = True
	array[2][6].topWall = True
	array[2][8].topWall = True
	array[2][8].botWall = True
	array[2][9].rigWall = True

	array[3][0].lefWall = True
	array[3][0].botWall = True
	array[3][1].topWall = True
	array[3][1].botWall = True
	array[3][2].rigWall = True
	array[3][3].lefWall = True
	array[3][3].botWall = True
	array[3][4].rigWall = True
	array[3][4].topWall = True
	array[3][5].lefWall = True
	array[3][5].topWall = True
	array[3][6].botWall = True
	array[3][6].rigWall = True
	array[3][7].lefWall = True
	array[3][8].botWall = True
	array[3][8].topWall = True
	array[3][9].rigWall = True
	array[3][9].botWall = True

	array[4][0].topWall = True
	array[4][0].botWall = True
	array[4][1].topWall = True
	array[4][1].botWall = True
	array[4][1].rigWall = True
	array[4][2].lefWall = True
	array[4][2].rigWall = True
	array[4][3].topWall = True
	array[4][3].lefWall = True
	array[4][4].botWall = True
	array[4][5].botWall = True
	array[4][6].topWall = True
	array[4][6].rigWall = True
	array[4][7].rigWall = True
	array[4][7].lefWall = True
	array[4][8].lefWall = True
	array[4][8].topWall = True
	array[4][8].botWall = True
	array[4][9].topWall = True
	array[4][9].botWall = True

	array[5][0].topWall = True
	array[5][0].botWall = True
	array[5][1].topWall = True
	array[5][1].botWall = True

	array[5][3].rigWall = True
	array[5][4].lefWall = True

	array[5][4].topWall = True
	array[5][4].botWall = True
	array[5][5].topWall = True
	array[5][5].botWall = True

	array[5][5].rigWall = True
	array[5][6].lefWall = True

	array[5][8].topWall = True
	array[5][8].botWall = True
	array[5][9].botWall = True
	array[5][9].topWall = True


	array[6][0].botWall = True
	array[6][0].topWall = True
	array[6][1].topWall = True
	array[6][1].botWall = True
	array[6][1].rigWall = True
	array[6][2].lefWall = True
	array[6][4].topWall = True
	array[6][4].botWall = True
	array[6][5].topWall = True
	array[6][5].botWall = True

	array[6][6].rigWall = True
	array[6][7].lefWall = True
	array[6][2].rigWall = True
	array[6][3].lefWall = True

	array[6][7].rigWall = True
	array[6][8].topWall = True
	array[6][8].botWall = True
	array[6][8].lefWall = True
	array[6][9].topWall = True
	array[6][9].botWall = True



	array[7][0].lefWall = True
	array[7][0].topWall = True
	array[7][1].topWall = True
	array[7][1].botWall = True
	array[7][3].botWall = True
	array[7][4].topWall = True
	array[7][4].rigWall = True
	array[7][5].topWall = True
	array[7][5].lefWall = True
	array[7][6].botWall = True
	array[7][8].topWall = True
	array[7][8].botWall = True
	array[7][9].rigWall = True
	array[7][9].topWall = True



	array[8][0].lefWall = True
	array[8][0].botWall = True
	array[8][1].topWall = True
	array[8][1].rigWall = True
	array[8][2].lefWall = True
	array[8][3].topWall = True
	array[8][4].botWall = True
	array[8][5].botWall = True
	array[8][6].topWall = True
	array[8][7].rigWall = True
	array[8][8].topWall = True
	array[8][8].lefWall = True
	array[8][9].botWall = True
	array[8][9].rigWall = True

	array[9][0].lefWall = True
	array[9][0].topWall = True
	array[9][1].botWall = True
	array[9][2].botWall = True
	array[9][2].rigWall = True
	array[9][3].botWall = True
	array[9][3].lefWall = True
	array[9][4].topWall = True
	array[9][4].rigWall = True
	array[9][5].topWall = True
	array[9][5].lefWall = True
	array[9][6].botWall = True
	array[9][6].rigWall = True
	array[9][7].lefWall = True
	array[9][7].botWall = True
	array[9][8].botWall = True
	array[9][9].rigWall = True
	array[9][9].topWall = True


	array[10][0].lefWall = True
	array[10][0].botWall = True
	array[10][1].botWall = True
	array[10][1].topWall = True
	array[10][2].botWall = True
	array[10][2].topWall = True
	array[10][3].botWall = True
	array[10][3].topWall = True
	array[10][4].botWall = True
	array[10][5].botWall = True
	array[10][6].botWall = True
	array[10][6].topWall = True
	array[10][7].botWall = True
	array[10][7].topWall = True
	array[10][8].botWall = True
	array[10][8].botWall = True
	array[10][8].topWall = True
	array[10][9].botWall = True
	array[10][9].rigWall = True


def pacmanFood(array):
	array[1][1].containsFood = False
	array[1][3].containsFood = False
	array[1][6].containsFood = False
	array[1][8].containsFood = False
	array[5][4].containsFood = False
	array[5][5].containsFood = False
	array[5][5].containsFood = False
	array[4][0].containsFood = False
	array[4][1].containsFood = False
	array[4][8].containsFood = False
	array[4][9].containsFood = False
	array[6][0].containsFood = False
	array[6][1].containsFood = False
	array[6][8].containsFood = False
	array[6][9].containsFood = False
	# array[5][5].containsFood = False
	# array[5][5].containsFood = False
	# array[5][5].containsFood = False
	# array[5][5].containsFood = False
	# array[5][5].containsFood = False


class gameBlock:
	def __init__(self):
		self.topWall = False
		self.botWall = False
		self.rigWall = False
		self.lefWall = False
		self.containsFood = True
		self.containsFruit = False


wallArray = []

# Initialize the wallArray with block/cell objects.
for r in range(ROWS):
	thisRow = []
	for c in range(COLS):
		thisRow.append(gameBlock()) # Create the object and pass coordinates to object.

	wallArray.append(thisRow)

pacmanWalls(wallArray)
pacmanFood(wallArray)

class player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.score = 0

		initialPossibilites = getDirList([self.x, self.y])
		self.direction = random.choice(initialPossibilites)

	def updatePosition(self, direction):
		global wallArray
		
		newPosition = getNewCoords([self.x, self.y], direction)

		self.eatFood(wallArray)

		if self.x == 9 and self.y == 5 and direction == [1, 0]: 
			self.x = 0
			return

		if self.x == 0 and self.y == 5 and direction == [-1, 0]: 
			self.x = 9
			return
								
		if testForEdge(newPosition):
			if direction == [0,1]:
				if wallArray[self.y][self.x].botWall == False and wallArray[newPosition[1]][newPosition[0]].topWall == False:
					self.y = self.y + 1
			elif direction == [0,-1]:
				if wallArray[self.y][self.x].topWall == False and wallArray[newPosition[1]][newPosition[0]].botWall == False:
					self.y = self.y - 1
			elif direction == [1,0]:
				if wallArray[self.y][self.x].rigWall == False and wallArray[newPosition[1]][newPosition[0]].lefWall == False:
						self.x = self.x + 1
			elif direction == [-1,0]:
				if wallArray[self.y][self.x].lefWall == False and wallArray[newPosition[1]][newPosition[0]].rigWall == False:
					self.x = self.x - 1

	def eatFood(self, array):
		if array[self.y][self.x].containsFood == True:
			self.score += 1
			array[self.y][self.x].containsFood = False

Player = player(0, 0 )

class ghost:
	def __init__(self):
		self.x = 5
		self.y = 6
		self.color = (0, 255, 200)

	def draw(self, lineMarg, tileSize):
		pygame.draw.rect(screen, self.color, (int((self.x * tileSize) -lineMarg+4), int((self.y * tileSize) -lineMarg+4), tileSize-lineMarg/2, tileSize-lineMarg/2))

	def updatePosition(self):
		global wallArray

		dirList = getDirList([self.x-1, self.y-1]) # For some reason, I needed to write -1 for index format

		direction = random.choice(dirList)

		self.x = self.x + direction[0]
		self.y = self.y + direction[1]

enemiesList = []
enemiesList.append(ghost())
enemiesList.append(ghost())
enemiesList.append(ghost())



def drawWallArray(lineSize, lineMarg, dif, lineColor, tileSize):
	global wallArray

	for row in range(ROWS):
		for col in range(COLS):
			x = col*tileSize+tileSize
			y = row*tileSize+tileSize
			if wallArray[row][col].topWall == True:
				pygame.draw.line(screen, lineColor, (int(x-lineMarg)+dif, int(y-lineMarg+dif)), (int(x+lineMarg-dif), int(y-lineMarg)+dif), lineSize)
			if wallArray[row][col].botWall == True:
				pygame.draw.line(screen, lineColor, (int(x-lineMarg+dif), int(y+lineMarg-dif)), (int(x+lineMarg-dif), int(y+lineMarg-dif)), lineSize)
			if wallArray[row][col].rigWall == True:
				pygame.draw.line(screen, lineColor, (int(x+lineMarg-dif), int(y-lineMarg+dif)), (int(x+lineMarg-dif), int(y+lineMarg-dif)), lineSize)
			if wallArray[row][col].lefWall == True:
				pygame.draw.line(screen, lineColor, (int(x-lineMarg+dif), int(y-lineMarg+dif)), (int(x-lineMarg+dif), int(y+lineMarg-dif)), lineSize)

			if wallArray[row][col].containsFood == True:
				pygame.draw.circle(screen, (253, 167, 147), (int(x), int(y)), 3)


def drawPlayer(lineMarg, tileSize):
	x = Player.x*tileSize+tileSize
	y = Player.y*tileSize+tileSize
	playerSize = 22
	playerX = x-lineMarg+4
	playerY = y-lineMarg+4

	pygame.draw.rect(screen, (216, 255, 0), (int(playerX), int(playerY), int(playerSize) ,int(playerSize)))

	indicatorX = playerX-2 + (playerSize/2) + (Player.direction[0]*5)
	indicatorY = playerY-2 + (playerSize/2) + (Player.direction[1]*5)
	pygame.draw.rect(screen, (0, 0, 0), (int(indicatorX), int(indicatorY), 5, 5))


def drawEnemies(lineMarg, tileSize):
	for obj in enemiesList:
		obj.draw(lineMarg, tileSize)


def draw():
	lineSize = 1
	lineMarg = tileSize/2
	dif = 1
	lineColor = (0, 0, 230)

	drawWallArray(lineSize, lineMarg, dif, lineColor, tileSize)

	drawPlayer(lineMarg, tileSize)
	
	drawEnemies(lineMarg, tileSize)
	# drawText(str("Press: (SPACE) to respawn ghost."), w_width/2, w_height-tileSize+10, "gray", 10)
	# for obj in enemiesList:
	# 	x = obj.x*tileSize+tileSize
	# 	y = obj.y*tileSize+tileSize
	# 	pygame.draw.rect(screen, obj.color, (int(x-lineMarg+4), int(y-lineMarg+4), 22, 22))

	drawText("Score: {}".format(Player.score), w_width/2, w_height-tileSize+10, "gray", 10)


def updateDisplay():
	global runLoop
	timeTracker = 0

	while runLoop:
		timeTracker += 1
		mouseX, mouseY = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					sys.exit()

				# if event.key == pygame.K_SPACE:
				# 	for obj in enemiesList:
				# 		obj.updatePosition()

				elif event.key == pygame.K_UP:
					if [0, -1] in getDirList([Player.x, Player.y]):
						Player.direction = [0, -1]
				elif event.key == pygame.K_DOWN:
					if [0, 1] in getDirList([Player.x, Player.y]):
						Player.direction = [0, 1]
				elif event.key == pygame.K_RIGHT:
					if [1, 0] in getDirList([Player.x, Player.y]):
						Player.direction = [1, 0]
				elif event.key == pygame.K_LEFT:
					if [-1, 0] in getDirList([Player.x, Player.y]):
						Player.direction = [-1, 0]


		# Do not update the images every single frame, however, key events are detected every frame.
		if timeTracker % 10 == 0:
			
			screen.fill(backgroundColour)
			draw()
			
		if timeTracker % 20 == 0:
			Player.updatePosition(Player.direction)

			for obj in enemiesList:
				obj.updatePosition()

		pygame.display.update()

		clock.tick(60)

updateDisplay()