from enum import IntFlag, auto


class Border(IntFlag):
    EMPTY = 0
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()

    @property
    def corner(self) -> bool:
        """The corner property."""
        return self in (
            self.TOP | self.LEFT,
            self.TOP | self.RIGHT,
            self.BOTTOM | self.RIGHT,
            self.BOTTOM | self.LEFT,
        )

    @property
    def dead_end(self) -> bool:
        """The dead_end property."""
        return self.bit_count() == 3

    @property
    def intersection(self) -> bool:
        """The intersection property."""
        return self.bit_count < 2
