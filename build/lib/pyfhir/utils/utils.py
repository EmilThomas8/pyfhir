"""
Utility helpers.
"""

import json


def pretty_json(data: dict) -> str:
    return json.dumps(
        data,
        indent=4,
        ensure_ascii=False,
        sort_keys=False,
    )