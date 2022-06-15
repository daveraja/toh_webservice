# ---------------------------------------------------------------------------------------
# The ASP Clorm schema for the input and output facts
# ----------------------------------------------------------------------------------------

from clorm import Predicate, ConstantStr

# ----------------------------------------------------------------------------------------
# Input facts
# ----------------------------------------------------------------------------------------

class Peg(Predicate):
    pegid: ConstantStr

class Disk(Predicate):
    diskid: int

class InitOn(Predicate, name="init_on"):
    diskid: int
    pegid: ConstantStr

class GoalOn(Predicate, name="goal_on"):
    diskid: int
    pegid: ConstantStr

# ----------------------------------------------------------------------------------------
# Output facts
# ----------------------------------------------------------------------------------------

class Move(Predicate):
    diskid: int
    pegid: ConstantStr
    time: int
