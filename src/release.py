import re


def is_semver(tag: str) -> bool:
    return bool(re.fullmatch(r"v\d+\.\d+\.\d+", tag))
