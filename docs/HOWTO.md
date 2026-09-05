### Create virtual environment in PowerShell
* Prerequisite: Python 3.x+ installed
* `cd` to your virtual environment directory
* Run `python -m venv {virtualenv_name}`
* Verify by `ls`. A new folder should be created for the new virtual environment
```
cd ~/venvs
python -m venv venv_basecamp
ls
```

### Activating virtual environment in PowerShell
* `cd` to your virtual environment Scripts directory
* Run `Activate.ps1`
```
cd ~/venvs/venv_basecamp/Scripts
.\Activate.ps1
```