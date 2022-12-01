# script principal de l'application
import config

config = config.configure()

# le syspath est configuré - on peut faire les imports
from Console import Console
from Dao import Dao
from Metier import Metier

# -------- couche console
try:
    # instanciation couche dao
    dao = Dao()
    # instanciation couche metier
    metier = Metier(dao)
    # instanciation couche ui
    console = Console(metier)
    # execution couche console
    console.run()
except BaseException as ex:
    # on affiche l'erreur
    print(f"L'erreur suivante s'est produite : {ex}")
finally:
    pass