"""Custom errors used by the Fantasy NPC Generator."""


class NPCGeneratorError(Exception):
    pass


class ConfigurationError(NPCGeneratorError):
    pass


class IconError(NPCGeneratorError):
    pass
