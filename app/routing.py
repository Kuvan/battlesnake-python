import json

class brains(name):
        def __init__(self,name):
                self.mName = name

        def start(self, data):
                self.mInfo = json.load(data)
                self.mWidth = self.mInfo["width"]
                self.mHeight = self.mInfo["height"]
                self.mGameID = self.mInfo["game_id"]
                print self.mGameID
                self.Board[self.mWidth,self.mHeight]
                                
        def move(self, data):
                                
                self.mInfo = json.load(data)
                self.mTurn = self.mInfo["turn"]
                self.mBoard = self.mInfo["board"]
                self.mSnakes = self.mInfo["snakes"]
                self.mFood = self.mInfo["food"]
                count = 0
                for x in self.mSnakes:
                        if x.name == self.mName:
                                break
                        count = count + 1
