"""Tkinter interface for the Fantasy NPC Generator."""

import tkinter as tk
from tkinter import messagebox, ttk
from errors import NPCGeneratorError
import webbrowser
from data import ROLES, NO_CLASS
from generator import generate_npc
from pixel_art import draw_symbol


TEXTS = {
    "title": "Fantasy NPC Generator",
    "header": "FANTASY NPC GENERATOR",
    "subtitle": "Choose a role and meet someone new.",
    "button": "CREATE A NEW NPC",
    "footer": "Made with coffee and dice by NonFlavia — feel free to use it.",
    "credit": "Pixel art by Pixel-boy for Sparklin Labs — CC0",
}

LINKS = {
    "mine": "https://github.com/NonFlavia",
    "artist": "https://github.com/sparklinlabs/superpowers-asset-packs",
}

SIZES = {
    "window": "700x850",
    "width": 520,
    "height": 600,
    "symbol": 128,
    "text": 180,
    "space": 260,
}

COLORS = {
    "background": "#d8c9a7",
    "card": "#f4ecd8",
    "text": "#2b2118",
    "secondary": "#665747",
    "accent": "#8b1e1e",
    "gold": "#a67c35",
    "light": "#fff8e7",
    "hover": "#a52a2a",
    "pressed": "#641414",
}

FONTS = {
    "title": ("Open Sans", 27, "bold"),
    "subtitle": ("Georgia", 10, "italic"),
    "text": ("Open Sans", 11),
    "label": ("Georgia", 9, "bold"),
    "button": ("Georgia", 11, "bold"),
    "footer": ("Georgia", 9, "italic"),
    "ornament": ("Georgia", 12),
}

FIELDS = (
    ("Name", "name"),
    ("Their role", "role"),
    ("Species", "species"),
    ("Adventuring class", "npc_class"),
    ("Experience", "level"),
    ("Background", "background"),
    ("They come from", "origin"),
    ("Alignment", "alignment"),
    ("Beliefs", "faith"),
    ("Personality", "personality"),
    ("Something they might say", "phrase"),
)


class NPCGeneratorGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.values: dict[str, tk.StringVar] = {}
        self.labels: list[tk.Label] = []
        self.setup_window()
        self.create_style()
        self.create_header()
        self.create_controls()
        self.create_footer()
        self.create_card()
        self.generate()

    def setup_window(self) -> None:
        self.root.title(TEXTS["title"])
        self.root.geometry(SIZES["window"])
        self.root.minsize(SIZES["width"], SIZES["height"])
        self.root.configure(bg=COLORS["background"])
        self.root.resizable(True, True)

    def create_style(self) -> None:
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Generate.TButton",
            background=COLORS["accent"],
            foreground=COLORS["light"],
            font=FONTS["button"],
            padding=(22, 10),
            borderwidth=0,
        )
        style.map(
            "Generate.TButton",
            background=[
                ("active", COLORS["hover"]),
                ("pressed", COLORS["pressed"]),
            ],
        )

        style.configure(
            "Role.TCombobox",
            fieldbackground=COLORS["card"],
            background=COLORS["accent"],
            foreground=COLORS["text"],
            arrowcolor=COLORS["light"],
            bordercolor=COLORS["gold"],
            padding=8,
        )
        style.map(
            "Role.TCombobox",
            fieldbackground=[("readonly", COLORS["card"])],
            foreground=[("readonly", COLORS["text"])],
            selectbackground=[("readonly", COLORS["card"])],
            selectforeground=[("readonly", COLORS["text"])],
        )

    def create_header(self) -> None:
        title = tk.Label(
            self.root,
            text=TEXTS["header"],
            bg=COLORS["background"],
            fg=COLORS["accent"],
            font=FONTS["title"],
        )
        title.pack(pady=(22, 2))

        subtitle = tk.Label(
            self.root,
            text=TEXTS["subtitle"],
            bg=COLORS["background"],
            fg=COLORS["secondary"],
            font=FONTS["subtitle"],
        )
        subtitle.pack(pady=(0, 10))

        ornament = tk.Label(
            self.root,
            text="◆ ───────────────── ◆",
            bg=COLORS["background"],
            fg=COLORS["gold"],
            font=FONTS["ornament"],
        )
        ornament.pack(pady=(0, 16))

    def create_controls(self) -> None:
        controls = tk.Frame(self.root, bg=COLORS["background"])
        controls.pack(pady=(0, 18))

        self.role_box = ttk.Combobox(
            controls,
            values=tuple(ROLES),
            state="readonly",
            width=23,
            style="Role.TCombobox",
            font=FONTS["text"],
        )
        self.role_box.set("Adventurer")
        self.role_box.grid(row=0, column=0, padx=(0, 12))

        button = ttk.Button(
            controls,
            text=TEXTS["button"],
            command=self.generate,
            style="Generate.TButton",
        )
        button.grid(row=0, column=1)

    def create_footer(self) -> None:
        footer = tk.Frame(self.root, bg=COLORS["background"])
        footer.pack(side="bottom", pady=(0, 10))

        mine = tk.Label(
            footer,
            text=TEXTS["footer"],
            bg=COLORS["background"],
            fg=COLORS["secondary"],
            font=FONTS["footer"],
            cursor="hand2",
        )
        mine.pack()
        mine.bind("<Button-1>", self.open_mine)

        artist = tk.Label(
            footer,
            text=TEXTS["credit"],
            bg=COLORS["background"],
            fg=COLORS["secondary"],
            font=FONTS["footer"],
            cursor="hand2",
        )
        artist.pack(pady=(2, 0))
        artist.bind("<Button-1>", self.open_artist)

    def create_card(self) -> None:
        card = self.create_scrollbar()

        self.symbol = tk.Canvas(
            card,
            width=SIZES["symbol"],
            height=SIZES["symbol"],
            bg=COLORS["card"],
            highlightbackground=COLORS["gold"],
            highlightthickness=2,
        )
        self.symbol.grid(row=0, column=0, columnspan=2, pady=(0, 18))

        for row, field in enumerate(FIELDS, start=1):
            text, attribute = field
            self.values[attribute] = tk.StringVar()

            label = tk.Label(
                card,
                text=text.upper(),
                bg=COLORS["card"],
                fg=COLORS["accent"],
                font=FONTS["label"],
                anchor="w",
            )
            label.grid(row=row, column=0, sticky="nw", padx=(0, 30), pady=7)

            value = tk.Label(
                card,
                textvariable=self.values[attribute],
                bg=COLORS["card"],
                fg=COLORS["text"],
                font=FONTS["text"],
                anchor="w",
                justify="left",
                wraplength=360,
            )
            value.grid(row=row, column=1, sticky="new", pady=7)
            self.labels.append(value)

        card.columnconfigure(1, weight=1)
        card.bind("<Configure>", self.update_scrollbar)
        self.scroll.bind("<Configure>", self.resize_card)
        self.scroll.bind_all("<MouseWheel>", self.scroll_mouse)

    def create_scrollbar(self) -> tk.Frame:
        area = tk.Frame(self.root, bg=COLORS["background"])
        area.pack(fill="both", expand=True, padx=40, pady=(0, 25))

        self.scroll = tk.Canvas(area, bg=COLORS["background"], highlightthickness=0)
        bar = ttk.Scrollbar(area, orient="vertical", command=self.scroll.yview)

        self.scroll.configure(yscrollcommand=bar.set)
        bar.pack(side="right", fill="y")
        self.scroll.pack(side="left", fill="both", expand=True)

        card = tk.Frame(
            self.scroll,
            bg=COLORS["card"],
            highlightbackground=COLORS["gold"],
            highlightthickness=2,
            padx=32,
            pady=20,
        )
        self.card = self.scroll.create_window((0, 0), window=card, anchor="nw")
        return card

    def open_mine(self, _event: tk.Event) -> None:
        webbrowser.open(LINKS["mine"])

    def open_artist(self, _event: tk.Event) -> None:
        webbrowser.open(LINKS["artist"])

    def update_scrollbar(self, _event: tk.Event) -> None:
        self.scroll.configure(scrollregion=self.scroll.bbox("all"))

    def resize_card(self, event: tk.Event) -> None:
        self.scroll.itemconfigure(self.card, width=event.width)
        width = max(SIZES["text"], event.width - SIZES["space"])

        for label in self.labels:
            label.configure(wraplength=width)

    def scroll_mouse(self, event: tk.Event) -> None:
        direction = int(-event.delta / 120)
        self.scroll.yview_scroll(direction, "units")

    def format_class_and_level(self, npc_class: str, level: int) -> tuple[str, str]:
        if npc_class == NO_CLASS:
            return "—", f"Professional level {level}"
        return npc_class, f"Class level {level}"

    def generate(self) -> None:
        selected_role = self.role_box.get()
        try:
            npc = generate_npc(selected_role)
            npc_class, level = self.format_class_and_level(npc.npc_class, npc.level)
            draw_symbol(self.symbol, npc.npc_class, npc.role, npc.morality)
        except NPCGeneratorError as error:
            messagebox.showerror("Generation error", str(error))
            return
        values = {
            "name": npc.name,
            "role": npc.role,
            "species": npc.species,
            "npc_class": npc_class,
            "level": level,
            "background": npc.background,
            "origin": npc.origin,
            "alignment": npc.alignment,
            "faith": npc.faith,
            "personality": npc.personality,
            "phrase": f'“{npc.phrase}”',
        }
        for attribute, value in values.items():
            self.values[attribute].set(value)
