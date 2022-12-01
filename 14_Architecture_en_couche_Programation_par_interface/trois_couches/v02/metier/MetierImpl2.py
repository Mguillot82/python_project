from AbstractBaseMetier import AbstractBaseMetier

class MetierImpl2(AbstractBaseMetier):
    # implémentation de l'interface InterfaceMetier
    def do_something_in_metier_layer(self: AbstractBaseMetier, x: int, y: int) -> int:
        x -= 1
        y -= 1
        return self.dao.do_something_in_dao_layer(x,y)