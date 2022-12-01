from InterfaceDao import InterfaceDao

class DaoImpl1(InterfaceDao):
    # implémentation InterfaceDao
    def do_something_in_dao_layer(self: InterfaceDao, x: int, y: int) -> int:
        return x + y