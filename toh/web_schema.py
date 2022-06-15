# ---------------------------------------------------------------------------------------
# The Pydantic schema to define the JSON WebAPI
# ----------------------------------------------------------------------------------------

from typing import List, Optional
from pydantic import BaseModel

# ----------------------------------------------------------------------------------------
# Input
# ----------------------------------------------------------------------------------------

class Peg(BaseModel):
    pegid: str

class Disk(BaseModel):
    diskid: int

class InitOn(BaseModel):
    diskid: int
    pegid: str

class GoalOn(BaseModel):
    diskid: int
    pegid: str

class Instance(BaseModel):
    moves: int
    pegs: List[Peg]
    disks: List[Disk]
    init: List[InitOn]
    goal: List[GoalOn]

# ----------------------------------------------------------------------------------------
# Output
# ----------------------------------------------------------------------------------------

class Move(BaseModel):
    diskid: int
    pegid: str
    time: int

class Solution(BaseModel):
    moves: List[Move]

class Result(BaseModel):
    solution: Optional[Solution]
    errors: Optional[List[str]]
