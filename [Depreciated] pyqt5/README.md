# DeepXDE-frontend

⚠️⚠️⚠️ I am going to update the repo's name to DeepINN's frontend. ⚠️⚠️⚠️

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
[![License](https://img.shields.io/github/license/praksharma/DeepXDE-frontend)](https://github.com/praksharma/DeepXDE-frontend/blob/main/LICENSE)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/04e5558c825a4cc09455565ec52a7874)](https://app.codacy.com/gh/praksharma/DeepXDE-frontend/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

A GUI frontend for [DeepINN](https://praksharma.github.io/DeepINN/) made in PyQt5. This project is in alpha unless you see a release.

## Installation
I think the frontend will be released as a compressed `tar.gz` file. You just need to uncompress the archives and install [PyQt5](https://pypi.org/project/PyQt5/) using the following command.

```bash
tar -xvf filename.tar.gz
pip install PyQt5
```

## Contributing to the project

Here are some ways to contribute.

- **Reporting bugs and Suggesting enhancements.** To report a bug, simply open an issue in the GitHub [Issues](https://github.com/praksharma/DeepXDE-frontend/issues).
- **Pull requests.** If you made improvements to the project, fixed a bug, feel free to send us a pull-request.

## The Team
As of now, I am the lone warrior.

## License
[AGPL-3.0 License](https://github.com/praksharma/DeepXDE-frontend/blob/main/LICENSE)

I suggest all the FOSS projects to use the GPL or AGPL license. Want to know [why](https://snyk.io/learn/agpl-license/)?

## Learn GUI development
There are bunch of tools to develop GUIs. [Qt](https://en.wikipedia.org/wiki/Qt_(software)) is a cross platform tool unlike [Visual Studio](https://en.wikipedia.org/wiki/Visual_Studio) on Windows or [GTK](https://en.wikipedia.org/wiki/GTK) on GNOME.

Sometimes, a Qt (written in C++) frontend for a software written in Python, such as DeepXDE may create a lot of issues. Thus, it is best to use PyQt to develop GUIs for Python software.

[This](https://www.geeksforgeeks.org/python-introduction-to-pyqt5/) is an amazing place to kickstart PyQt5. Btw, [PyQt6](https://pypi.org/project/PyQt6/) is already released and I might ship the development to PyQt6.

## Structure of the GUI interface
The `main_window.py` is the main file. One can add more tabs in the `main_tabs.py` file. All tabs are connected to individual classes and reside in the `tabs`  directory. When you add a new tab you can create a new python file in this directory. helper contains some functions that, I think, I will use frequently.

The `config.ini` stores shared strings specific to the GUI such the current working directory.