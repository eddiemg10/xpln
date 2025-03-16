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

### Example Usage
```sh
xpln this ls -al
```

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
