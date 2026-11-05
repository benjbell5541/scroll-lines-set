"""Scroll Lines Set — Set the mouse wheel scroll-lines value and show the current number."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='scroll_lines_set',
        description='Set the mouse wheel scroll-lines value and show the current number.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Scroll Lines Set')
    print('Wheel speed without the Mouse dialog.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# cleanup (2026-11-03)
# tune (2026-11-03)
# tweak (2026-11-04)
# small fix (2026-11-04)
# cleanup (2026-11-05)
# refactor bit (2026-11-05)
# minor adjust (2026-11-05)
