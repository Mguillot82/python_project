from AbstractBaseUi import AbstractBaseUi

class UiImpl1(AbstractBaseUi):
    # implémentation de l'interface InterfaceUi
    def do_something_in_ui_layer(self: AbstractBaseUi, x: int, y:int) -> int:
        x += 1
        y += 1
        return self.metier.do_something_in_metier_layer(x,y)
