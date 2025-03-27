# xpln 🛠️
**xpln** is a python package made available as a CLI tool that explains terminal commands for you to understand what they do before you execute them.

## 📦Installation
xpln is available on PyPI under the package name [`xpln2me`](https://pypi.org/project/xpln2me/). It can be installed by running
```
pip install xpln2me
``` 
At this point, `xpln` should be globally accessible from the terminal!

> [!NOTE]
> On linux, this may not be as straightforward due to restrictions of direct installations of non-Debian-packaged Python packages.
> It's recommended to use `pipx install xpln2me` for this instead which will automatically create a virtual environment to install the package and creates a symlink in `/.local/bin/xpln` pointing to the real executable

## 📌 Usage
### Basic Usage
Run `xpln` on the terminal to begin, or `xpln --help` to get the available commands
![image](https://github.com/user-attachments/assets/14c04108-624d-487d-beec-9ad3eae79863)

`xpln` is powered by Google AI Studio and requires an an [API Key](https://aistudio.google.com/apikey) to initialize.
Once you have an API Key, initialize the CLI by running `xpln init` and following the instructions.

Alternatively, an API Key can be directly specified by including the `--key / -k` option
```sh
xpln init --key <API KEY>
```
```sh
xpln init --update --key <UPDATED API KEY>
```
Once initialized, use the `this` command to get explanations of different commands
```sh
xpln this <COMMAND>
```
### Example Usage
There are 2 ways of using `xpln`:
1. Directly pasting commands into `xpln this`
```sh
xpln this ls -al
```
![image](https://github.com/user-attachments/assets/06f13f54-33d3-4b5d-a145-0c1f6b776731)

2. Piping the input into `xpln this`
```
cat script.sh | xpln this
```
![image](https://github.com/user-attachments/assets/95441a13-5234-46f8-b3d7-c4d3783e3ada)


## ⚙️ Technical Details
### Tools Used
- **Python 3.12** - Core language
- **Poetry** - Dependency & package management
- **Click/Typer** - CLI framework
- **GitHub Actions** - CI/CD automation

### How xpln2me is Packaged
- Python CLI tools can be packaged as:

    - sdist [_Source Distribution]_ - Requires building before installation
    - Wheel (.whl) [_Built Distribution_] - Prebuilt, faster to install

- This project uses Poetry to build and distribute both formats.

### Versioning & Automated Releases
- Uses Semantic Versioning: `MAJOR.MINOR.PATCH`
- On PR merge, GitHub Actions:
    1. Bumps the version
        > This is done by including special indicators in PR titles (commit messages to main)
        > - **#major** - bumps the major version
        > - **#minor** - bumps the minor version
        > - Failure to include one of these bumps the patch version
    2. Creates a Git tag
    3. Publishes to PyPI the new version
