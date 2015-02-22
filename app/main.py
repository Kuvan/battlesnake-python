import bottle
import json

class decesion():
	def __init__(self):
		print 'hello world'

	def initialize(self):
		print 'hello world'

	def realInit(self, data):
		info = json.load(data)
		self.game_id = info['game_id']
		self.width = info['width']
		self.height = info['height']

	def findPos():
		xdex =0
		ydex= 0
		for x in self.board:
			ydex = 0
			for y in x:
				if y['state'] == 'head' and y['snake'] == 'golden_hamster':
					return [xdec, ydex]
				ydex += 1
			xdex += 1
	def move(self):
		info = json.load(data)
		self.board = info['board']
		self.snake = info['snakes']
		self.food = info['food']
		direction = findDanger();

	def findDanger(self):
		for x in self.board:
			for y in x:
				x =0
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
    
    

   # decide.realInit(data)

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
