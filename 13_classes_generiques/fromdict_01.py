# on configure l'application
import config

config = config.configure()

# le syspath est configuré, on peut importer
from enseignant import Enseignant

# un enseignant
enseignant1 = Enseignant().fromdict({"id": 1, "nom": "Lourou", "prenom": "paul", "age": 56})
enseignant1.show()
