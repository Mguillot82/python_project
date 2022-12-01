def configure():
    import os

    # étape 1 ------
    # configuration du python Path

    # dossier de ce fichier
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # root_dir
    root_dir = "C:\\Users\\matgu\\Documents\\10_Python\\00_Cours_python\\13_classes_generiques"
    # dépendances absolues de l'application
    absolute_dependencies = [
        f"{script_dir}/../entities",
        f"{script_dir}/../interfaces",
        f"{script_dir}/../services",
        f"{root_dir}/entities",
    ]

    # on fixe le syspath
    from myutils import set_syspath
    set_syspath(absolute_dependencies)

    # étape 2 ------
    # configuration de l'application
    config = {
        # chemins absolus des fichiers de l'application
        "admindataFilename": f"{script_dir}/../data/input/admindata.json"
    }

    # instanciation des couches de l'application
    from ImpotsDaoWithAdminDataInJsonFile import ImpotsDaoWithAdminDataInJsonFile
    from ImpotsMetier import ImpotsMetier

    dao = ImpotsDaoWithAdminDataInJsonFile(config)
    metier = ImpotsMetier()

    # on met les instances de couches dans la config
    config["dao"] = dao
    config["metier"] = metier

    # on rend la config
    return config

