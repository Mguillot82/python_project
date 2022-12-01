# application pour afficher les notes de élèves
# architecture multicouches

# Utilisateur <-> couche UI + Couche métier + Couche dao <-> SGBD

# la couche User Interface est la couche en contact avec l'utilisateur de l'application

# la couche métier implémente les règles de gestion de l'application (calcul d'un salaire par exemple). Elle utilise les
# données provenant de l'utilisateur via la couche UI et du SGBD via la couche DAO

# la couche Data Access Objects gère l'accès aux données du Système de Gestion de Bases de Données

# une autre structure envisageable contient un script principal main qui organise l'instanciation des couches.
# main est le chef d'orchestre et les couches sont les centres de compétences

# exemple :
# pas de bases de données
# dao gère les entités Eleves classe et Matière, Note pour noter les élèves
# métier permet de calculer des indicateurs sur les notes d'un élève
# la couche UI est une application console qui affiche les résultats des éleves

# La couche dao implémente l'interface InterfaceDao elle même implantée par la classe Dao. Tests_dao teste les méthodes
# de la couche dao.

# Une interface est un contrat passé entre code appelant et code appelé. Le code appelant ne connait pas l'implémentation
# du code appelé. C'est l'interface qui lui indique la façon de l'appeler. L'interface s'appelle également API.
# Application Programming Interface

# Le code appelant utilise des méthodes l'API. Les données peuvent provenir de différentes sources (en dur,
# base de données, fichiers textes...). C'est la programmation par interface.

# Notion Python qui s'approche de l'interface : la classe abstraite.