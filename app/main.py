import bottle
import json

class decesion():
	return
	def __init__(self):
		print 'hello world'

	def initialize(self):
		print 'hello world'

	def realInit(self, data):
		info = json.load(data)
		self.game_id = info['game_id']
		self.width = info['width']
		self.height = info['height']
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
	def move(self):
		info = json.load(data)
		self.board = info['board']
		self.snake = info['snakes']
		self.food = info['food']
		direction = findDanger();

	def findDanger(self):
		up = 0
		down = 0
		right = 0
		left = 0

		xdex =0
		ydex= 0

		for x in self.board:
			ydex = 0
			for y in x:
				if y['state'] == 'snake':
					if(ydex < self.head[1] ):
						up += 1
					elif(ydex > self.head[1]):
						down -= 1;
					if(xdex < self.head[0] ):
						left += 1
					elif(xdex > self.head[0]):
						right -= 1;
				ydex += 1	
			xdex += 1
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
        'move': 'left',
        'taunt': 'battlesnake-python!'
    })


@bottle.post('/end')
def end():
    data = bottle.request.json
	
    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
