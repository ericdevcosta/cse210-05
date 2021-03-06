import constants
from cicle.game.casting.actor import Actor
from cicle.game.shared.point import Point


class rider(Actor):
    """
    
    
    The responsibility of rider is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, playertype):
        super().__init__()
        self._segments = []
        self._playertype = playertype
        self._prepare_body()


    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        if self._playertype == "player1":
            color = constants.GREEN
        elif self._playertype == "player2":
            color = constants.BLUE
            
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position()#.add(offset)
            
            segment = Actor()
            segment.set_position(position)
            #segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        if self._playertype == "player1":   
            x = int(constants.MAX_X / 4)
            y = int(constants.MAX_Y / 2)

            for i in range(constants.RIDER_LENGTH):
                position = Point(x - i * constants.CELL_SIZE, y)
                velocity = Point(1 * constants.CELL_SIZE, 0)
                text = "8" if i == 3 else "#"
                color = constants.YELLOW if i == 3 else constants.GREEN
                
                segment = Actor()
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text(text)
                segment.set_color(color)
                self._segments.append(segment)
    
        elif self._playertype == "player2":
            x = int(constants.MAX_X / 4 + constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)

            for i in range(constants.RIDER_LENGTH):
                position = Point(x - i * constants.CELL_SIZE, y)
                velocity = Point(1 * constants.CELL_SIZE, 0)
                text = "8" if i == 0 else "#"
                color = constants.YELLOW if i == 3 else constants.BLUE
                
                segment = Actor()
                segment.set_position(position)
                segment.set_velocity(velocity)
                segment.set_text(text)
                segment.set_color(color)
                self._segments.append(segment)            