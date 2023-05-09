import frame

class BowlingGame:
    def __init__ (self):
        self.frames = [frame.Frame() for i in range(10)]
        self.frameNumber = 0
        self.ballsToDouble = 0
        self.isFinished = False
        self.bonus = False

    def score(self):
        total = 0
        for i in range (0, self.frameNumber+1):
            total += self.frames[i].score()
        return total
        
    def rollBall(self,roll):
        currentFrame = self.frames[self.frameNumber]
        print('Frame', self.frameNumber+1, 'roll', len(currentFrame.rolls)+1)
        currentFrame.addRoll(roll)

        # Add bonus
        self.bonus = False
        if (self.ballsToDouble > 0):
            print("BONUS", roll, "ADDED")
            self.frames[self.frameNumber-1].rolls.append(roll)
            self.ballsToDouble -= 1
            self.bonus = True

        print('Total score: ', self.score())
        # Increment bonuses
        if (currentFrame.isStrike()):
            print("STRIKE!")
            self.ballsToDouble = 2
        elif (currentFrame.isSpare()):
            print("SPARE!")
            self.ballsToDouble += 1

        # Move game to next frame
        if (currentFrame.isFinished() and self.frameNumber < 9):
            self.frameNumber += 1

        if (self.frameNumber == 9 and self.ballsToDouble == 0):
            self.isFinished = True
        elif (self.frameNumber == 9 and self.ballsToDouble > 0): 
            self.ballsToDouble = 1
            currentFrame.setPins(10)

