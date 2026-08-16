# Fantasy NPC Generator

```text
 /\_/\\
( o.o )   meow! a tiny helper for your next adventure
 > ^ <

                 / \  //\
        |\___/|      /   \//  \\
        /0  0  \__  /    //  | \ \
       /     /  \/_/    //   |  \  \
       @_^_@'/   \/_   //    |   \   \
       //_^_/     \/_ //     |    \    \
    ( //) |        \///      |     \     \
  ( / /) _|_ /   )  //       |      \     _\
( // /) '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
(( // )) ,-{        _      `-.|.-~-.           .~         `.
(( /// ))  '/\      /                 ~-. _ .-~      .-~^-.  \
 (( / ))     `.   {            }                   /      \  \
  ||||         \  \         -~                    |        }  \
  ||||          `._~-^._                          \       /    |
  ||||              {-_  ~-.      .-~-.           \     /     |
```

A small Python project that creates randomized fantasy NPCs for tabletop role-playing games.

Choose a role, press the button, and let the generator build a character with a name, species, class, level, background, origin, alignment, faith, personality, and a typical phrase.

I made this project for fun, for my role-playing sessions as a Dungeon Master, and yes... with coffee. A lot of coffee.

## Features

- Several NPC roles, from **Commoner** to **Legendary Hero** and **Archenemy**
- Randomized fantasy names built from smaller name fragments
- Classic fantasy tabletop RPG-inspired species, classes, backgrounds, and alignments
- Personalities and phrases based on the NPC's morality
- A responsive and scrollable **Tkinter** interface
- Pixel-art symbols based on the NPC's class or role
- Simple custom error handling for configuration and missing icons

## How to run it

You need **Python 3** with **Tkinter** installed.

1. Download the project and keep all files and folders together
2. Open a terminal inside the project folder
3. Run:

```bash
python main.py
```

On some systems, the command may be:

```bash
python3 main.py
```

## Project files

- `main.py` starts the application
- `gui.py` builds and manages the graphical interface
- `generator.py` contains the random generation logic
- `npc.py` defines the NPC object
- `data.py` is the main customization file
- `errors.py` defines the custom errors used by the project
- `pixel_art.py` loads and displays the correct icon
- `assets/icons` contains the pixel-art files used by the interface

## Make it your own

Most of the generator can be customized from `data.py` without changing the program logic.

You can:

- add or edit NPC roles and their level ranges
- choose which moralities are available for each role
- add moralities with their own alignments, faiths, colors, personalities, and phrases
- edit the fragments used to generate fantasy names
- add species, backgrounds, and origins
- add a new class by adding it to `CLASSES` and placing its icon inside `assets/icons`

The goal is to keep content changes in one place, so you do not need to search through the rest of the project just to customize the generator.

## About me!

I am currently studying at 42 in Italy, where I am building my foundations in software development through hands-on projects, problem solving, and peer learning.

This project is part of that learning process. I wanted to build something useful for my role-playing sessions while also practicing Python outside school projects and learning how to structure a small application of my own. :)

## License and reuse

The original source code written for this project is released under the **MIT-0 License**.

Feel free to use it, study it, modify it, copy parts of it, or reuse it in your own projects. Credit is not required, but if something here was useful to you, a little mention of **NonFlavia** would make me very happy. :)

This license applies only to my original source code. Third-party artwork, names, material, and intellectual property keep their own licenses and rights.

## A small disclaimer before the law mages arrive

Obviously, this is not an official Wizards of the Coast project.

This repository is shared as a free, non-commercial, fan-made tool for tabletop role-playing games. Some names, terminology, or game concepts may be inspired by material published by Wizards of the Coast.

The project is not approved, endorsed, sponsored, or affiliated with Wizards of the Coast. Anything that belongs to Wizards remains theirs; the MIT-0 license above only covers my original source code.

You can read the official [Wizards of the Coast Fan Content Policy](https://company.wizards.com/en/legal/fancontentpolicy) for the rules that apply to their intellectual property.

## AI-assisted development

I used AI-assisted tools mostly while working on the graphical interface, since GUI development is still something I am learning.

If a more experienced developer ever wants to improve or rewrite that part, contributions are very welcome. I would genuinely enjoy seeing how someone else approaches the same problem, learning from it, and maybe turning this little project into a chance to collaborate with other developers.

## Pixel-art credits

The pixel-art icons come from the **Medieval Fantasy** asset pack created by **Pixel-boy for Sparklin Labs**.

- [Asset repository](https://github.com/sparklinlabs/superpowers-asset-packs)
- License: **Creative Commons Zero 1.0 Universal (CC0-1.0)**

Attribution is not required by the license, but I still wanted to credit the original creators because I think it is a nice thing to do.

## Author

Made with coffee, affection for fantasy worlds, and a soft spot for chaotic NPC creation by [NonFlavia](https://github.com/NonFlavia).

Feel free to explore the project, study it, and adapt it to your own setting.

```text
 /\_/\
( •.• )  thanks for stopping by
 > ^ <
```
