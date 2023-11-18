# from interfaces.builder_interface import BuilderInterface
from builder import Builder
from connection import Connection


class ListBuilder(Builder):
    def __init__(self, app, connection: Connection) -> None:
        super().__init__(app, connection)

    def build(self):
        self.build_menu()
