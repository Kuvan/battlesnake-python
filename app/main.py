import bottle
import json
#import routing

def function():
    print "Hello World"

class myClass():
    def __init__(self):
        print "this is a class"
        
function()
glow = myClass()
#name = "golden_hamster"
#smart = brains(name)

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
    #smart.start(data)
	
    return json.dumps({
        'name': 'golden_hamster',
        'color': '#00ff00',
        'head_url': 'http://battlesnake-python.herokuapp.com',
        'taunt': 'battlesnake-python!'
    })


@bottle.post('/move')
def move():
    data = bottle.request.json
    
    #return smart.move()


@bottle.post('/end')
def end():
    data = bottle.request.json
	
    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
