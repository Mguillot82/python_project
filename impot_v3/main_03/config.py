def configure():
    import os

    # chemin absolu du dossier de ce script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # racine à partir de laquelle vont être mesurés certains chemins relatifs
    root_dir = "C:/Users/matgu/Documents/10_Python/00_Cours_python/"

    # dépendances de l'application
    # absolute_dependencies = [
    #    f"{root_dir}/08_appli_impot/shared",
    # ]

    absolute_dependencies = [
        f"{script_dir}/../shared_03",
    ]

    # configuration de l'application
    config = {
        # chemin absolu du fichier des contribuables
        "taxpayersFilename": f"{script_dir}/../data_03/taxpayersdata.txt",
        # chemins absolu du fichier des résultats
        "resultsFilename": f"{script_dir}/../data_03/resultats.json",
        # chemin absolu du fichier des données de l'administration fiscale
        "admindataFilename": f"{script_dir}/../data_03/admindata.json"
    }

    # mise à jour du syspath
    from myutils import set_syspath
    set_syspath(absolute_dependencies)

    # on rend la config
    return config