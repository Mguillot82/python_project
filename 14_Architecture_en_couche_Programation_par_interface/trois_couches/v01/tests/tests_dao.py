import config

config = config.configure()

# instanciation couche dao
from Dao import Dao

daoImp1 = Dao()

# liste des classes
for classe in daoImp1.get_classes():
    print(classe)

# liste des matières
for matiere in daoImp1.get_matieres():
    print(matiere)

# liste des élèves
for eleve in daoImp1.get_eleves():
    print(eleve)

# liste des notes
for note in daoImp1.get_notes():
    print(note)

# un élève particulier
print(daoImp1.get_eleve_by_id(11))

# la liste de ses notes
dict1 = daoImp1.get_notes_for_eleve_by_id(11)
print(f"élève n° 11 = {dict1['eleve']}")
for note in dict1["notes"]:
    print(f"note de l'élève n° 11 = {note}")