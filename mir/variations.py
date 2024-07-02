import itertools
import subprocess
from pathlib import Path


stop_template = """<stop
         style="stop-color:#{};stop-opacity:1;"
         offset="0"
         id="{}" />"""

stop_num_badge_outer = "stop6"
stop_num_badge_inner = "stop18"
stop_num_lines = "stop4"
stop_num_arrows_accent = "stop9"

order = (
    stop_num_lines,
    stop_num_badge_outer,
    stop_num_badge_inner,
    stop_num_arrows_accent,
)

blue = "5bcefa"
pink = "f5a9b8"
white = "ffffff"
yellow = "fdd910"

mimi_blue = "4fd6d4"
mimi_pink = "dd43e1"
mimi_white = "f3ece7"
mimi_black = "5f5b6a"

to_rearrange = (
    mimi_blue,
    mimi_pink,
    mimi_white,
    mimi_black,
)

current = (
    pink,
    blue,
    white,
    yellow,
)

svg_path = Path("Mir_insignia.svg")
temp_path = Path("Mir_variant.svg")


def replace(colours, out_name):
    contents = svg_path.read_text()
    for i in range(4):
        old = stop_template.format(current[i], order[i])
        new = stop_template.format(colours[i], order[i])
        contents = contents.replace(old, new)
    temp_path.write_text(contents)

    subprocess.run(["inkscape", temp_path, "-o", out_name, "--export-type", "png"])



def permute():
    orderings = itertools.permutations(to_rearrange)
    for colours in orderings:
        out_name = "palettes/" + "-".join(colours) + ".png"
        colours = list(colours)
        # make up arrow accent if only
        # permuting three colours
        # colours.append(colours[1])
        replace(colours, out_name)



if __name__ == "__main__":
    permute()
