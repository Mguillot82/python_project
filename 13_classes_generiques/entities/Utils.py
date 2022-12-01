class Utils:

    # méthode statique
    @staticmethod
    def is_string_ok(string: str) -> bool:
        # string est elle une chaîne ?
        erreur = not isinstance(string, str)
        if not erreur:
            # la chaîne est elle vide ?
            erreur = string.strip() == ''
        # résultat
        return not erreur
