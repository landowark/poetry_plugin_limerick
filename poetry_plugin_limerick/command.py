from __future__ import annotations

from pathlib import Path
import toml

from cleo.helpers import option, argument
from packaging.utils import canonicalize_name
from poetry.console.commands.group_command import GroupCommand
from poetry.core.packages.dependency_group import MAIN_GROUP
from poetry.core.pyproject.toml import PyProjectTOML
from poetry.factory import Factory


from poetry_plugin_limerick.cc import Cutter

toml_file = Path(__file__).absolute().parent.parent.joinpath("pyproject.toml")

class LimerickCommand(GroupCommand):
    name = "limerick"
    description = "Creates boilerplate files using cookiecutter."
    version = toml.load(toml_file)['tool']['poetry']['version']
    options = [
        option(
            "checkout",
            "c",
            "The branch, tag or commit ID to checkout after clone.",
            flag=False,
            # default=Exporter.FORMAT_REQUIREMENTS_TXT,
        ),
        *GroupCommand._group_dependency_options(),
        option(
            "no-input",
            "i",
            "Prompt the user at command line for manual configuration?",
            flag=True,
        ),
        option(
            "extra-content",
            "e",
            "A dictionary of context that overrides default and user configuration.",
            flag=False,
        ),
        option(
            "replay",
            "r",
            " Do not prompt for input, instead read from saved json. If \
            ``True`` read from the ``replay_dir``. \
            if it exists",
            flag=True,
        ),
        option(
            "config-file",
            "x",
            "User configuration file path.",
            flag=False,
        ),
        option(
            "default_config",
            "d",
            "Use default values rather than a config file.",
            flag=True,
        ),
        option(
            "password",
            "p",
            "The password to use when extracting the repository.",
            flag=False,
        ),
        option(
            "directory", 
            "b",
            "Relative path to a cookiecutter template in a repository.",
            flag=False,            
        ),
        option(
            "deny-hooks", 
            None,
            "Accept pre and post hooks if set to `True`.",
            flag=True,
        ),
        ]

    arguments = [argument(name="template"), argument(name="output_dir", optional=True, default=".")]

    @property
    def non_optional_groups(self) -> set[str]:
        # method only required for poetry <= 1.2.0-beta.2.dev0
        return {MAIN_GROUP}

    @property
    def default_groups(self) -> set[str]:
        return {MAIN_GROUP}

    def handle(self) -> None:
        print(f"Hello from LimerickCommand v{self.version}")
        opts = {opt.name:self.option(opt.name) for opt in self.options}
        args = {arg.name:self.argument(arg.name) for arg in self.arguments}
        # print(f"I got arguments: {self.arguments.__dict__}")
        # print(f"I got options: {self.options.__dict__}")
        print(f"I got arguments: {args}")
        print(f"I got options: {opts}")
        poetry_file = Factory.locate(Path.cwd())
        config = PyProjectTOML(poetry_file).poetry_config
        print(f"And here's the info about your project: {config}")