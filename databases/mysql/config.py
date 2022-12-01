def configure():
    import os

    script_dir = os.path.dirname(os.path.abspath(__file__))

    absolute_dependencies = [
        f"{script_dir}/shared",
    ]

    from myutils import set_syspath
    set_syspath(absolute_dependencies)

    return {
        "commands_filename": f"{script_dir}/data/commandes.sql",
        "host":"localhost",
        "database": "dbpersonnes",
        "user": "admpersonnes",
        "password": "nobody"
    }