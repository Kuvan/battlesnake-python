mport bottle
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
	
	def move(self):
		findDanger()

	def findDanger(self):
		

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
