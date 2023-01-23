import pytest

from ..src.pathfind import pathfind, Coord
from ..src.exception import NoPossiblePath, OutOfBoundsError


def test_success_case():
    array = """. P . . .
. # # # .
. . . . .
. . Q . .
. . . . ."""

    shortest = pathfind(array=array, p=Coord(1, 0), q=Coord(2, 3))
    assert(shortest == 6)


def test_reverse():
    # By testing in reverse, all 4 directions of travel are covered. 
    array = """. P . . .
. # # # .
. . . . .
. . Q . .
. . . . ."""

    shortest = pathfind(array=array, p=Coord(2, 3), q=Coord(1, 0))
    assert(shortest == 6)


def test_no_possible_path():
    array = """. P . . .
. # # # .
. # # # .
. # Q # .
. # # # ."""

    with pytest.raises(NoPossiblePath):
        shortest = pathfind(array=array, p=Coord(1, 0), q=Coord(2, 3))


def test_out_of_bounds():
    array = """. P . . .
. # # # .
. . . . .
. . Q . .
. . . . ."""

    with pytest.raises(OutOfBoundsError):
        shortest = pathfind(array=array, p=Coord(-1, 10), q=Coord(10, -1))


def test_p_q_coincident():
    array = """. P . . .
. # # # .
. . . . .
. . . . .
. . . . ."""

    shortest = pathfind(array=array, p=Coord(1, 0), q=Coord(1, 0))
    assert(shortest == 0)

def test_large_map():
    array = "\n".join(" ".join("." for i in range(100)) for j in range(100))

    shortest = pathfind(array=array, p=Coord(50, 20), q=Coord(50, 30))
    assert(shortest == 10)


    

    

