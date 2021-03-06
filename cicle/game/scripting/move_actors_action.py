from cicle.game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor
# 4) call the grow_tail() on each movement
class MoveActorsAction(Action):

    def execute(self, cast, script):
        
        actors = cast.get_all_actors()
        rider = cast.get_first_actor("Riders")
        rider1 = cast.get_second_actor("Riders")

        for actor in actors:
            actor.move_next()
            