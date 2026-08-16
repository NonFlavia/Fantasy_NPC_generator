"""Data used by the Fantasy NPC Generator.

Edit this file to customize roles, moralities, names, species,
classes, backgrounds and origins.
"""

NO_CLASS = "No adventuring class"


# Roles

ROLES = {
    "Adventurer": {
        "has_class": True,
        "min_level": 1,
        "max_level": 7,
        "moralities": ("good", "neutral", "evil"),
        "icon": None,
    },
    "Hero": {
        "has_class": True,
        "min_level": 8,
        "max_level": 14,
        "moralities": ("good",),
        "icon": None,
    },
    "Legendary Hero": {
        "has_class": True,
        "min_level": 15,
        "max_level": 20,
        "moralities": ("good",),
        "icon": None,
    },
    "Noble": {
        "has_class": False,
        "min_level": 1,
        "max_level": 10,
        "moralities": ("good", "neutral", "evil"),
        "icon": "noble.png",
    },
    "Merchant": {
        "has_class": False,
        "min_level": 1,
        "max_level": 10,
        "moralities": ("good", "neutral", "evil"),
        "icon": "merchant.png",
    },
    "Commoner": {
        "has_class": False,
        "min_level": 1,
        "max_level": 10,
        "moralities": ("good", "neutral", "evil"),
        "icon": "commoner.png",
    },
    "Minor Enemy": {
        "has_class": True,
        "min_level": 1,
        "max_level": 7,
        "moralities": ("evil",),
        "icon": None,
    },
    "Major Enemy": {
        "has_class": True,
        "min_level": 8,
        "max_level": 14,
        "moralities": ("evil",),
        "icon": None,
    },
    "Archenemy": {
        "has_class": True,
        "min_level": 15,
        "max_level": 20,
        "moralities": ("evil",),
        "icon": None,
    },
}


# Moralities

MORALITIES = {
    "good": {
        "color": "#355c8a",
        "alignments": (
            "Lawful Good",
            "Neutral Good",
            "Chaotic Good",
        ),
        "faiths": (
            "Follows a benevolent deity",
            "Follows a deity of justice",
            "Follows a deity of life",
            "Follows a deity of light",
            "Has no faith",
        ),
        "personalities": {
            "Altruistic and brave": (
                "If someone must face the danger, let it be me.",
                "I will not abandon those who need me.",
            ),
            "Kind and protective": (
                "Stay behind me. I will keep you safe.",
                "Strength means protecting those who have none.",
            ),
            "Honest and determined": (
                "I gave my word, and I intend to keep it.",
                "The difficult path is still the right one.",
            ),
            "Optimistic and inspiring": (
                "As long as we stand together, hope remains.",
                "This story is not over yet.",
            ),
        },
    },
    "neutral": {
        "color": "#66577a",
        "alignments": (
            "Lawful Neutral",
            "True Neutral",
            "Chaotic Neutral",
        ),
        "faiths": (
            "Follows a deity of knowledge",
            "Follows a deity of nature",
            "Follows a deity of fate",
            "Follows a deity of balance",
            "Has no faith",
        ),
        "personalities": {
            "Calm and thoughtful": (
                "A wise decision requires patience.",
                "First we understand the problem, then we act.",
            ),
            "Independent and cautious": (
                "Trust must be earned.",
                "I work better when nobody stands in my way.",
            ),
            "Pragmatic and direct": (
                "Tell me what needs to be done.",
                "We can discuss morality after we survive.",
            ),
            "Reserved and observant": (
                "I prefer to watch before I choose.",
                "People reveal more when you let them speak.",
            ),
        },
    },
    "evil": {
        "color": "#7a2020",
        "alignments": (
            "Lawful Evil",
            "Neutral Evil",
            "Chaotic Evil",
        ),
        "faiths": (
            "Follows a deity of death",
            "Follows a deity of darkness",
            "Follows a deity of tyranny",
            "Follows a deity of destruction",
            "Has no faith",
        ),
        "personalities": {
            "Ambitious and ruthless": (
                "Power belongs to those willing to take it.",
                "Mercy is a luxury I cannot afford.",
            ),
            "Cruel and arrogant": (
                "You are not worthy of my attention.",
                "You were defeated before you arrived.",
            ),
            "Manipulative and patient": (
                "Everyone makes the right choice eventually.",
                "There is no need for violence when words will suffice.",
            ),
            "Vengeful and determined": (
                "I remember every debt.",
                "You will answer for what you have done.",
            ),
        },
    },
}


# Name generation

NAMES = {
    "start": (
        "Aer", "Bel", "Cael", "Dar", "El", "Fen", "Iri", "Ka",
        "Lor", "Mor", "Nae", "Or", "Rae", "Syl", "Tha", "Val",
    ),
    "middle": (
        "", "a", "e", "i", "o", "ae", "eri", "ira", "ori", "yri",
    ),
    "end": (
        "l", "m", "n", "r", "s", "th", "del", "en", "ren", "vyn",
    ),
}


# Species

SPECIES = (
    "Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf",
    "Half-Orc", "Halfling", "Human", "Tiefling",
)


# Classes
# Add a class here and place its icon inside assets/icons.

CLASSES = {
    "Barbarian": "barbarian.png",
    "Bard": "bard.png",
    "Cleric": "cleric.png",
    "Druid": "druid.png",
    "Fighter": "fighter.png",
    "Monk": "monk.png",
    "Paladin": "paladin.png",
    "Ranger": "ranger.png",
    "Rogue": "rogue.png",
    "Sorcerer": "sorcerer.png",
    "Warlock": "warlock.png",
    "Wizard": "wizard.png",
}


# Backgrounds

BACKGROUNDS = (
    "Acolyte", "Charlatan", "Criminal", "Entertainer", "Folk Hero",
    "Guild Artisan", "Hermit", "Noble", "Outlander", "Sage",
    "Sailor", "Soldier", "Urchin",
)


# Origins

ORIGINS = (
    "Coast", "Desert", "Farmland", "Forest", "Island", "Large City",
    "Mountains", "Sea", "Small Village", "Swamp", "Tundra", "Underground",
)
