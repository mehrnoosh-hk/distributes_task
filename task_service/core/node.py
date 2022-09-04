from typing import Any
from __future__ import annotations

class Node:
    def __init__(self, value: Any):
        self.__value = value
        self.__next: Node | None = None

    @property
    def value(self) -> Any:
        return self.__value

    @value.setter
    def value(self, new_value: Any) -> None:
        self.__value = new_value

    @property
    def next(self) -> Node:
        return self.__next

    @next.setter
    def next(self, new_value: Node) -> None:
        self.__next = new_value

    @next.deleter
    def next(self):
        self.__next = None
