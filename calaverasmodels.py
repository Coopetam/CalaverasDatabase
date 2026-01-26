class Character:
    def __init__(self, name, heritage, profession):
        self.name = name
        self.heritage = heritage
        self.profession = profession

    def to_dict(self):
        return {
            "name": self.name,
            "heritage": self.heritage,
            "profession": self.profession
        }

    @staticmethod
    def from_dict(data):
        return Character(
            data["name"],
            data["heritage"],
            data["profession"]
        )
