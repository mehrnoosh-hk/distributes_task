from node import Node
from __future__ import annotations


class Queue:
    def __init__(self):
        self.__head: Node | None = None
        self.__tail: Node | None = None

    def is_empty(self) -> bool:
        return not self.__head

    @property
    def head(self) -> Node | None:
        return self.__head

    @property
    def tail(self) -> Node | None:
        return self.__tail

    def add_to_queue(self, node: Node) -> Queue:
        if self.is_empty():
            self.__head = node
            self.__tail = node
            return self
        self.__tail.next(node)
        self.__tail = node
