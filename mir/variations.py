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
    stop_num_arrows_accent,
    stop_num_badge_inner
)

blue = "5bcefa"
pink = "f5a9b8"
white = "ffffff"
yellow = "fdd910"

current = (pink, blue, yellow, white)

svg_path = Path("Mir_insignia.svg")
temp_path = Path("Mir_variant.svg")


def replace(colours, out_name):
    contents = svg_path.read_text()
    for i in range(4):
        old = stop_template.format(current[i], order[i])
        new = stop_template.format(colours[i], order[i])
        print(old)
        print(new)
        contents = contents.replace(old, new)
    temp_path.write_text(contents)


if __name__ == "__main__":
    replace(("ffffff", "ffffff", "ffffff", "ffffff", ), "abc.svg")

