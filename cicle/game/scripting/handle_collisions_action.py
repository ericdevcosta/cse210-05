from cicle.game.casting.coin import coin
import constants
from cicle.game.casting.actor import Actor
from cicle.game.scripting.action import Action
from cicle.game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        score1 = cast.get_second_actor("scores")
        coin = cast.get_first_actor("Coins")
        rider = cast.get_first_actor("Riders")
        rider1 = cast.get_second_actor("Riders")
        head = rider.get_head()
        head1 = rider1.get_head()

        if head.get_position().equals(coin.get_position()):
            points = coin.get_points()
            rider.grow_tail(points)
            score.add_points(points)
            coin.reset()
            
        if head1.get_position().equals(coin.get_position()):
            points = coin.get_points()
            rider1.grow_tail(points)
            score1.add_points(points)
            coin.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        rider = cast.get_first_actor("Riders")
        rider1 = cast.get_second_actor("Riders")
        head = rider.get_segments()[0]
        head1 = rider1.get_segments()[0]
        segments = rider.get_segments()[1:]
        segments1 = rider1.get_segments()[1:]
        score = cast.get_first_actor("scores")
        score1 = cast.get_second_actor("scores")
        
        for segment in segments:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
            elif head1.get_position().equals(segment.get_position()):
                score.add_points(25)
                self._is_game_over = True
        
        for segment1 in segments1:
            if head1.get_position().equals(segment1.get_position()):
                self._is_game_over = True
            elif head.get_position().equals(segment1.get_position()):
                score1.add_points(25)
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
<<<<<<< Updated upstream
            rider1 = cast.get_first_actor("Riders")
            rider2 = cast.get_second_actor("Riders")
            segments1 = rider1.get_segments()
            segments2 = rider2.get_segments()
            coin = cast.get_first_actor("Coins")
=======
            score1 = cast.get_first_actor("scores")
            score2 = cast.get_second_actor("scores")
>>>>>>> Stashed changes

            if score1 > score2:
                rider = cast.get_first_actor("Riders")
                segments = rider.get_segments()
                coin = cast.get_first_actor("Coins")

                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                position = Point(x, y)

<<<<<<< Updated upstream
            for segment1 in segments1:
                segment1.set_color(constants.WHITE)
            for segment2 in segments2:
                segment2.set_color(constants.WHITE)
            coin.set_color(constants.WHITE)
=======
                message = Actor()
                message.set_text("Player 1 Wins!")
                message.set_position(position)
                cast.add_actor("messages", message)

                for segment in segments:
                    segment.set_color(constants.WHITE)
                coin.set_color(constants.WHITE)

            if score1 < score2:
                rider = cast.get_second_actor("Riders")
                segments = rider.get_segments()
                coin = cast.get_first_actor("Coins")

                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                position = Point(x, y)

                message = Actor()
                message.set_text("Player 2 Wins!")
                message.set_position(position)
                cast.add_actor("messages", message)

                for segment in segments:
                    segment.set_color(constants.WHITE)
                coin.set_color(constants.WHITE)
>>>>>>> Stashed changes
