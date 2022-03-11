from cicle.game.casting.actor import Actor
from cicle.game.shared.point import Point
import constants


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, playertype):
        super().__init__()
        self._points = 0
        self.add_points(0)
        if playertype == "player2":
            self.set_position(Point(constants.MAX_X - (constants.CELL_SIZE * 6), 0))

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")