from __future__ import annotations

from pathlib import Path
import toml

from cleo.helpers import option, argument
from packaging.utils import canonicalize_name
from poetry.console.commands.group_command import GroupCommand
from poetry.core.packages.dependency_group import MAIN_GROUP

from poetry_plugin_limerick.cc import Cutter

toml_file = Path(__file__).absolute().parent.parent.joinpath("pyproject.toml")

class LimerickCommand(GroupCommand):
    name = "limerick"
    description = "Creates boilerplate files using cookiecutter."
    version = toml.load(toml_file)['tool']['poetry']['version']
    # options = [
    #     option(
    #         "format",
    #         "f",
    #         "Format to export to. Currently, only constraints.txt and requirements.txt"
    #         " are supported.",
    #         flag=False,
    #         # default=Exporter.FORMAT_REQUIREMENTS_TXT,
    #     ),
    #     *GroupCommand._group_dependency_options(),
    #     option(
    #         "extras",
    #         "E",
    #         "Extra sets of dependencies to include.",
    #         flag=False,
    #         multiple=True,
    #     ),
    #     ]

    arguments = [argument(name="main_arg")]

    @property
    def non_optional_groups(self) -> set[str]:
        # method only required for poetry <= 1.2.0-beta.2.dev0
        return {MAIN_GROUP}

    @property
    def default_groups(self) -> set[str]:
        return {MAIN_GROUP}

    def handle(self) -> None:
        cc_file = self.argument("main_arg")
        print(f"Hello from LimerickCommand v{self.version}")
        print(f"I got arguments: {cc_file}")
        print(f"Everything else: {self.__dict__}")