from src.block import fence


class homeStage:
    def __init__(self,houseCount):
        self.houseCount = houseCount
        self.fences = [fence(0, 544,0), fence(0, 640, 1)]

    def draw(self,win):
        win.fill((0,200,0))
