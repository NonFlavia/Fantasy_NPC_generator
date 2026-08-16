from pathlib import Path
import tkinter as tk
from errors import ConfigurationError, IconError
import data


ICON_CENTER = 64
ICON_SIZE = 82
ICON_FOLDER = Path(__file__).parent / "assets" / "icons"


def get_background(morality: str) -> str:
    morality_info = data.MORALITIES[morality]
    color = morality_info["color"]
    return color


def get_icon_name(npc_class: str, role: str) -> str:
    if npc_class != data.NO_CLASS:
        icon_name = data.CLASSES[npc_class]
        return icon_name
    role_info = data.ROLES[role]
    icon_name = role_info["icon"]
    if icon_name is None:
        raise ConfigurationError(f"No icon configured for role: {role}")
    return icon_name


def load_icon(icon_name: str) -> tk.PhotoImage:
    path = ICON_FOLDER / icon_name
    if not path.exists():
        raise IconError(f"Icon not found: {path}")
    icon = tk.PhotoImage(file=str(path))
    side = max(icon.width(), icon.height())
    zoom_factor = max(1, ICON_SIZE // side)
    icon = icon.zoom(zoom_factor, zoom_factor)
    return icon


def draw_symbol(canvas: tk.Canvas, npc_class: str, role: str, morality: str) -> None:
    background = get_background(morality)
    icon_name = get_icon_name(npc_class, role)
    icon = load_icon(icon_name)
    canvas.delete("all")
    canvas.configure(bg=background)
    canvas.create_image(ICON_CENTER, ICON_CENTER, image=icon)
    canvas.icon = icon
