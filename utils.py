
import math

class Utils:

    @staticmethod
    def ballsToOvers(balls):
        if balls >0:
            return str(math.floor(balls/6)) + "." +str(balls % 6)
        else:
            return "0.0"
        