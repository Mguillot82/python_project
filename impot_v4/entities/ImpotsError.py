# classe d'exception propriétaire
# classe d'exception
from MyException import MyException

# Derive de MyException : raise ImpotError(code_erreur, msg_erreur)
class ImpotsError(MyException):
    pass