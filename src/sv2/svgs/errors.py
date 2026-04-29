from dataclasses import dataclass
from pathlib import Path


@dataclass
class NoPathsWithIdsException(Exception):
    path: Path

    def message(self):
        return (
            f"Could not find any paths with an `id` attribute in the file {self.path}"
        )
