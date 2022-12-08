from __future__ import annotations

import urllib.parse

from functools import partialmethod
from typing import TYPE_CHECKING
from typing import Iterable
import sys
from pathlib import Path
import json
from tempfile import NamedTemporaryFile

from cleo.io.io import IO
from poetry.core.packages.dependency_group import MAIN_GROUP

from .tools import Struct


if TYPE_CHECKING:
    from pathlib import Path

    from packaging.utils import NormalizedName
    from poetry.poetry import Poetry


class Cutter:
    """
    Class to utilize Limerick
    """
    

    def __init__(self, poetry: Poetry, io: IO) -> None:
        self._poetry = poetry
        self._io = io
        

    def cut(self, cli:Struct):
        print(self._poetry.local_config)
        f = NamedTemporaryFile(mode="w")
        f.write(json.dumps(self._poetry.local_config))
        f.seek(0)
        

        
        f.delete
        