from pathlib import Path
from json2m3u import json_to_m3u
import os

if __name__ == "__main__":
    import sys

    input_json_file = Path("tv-garden/channels/raw/countries").rglob("*.json")
    output_m3u_dir = Path("output")
    os.makedirs(output_m3u_dir, exist_ok=True)

    for json_file in input_json_file:
        json_to_m3u(json_file, output_m3u_dir / f"{json_file.stem}.m3u")