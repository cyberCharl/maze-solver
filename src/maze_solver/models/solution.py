from dataclasses import dataclass
from functools import reduce
from typing import Iterator

from maze_solver.models.role import Role
from maze_solver.models.square import Square


@dataclass(frozen=True)
class Solution:
    squares: tuple[Square, ...]

    # Validation includes checking that the first square is the entrance,
    # the last square is the exit and if the squares form a corridor
    def __post_init__(self) -> None:
        assert self.squares[0].role is Role.ENTRANCE
        assert self.squares[-1].role is Role.EXIT
        reduce(validate_corridor, self.squares)

    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

    def __getitem__(self, index: int) -> Square:
        return self.squares[index]

    # Compare length of solution to other possible solutions
    def __len__(self) -> int:
        return len(self.squares)


# Corridor validation checks whether the current and following square share
# either a row or column
def validate_corridor(current: Square, following: Square) -> Square:
    assert any([
        current.row == following.row,
        current.column == following.column
    ]), "Squares must lie in the same row or column"
    return following
