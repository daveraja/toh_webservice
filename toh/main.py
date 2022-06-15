# ------------------------------------------------------------------------------
# The Tower of Hanoi FastAPI app. To start the web-service run:
#
#     uvicorn toh.main:app --reload
#
# ------------------------------------------------------------------------------

from typing import Tuple
from fastapi import FastAPI
from fastapi.logger import logger
import logging
import importlib.resources as ir
from pathlib import Path
from clorm import FactBase
from clorm.clingo import Control

from . import asp_schema as asp
from . import web_schema as web

# ------------------------------------------------------------------------------
# Globals
# ------------------------------------------------------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = FastAPI()

# ------------------------------------------------------------------------------
# Support functions
# ------------------------------------------------------------------------------
def process_instance(instance: web.Instance) -> Tuple[FactBase, int]:
    fb = FactBase()
    fb.add([asp.Peg(pegid=x.pegid) for x in instance.pegs])
    fb.add([asp.Disk(diskid=x.diskid) for x in instance.disks])
    fb.add([asp.InitOn(diskid=x.diskid, pegid=x.pegid) for x in instance.init])
    fb.add([asp.GoalOn(diskid=x.diskid, pegid=x.pegid) for x in instance.goal])
    return fb, instance.moves

def return_solution(fb: FactBase) -> web.Solution:
    return web.Solution(moves=list(
        fb.query(asp.Move).
        order_by(asp.Move.time).
        select(lambda m: web.Move(diskid=m.diskid, pegid=m.pegid, time=m.time)).
        all()))

def get_tohE():
    try:
        base_resource = ir.files('toh.encodings')
        with ir.as_file(base_resource) as base:
            encoding_file = base.joinpath("tohE.lp")
            if encoding_file.is_file():
                return encoding_file
    except Exception:
        return Path(__file__).resolve().parent.parent / 'encodings' / 'tohE.lp'

def solve(fb: FactBase, moves) -> FactBase:
    try:
        encoding_file = get_tohE()
        logger.debug(f"ASP_ENCODINGS: using {encoding_file}")
        logger.debug(f"Searching for solution in {moves} moves for instance: {fb}")
        ctrl = Control(arguments=[f"--const=moves={moves}"], unifier=[asp.Move])
        ctrl.add_facts(fb)
        ctrl.load(str(encoding_file))
        ctrl.ground([("base", [])])
        with ctrl.solve(yield_=True) as sh:
            for m in sh:
                return m.facts(atoms=True)
    except Exception as e:
        raise RuntimeError(f"Processing error: {e}")
    raise RuntimeError("Problem is UNSAT")

# ------------------------------------------------------------------------------
# API endpoints
# ------------------------------------------------------------------------------

@app.post("/")
async def find_solution(instance : web.Instance) -> web.Result:
    try:
        fb, num_moves = process_instance(instance)
        return web.Result(solution=return_solution(solve(fb, num_moves)))
    except RuntimeError as e:
        errmsg = f"Failed to find a solution for {e}"
        logger.error(errmsg)
        return web.Result(errors=[errmsg])
    except Exception as e2:
        errmsg = f"{e2}"
        logger.error(errmsg)
        return web.Result(errors=[errmsg])

# ------------------------------------------------------------------------------
# main
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    raise RuntimeError('Cannot run modules')

