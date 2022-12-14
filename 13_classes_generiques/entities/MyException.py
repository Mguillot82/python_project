# fournit une classe d'exceptions propriétaire

class MyException(BaseException):
    # constructeur
    def __init__(self: object, code: int, message: str):
        # parent
        BaseException.__init__(self, message)
        # code  erreur
        self.code = code
    
    # toString
    def __str__(self):
        return f"MyException[{self.code}, {super().__str__()}]"

    # getter
    @property
    def code(self) -> int:
        return self.__code

    # setter
    @code.setter
    def code(self, code: int):
        # le code d'erreur doit être un entier positif
        if isinstance(code, int) and code > 0:
            self.__code = code
        else:
            # exception
            raise BaseException(f"code erreur {code} incorrect")
            