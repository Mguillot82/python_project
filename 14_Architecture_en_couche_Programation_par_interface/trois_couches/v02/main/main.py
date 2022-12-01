# main <-> UI <-> Metier <-> Dao

import importlib
import sys

# main --------
# il faut deux arguments
nb_args = len(sys.argv)
if nb_args != 2 or (sys.argv[1] != "config1" and sys.argv[1] != "config2"):
    print(f"Syntaxe : {sys.argv[0]} config1 ou config2")
    sys.exit()

# configuration de l'application
module = importlib.import_module(sys.argv[1])
config = module.configure()

# exécution de la couche ui
print(config["ui"].do_something_in_ui_layer(10,20))
    