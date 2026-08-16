from dataclasses import dataclass

from data import NO_CLASS


@dataclass
class NPC:
    name: str
    role: str
    species: str
    level: int
    npc_class: str
    background: str
    origin: str
    morality: str
    alignment: str
    faith: str
    personality: str
    phrase: str

    def show(self) -> None:
        print("\n=== RANDOM NPC ===")
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
        print(f"Species: {self.species}")

        if self.npc_class == NO_CLASS:
            print(f"Professional level: {self.level}")
        else:
            print(f"Class: {self.npc_class}")
            print(f"Class level: {self.level}")

        print(f"Background: {self.background}")
        print(f"Origin: {self.origin}")
        print(f"Morality: {self.morality}")
        print(f"Alignment: {self.alignment}")
        print(f"Faith: {self.faith}")
        print(f"Personality: {self.personality}")
        print(f'Typical phrase: "{self.phrase}"')