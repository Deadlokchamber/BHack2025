
class gameState:
    state=2
    
    def __init__(self,stateList):
        self.states=stateList
    
    
    def drawState(self,window,player,bgImage):
        self.states[gameState.state].update(window,player,bgImage)
