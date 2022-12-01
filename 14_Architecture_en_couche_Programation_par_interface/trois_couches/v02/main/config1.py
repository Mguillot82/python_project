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

    from DaoImpl1 import DaoImpl1
    from MetierImpl1 import MetierImpl1
    from UiImpl1 import UiImpl1
    # instanciation des couches
    # dao
    dao = DaoImpl1()
    # metier
    metier = MetierImpl1()
    metier.dao = dao
    # ui
    ui = UiImpl1()
    ui.metier = metier

    # on met les instances de couche dans la config
    # seule la couche ui est ici nécessaire
    config = {"ui": ui}

    # on rend la config
    return config