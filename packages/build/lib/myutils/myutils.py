# imports
import sys
import os


# Crée un Python Path avec la liste des dossiers qu'on lui transmet en paramètre.
def set_syspath(absolute_dependencies: list):
    # absolute_dependencies : une liste de noms absolus de dossiers

    # on ajoute au syspath les dépendances absolues du projet
    for directory in absolute_dependencies:
        # on vérifie l'existence du dossier
        existe = os.path.exists(directory) and os.path.isdir(directory)
        if not existe:
            # on lève une exception
            raise BaseException(f"[set_syspath] le dossier du Python Path [{directory}] n'existe pas")
        else:
            # on ajoute le dossier au début du syspath
            sys.path.insert(0,directory)