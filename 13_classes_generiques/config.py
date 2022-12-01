def configure():
    import os

    # dossier du fichier de configuration
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # chemins absolus des dossiers à mettre dans le syspath
    absolute_dependencies = [
        # la classe BaseEntity
        f"{script_dir}/entities",
    ]

    # mise à jour du syspath
    from myutils import set_syspath
    set_syspath(absolute_dependencies)

    # on rend la configuration
    return {}
