<h1>Poetry Plugin Limerick</h1>

Limerick is a Poetry plugin that leverages a modified version of cookiecutter taking values from your pyproject.toml file to fill in template values. It was created to improve fidelity of code compared to using poetry and cookiecutter seperately. It is backwards compatible with cookiecutter so you can use your existing projects. 

<h2>Example</h2>

Limerick will use the values from the following pyproject.toml to fill in the values of your cookiecutter (as long as you have the values in your cookiecutter.json). If the corresponding .json value is not found in the toml file Limerick will ask the user to input it (the same as cookiecutter).

```toml
# pyproject.toml

[tool.poetry]
name = "hey_there_world"
version = "0.1.1"
description = "Created using limerick!"
authors = ["landowark <lando.wark@gmail.com>"]
readme = "README.md"
```

cookiecutter with default values.

```json
// cookiecutter.json
{
    "name":"hello_world",
    "description":"This project was created to...",
    "authors": "Landon Wark <lando.wark@gmail.com>",
    "readme": "Boring.md"
}
```
```
├── cookiecutter.json
├── {{ cookiecutter.name }}
│   ├── poetry.toml
│   ├── pyproject.toml
│   ├── {{ cookiecutter.readme }}
│   └── src
│       └── {{ cookiecutter.name }}
│           ├── __init__.py
│           └── __main__.py
```
File structure after running:
```bash
poetry limerick <path or url of your cookiecutter>
```
```
├── cookiecutter.json
├── hey_there_world
│   ├── poetry.toml
│   ├── pyproject.toml
│   ├── README.md
│   └── src
│       └── hey_there_world
│           ├── __init__.py
│           └── __main__.py
```

<h2>Arguments</h2>

template,
    Path or url of the cookiecutter template. Required. 
    
output_dir, 
    Where resulting files are placed. Optional, default="."

<H2>Options</h2>

"--checkout", "-c",
    The branch, tag or commit ID to checkout after clone,
    flag=False,
    
"--no-input", "-i"
    Prompt the user at command line for manual configuration,
    flag=True,

"--extra-context", "-e",
    A dictionary of context that overrides default and user configuration,
    flag=False,
    
"--replay", "-r",
    Do not prompt for input, instead read from saved json. If ``True`` read from the ``replay_dir`` if it exists
    flag=True,
        
"--overwrite-if-exists", "-o",
    Overwrite the contents of the output directory if it exists,
    flag=True,
    
"--config-file", "-x",
    User configuration file path,
    flag=False,

"--default-config", "-d",
    Use default values rather than a config file,
    flag=True,
        
"--password", "-p",
    The password to use when extracting the repository,
    flag=False,
    
"--directory", "-b",
    Relative path to a cookiecutter template in a repository,
    flag=False,            

"--skip-if-file-exists", "-s",
    Skip the files in the corresponding directories if they already exist,
    flag=True,
    
"--deny-hooks", 
    Don't run pre and post hooks if set to `True`,
    flag=True,
    
"--override-toml", "-t",
    Use user input instead of pyproject.toml (i.e. default cookiecutter behaviour),
    flag=True,
    
"--keep-project-on-failure", "-k", 
    If `True` keep generated project directory even when generation fails,
    flag=True,
    

<h2>FAQ</h2>

*Couldn't I just use poetry and cookiecutter seperately?*<br/>
Boy could you. But that would mean answering 2 sets of questions, one from poetry and one from cookiecutter and come on, you're too lazy for that.

*Why did you make an altered version of cookiecutter? Couldn't you just import the module?*<br/>
Unfortunately to make an interface between cc and poetry's cleo commandline I needed to make some changes to how cookiecutter worked. If cc had used an object structure I likely could have imported and overridden some functions, but, alas, cc is almost entirely functionally based.

*Did you make any other changes while you were in there?*<br/>
Yes. I mucked around with the path finding a bit and, instead of the system git Limerick makes use of the dulwich python package as a fallback so you can use it even if you don't have git installed.