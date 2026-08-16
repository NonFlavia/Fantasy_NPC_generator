"""Generate randomized NPC data from the settings in data.py."""

import random
from errors import ConfigurationError
import data
from npc import NPC


def generate_name() -> str:
    name_parts = data.NAMES
    start = random.choice(name_parts["start"])
    middle = random.choice(name_parts["middle"])
    end = random.choice(name_parts["end"])
    return start + middle + end


def generate_level(role: str) -> int:
    role_info = data.ROLES[role]
    minimum = role_info["min_level"]
    maximum = role_info["max_level"]
    level = random.randint(minimum, maximum)
    return level


def generate_class(role: str) -> str:
    role_info = data.ROLES[role]
    has_class = role_info["has_class"]
    if not has_class:
        return data.NO_CLASS
    class_names = tuple(data.CLASSES)
    npc_class = random.choice(class_names)
    return npc_class


def generate_morality(role: str) -> str:
    role_info = data.ROLES[role]
    moralities = role_info["moralities"]
    if not moralities:
        raise ConfigurationError(f"No moralities configured for role: {role}")
    morality = random.choice(moralities)
    return morality

def generate_alignment(morality: str) -> str:
    morality_info = data.MORALITIES[morality]
    alignments = morality_info["alignments"]
    alignment = random.choice(alignments)
    return alignment


def generate_faith(morality: str) -> str:
    morality_info = data.MORALITIES[morality]
    faiths = morality_info["faiths"]
    faith = random.choice(faiths)
    return faith


def generate_personality(morality: str) -> tuple[str, str]:
    morality_info = data.MORALITIES[morality]
    personalities = morality_info["personalities"]
    personality_names = tuple(personalities)
    personality = random.choice(personality_names)
    phrases = personalities[personality]
    phrase = random.choice(phrases)
    return personality, phrase


def generate_npc(role: str) -> NPC:
    name = generate_name()
    species = random.choice(data.SPECIES)
    level = generate_level(role)
    npc_class = generate_class(role)
    background = random.choice(data.BACKGROUNDS)
    origin = random.choice(data.ORIGINS)
    morality = generate_morality(role)
    alignment = generate_alignment(morality)
    faith = generate_faith(morality)
    personality, phrase = generate_personality(morality)

    npc = NPC(
        name=name,
        role=role,
        species=species,
        level=level,
        npc_class=npc_class,
        background=background,
        origin=origin,
        morality=morality,
        alignment=alignment,
        faith=faith,
        personality=personality,
        phrase=phrase,
    )
    return npc
