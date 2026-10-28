from models.cours import Cours

class Programme:
    def __init__(self, nom: str):
        self.nom = nom
        self.cours: list[Cours] = []

    def ajouter_cours(self, cours: Cours) -> None:
        self.cours.append(cours)

 #  asd
    def moyenne(self) -> float:
        if not self.cours:
            return 0.0
        return round(sum(c.moyenne() for c in self.cours) / len(self.cours), 1)

    def nb_etudiants(self) -> int:
        return sum(c.nb_etudiants() for c in self.cours)
    # on pourrait aussi faire:
    # somme = 0
    # for cours in self.cours:
    #     somme += cours.nb_etudiants()
    #   return somme

    # Programme.to_dict() — délègue à ses enfants directs
    def to_dict(self) -> dict:
        return {
            "type": "programme",
            "nom": self.nom,
            "moyenne": self.moyenne(),
            "nb_etudiants": self.nb_etudiants(),
            "enfants": [c.to_dict() for c in self.cours]
        }
