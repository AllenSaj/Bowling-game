class Frame:
    def __init__ (self):
        self.rolls = []
        self.pins = 10

    def addRoll (self, pins):
        print('rolled', pins, '/', self.pins)

        self.pins = self.pins - pins
        self.rolls.append(pins)

    def score(self):
        return sum(self.rolls)
        
    def isStrike(self):
        if len(self.rolls) == 1 and self.score() == 10:
            return True
    
    def isSpare(self):
        if len(self.rolls) == 2 and self.score() == 10:
            return True
    
    def isFinished(self):
        return len(self.rolls) == 2 or self.pins == 0
    
    def setPins(self, pins):
        self.pins = pins

