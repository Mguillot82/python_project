def configure():
    import os

    # chemin absolu du dossier de ce script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # root_dir
    root_dir = "C:\\Users\\matgu\\Documents\\10_Python\\00_Cours_python"
    # dépendances absolues
    absolute_dependencies = [
        # les dossiers locaux contenant des classes et interfaces
        f"{root_dir}\\13_classes_generiques\\entities",
        f"{script_dir}\\..\\entities",
        f"{script_dir}\\..\\interfaces",
        f'{script_dir}\\..\\services',
    ]

    # mise à jour du syspath
    from myutils import set_syspath
    set_syspath(absolute_dependencies)

    # on rend la config
    return {}