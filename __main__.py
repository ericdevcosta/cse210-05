import constants

from cicle.game.casting.cast import Cast
from cicle.game.casting.coin import coin
from cicle.game.casting.score import Score
from cicle.game.casting.rider import rider
from cicle.game.scripting.script import Script
from cicle.game.scripting.control_actors_action import ControlActorsAction
from cicle.game.scripting.move_actors_action import MoveActorsAction
from cicle.game.scripting.handle_collisions_action import HandleCollisionsAction
from cicle.game.scripting.draw_actors_action import DrawActorsAction
from cicle.game.directing.director import Director
from cicle.game.services.keyboard_service import KeyboardService
from cicle.game.services.video_service import VideoService
from cicle.game.shared.color import Color
from cicle.game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("Coins", coin())
    cast.add_actor("Riders", rider("player1"))
    cast.add_actor("scores", Score("player1"))
    cast.add_actor("Riders", rider("player2"))
    cast.add_actor("scores", Score("player2"))
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()