import bottle
import json

class decesion():
	def __init__(self):
		print 'hello world'

	def realInit(self, info):
		
		self.game_id = info['game_id']
		self.width = info['width']
		self.height = info['height']
		self.direction = 'up'
		self.counter = 0
		return

	def findPos():
		xdex =0
		ydex= 0
		for x in self.board:
			ydex = 0
			for y in x:
				if y['state'] == 'head' and y['snake'] == 'golden_hamster':
					self.head = [xdec, ydex]
				ydex += 1
			xdex += 1

	def isSafe(self, direction):
		location = []
		if(direction == "up"):
			location.Append(self.head[0])
			location.Append((self.head[1] - 1))
		elif(direction == "down"):
			location.Append(self.head[0])
			location.Append((self.head[1] + 1))
		elif(direction == "right"):
			location.Append((self.head[0] + 1))
			location.Append(self.head[1])
		elif(direction == "left"):
			location.Append((self.head[0] - 1))
			location.Append(self.head[1])
		if(location[0] < 0 or location[1] < 0):
			return False
		elif(location[0] > self.width - 1 or location[1] > self.height - 1):
			return False
		elif(self.board[location[0]][location[1]]['state'] == "head"):
			return False
		elif(self.board[location[0]][location[1]]['state'] == "body"):
			return False
		elif(self.board[location[0]][location[1]]['state'] == "food"):
			return True
		elif(self.board[location[0]][location[1]]['state'] == "empy"):
			return True
		return True
	
	def move(self, info):
		
		self.board = info['board']
		self.snake = info['snakes']
		self.food = info['food']
		self.findPos();
		return self.findDanger();

	def findDanger(self):
		dirs = {'up': 0, 'down': 0, 'right': 0, 'left': 0}

		xdex =0
		ydex= 0

		for x in self.board:
			ydex = 0
			for y in x:
				if y['state'] == 'snake':
					if(ydex < self.head[1] ):
						dirs['up'] += 1
					elif(ydex > self.head[1]):
						dirs['down'] += 1;
					if(xdex < self.head[0] ):
						dirs['left'] += 1
					elif(xdex > self.head[0]):
						dirs['right'] += 1;
				ydex += 1	
			xdex += 1

		if (dirs['up']) > dirs['down'] and (dirs['up']) > dirs['right'] and (dirs['up']) > dirs['left'] and isSafe('up'):
			return 'up'
		if (dirs['down']) > dirs['up'] and (dirs['down']) > dirs['right'] and (dirs['down']) > dirs['left'] and isSafe('down'):
			return 'down'
		if (dirs['right'] > dirs['up']) and (dirs['right'] > dirs['down']) and (dirs['right']) > dirs['left'] and isSafe('right'):
			return 'right'
		if (dirs['left'] > dirs['up']) and (dirs['left'] > dirs['down']) and (dirs['left'] > dirs['right']) and isSafe('left'):
			return 'left'
		if(isSafe('right')):		
			return 'right'
		if(isSafe('left')):
			return 'left'
		if(isSafe('down')):
			return 'down'
		return 'up'

decide = decesion()

@bottle.get('/')
def index():
    return """
        <a href="https://github.com/sendwithus/battlesnake-python">
            battlesnake-python
        </a>
    """


@bottle.post('/start')
def start():
    data = bottle.request.json
    
    

    decide.realInit(data)

    return json.dumps({
        'name': 'golden_hamster',
        'color': '#00ff00',
        'head_url': 'http://battlesnake-python.herokuapp.com',
        'taunt': 'battlesnake-python!'
    })


@bottle.post('/move')
def move():
    data = bottle.request.json
    
    return json.dumps({
        'move': decide.move(),
        'taunt': 'Hoo-ray'
    })


@bottle.post('/end')
def end():
    data = bottle.request.json
	
    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
