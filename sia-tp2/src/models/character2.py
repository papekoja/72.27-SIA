from src.models.constants import Classes

class character:
    
    
    def __init__(self, character_class: Classes, strength, agility, expertise, resistance, health, height, gene1=None, gene2=None):
        self.character_class = character_class