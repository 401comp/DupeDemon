"""Safety policy for Apple Photos library bundles.

Photos libraries are database-backed packages. Their image originals must not
be removed with Finder-level file operations: doing so can leave Photos with
broken records. Dupe Demon can inspect them, but treats every item inside one
as a protected reference.
"""

from pathlib import Path


PHOTO_LIBRARY_SUFFIXES = (".photoslibrary", ".migratedphotolibrary")


def photo_library_root(path):
    """Return the enclosing Photos library bundle for *path*, if any."""
    candidate = Path(path).expanduser()
    for part in (candidate, *candidate.parents):
        if part.name.lower().endswith(PHOTO_LIBRARY_SUFFIXES):
            return str(part)
    return None


def is_photos_library(path):
    """Whether *path* is a Photos library package or lives inside one."""
    return photo_library_root(path) is not None
