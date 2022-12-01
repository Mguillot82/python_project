def configure():
    # étape 1
    # Chemin absolu du dossier de ce script
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # dépendances
    absolute_dependencies = [
        # dossiers locaux du Python Path
        f"{script_dir}/../dao",
        f"{script_dir}/../ui",
        f"{script_dir}/../metier",
    ]

    # on configure le syspath
    from myutils import set_syspath
    set_syspath(absolute_dependencies)

    # étape 2
    # configuration des couches de l'application
    from DaoImpl2 import DaoImpl2
    from MetierImpl2 import MetierImpl2
    from UiImpl2 import UiImpl2
    # instanciation des couches
    # dao
    dao = DaoImpl2()
    # metier
    metier = MetierImpl2()
    metier.dao = dao
    # ui
    ui = UiImpl2()
    ui.metier = metier

    # on met les instances de couche dans la config
    # seule la couche ui est ici nécessaire
    config = {"ui": ui}

    # on rend la config
    return config