import random
import constants
from cicle.game.casting.actor import Actor
from cicle.game.shared.point import Point


class coin(Actor):
    """
    A Coin that riders like to catch.
    
    The responsibility of coin is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the coin is worth.
    """
    def __init__(self):
        "Constructs a new coin."
        super().__init__()
        self._points = 0
        self.set_text("@")
        self.set_color(constants.RED)
        self.reset()
        
    def reset(self):
        """Selects a random position and points that the coin is worth."""
        self._points = random.randint(1, 8)
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        
    def get_points(self):
        """Gets the points the coin is worth.
        
        Returns:
            points (int): The points the coin is worth.
        """
        return self._points