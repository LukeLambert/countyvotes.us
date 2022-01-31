#!/usr/bin/env python3

import hashlib
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / 'map-in.svg'
OUTPUT_FILE = BASE_DIR / 'map-out.svg'

with INPUT_FILE.open('r') as in_file, OUTPUT_FILE.open('w') as out_file:
    out_file.write(
        re.sub(
            ' id="(c\d+)"',
            lambda m: ' opacity="0.{:02d}"'.format(
                int(hashlib.md5(m.group(1).encode()).hexdigest()[3], 16) + 4,
            ),
            in_file.read()
        )
    )
