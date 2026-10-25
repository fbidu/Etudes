"""
Sample program from chapter 3. 1st, naïve version.

It accepts two directories, source and destination

It syncs both directories through three simple rules:
    
    1. If a file exists in source but not on the destination,
        copy it over to the destination

    2. If it exists in source but has a different name in the
        destination, rename it in the destination to match
        
    3. If it exists in the destination but not in the source,
        remove from the destination
"""

import hashlib
from pathlib import Path
import sys
import logging

BUFFER_SIZE = 65536
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
logger = logging.getLogger("sync")

def hash_file(path: Path):
    hasher = hashlib.sha1()
    with path.open("rb") as f:
        while buffer := f.read(BUFFER_SIZE):
            hasher.update(buffer)

    return hasher.hexdigest()

def main():
    source = Path(sys.argv[1])
    destination = Path(sys.argv[2])
    logger.info("Comparing %s with %s", source, destination)

    if not source.exists():
        logger.exception("'%s' does not exist", source)
        raise ValueError("Source must exist")
    if not source.is_dir():
        logger.exception("'%s' is not a directory", source)
        raise ValueError("Source must be a directory")
    
if __name__ == "__main__":
    main()
