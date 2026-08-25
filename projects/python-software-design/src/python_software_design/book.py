"""Module providing the Book data model."""

from __future__ import annotations


class Book:
    """Represents a book with a title and author information."""

    def __init__(self, title: str, last: str, first: str) -> None:
        """Initializes a Book instance with the given title and author names."""
        self._title: str = title
        self._last: str = last
        self._first: str = first

    @property
    def title(self) -> str:
        """Returns the title of the book."""
        return self._title

    @property
    def last(self) -> str:
        """Returns the last name of the author."""
        return self._last

    @property
    def first(self) -> str:
        """Returns the first name of the author."""
        return self._first

    def __str__(self) -> str:
        """Returns a string representation of the book."""
        return (
            f"{{TITLE: '{self._title}', LAST: '{self._last}', FIRST: '{self._first}'}}"
        )
