# basecamp

### Working Directory
All commands listed below assume that the working directory is the project root folder.  
```
$> cd ~\basecamp
$> pwd  
~\basecamp

$> ls
docs
lib
...
requirements.txt
webapp.py
```

### Running the app
```
$> python webapp.py
* Serving Flask app 'webapp'
* Debug mode: off
* Running on http://localhost:8080
Press CTRL+C to quit
```

### Running Tests
#### Unit Tests
```
$> pytest -q
===== test session starts =====
...
...
===== n passed in 0.5s =====
```
#### Test Coverage
```
$> pytest --cov=. --cov-report=term-missing --cov-config=.coveragerc
===== test session starts =====
---------- coverage: platform win32, python 3.8.10-final-0 -----------
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
lib\__init__.py                           0      0   100%
...
...
---------------------------------------------------------
TOTAL                                    47      1    98%
```
#### Generating Reports
```
pytest --junitxml=test-results.xml --cov=. --cov-report xml:test-coverage.xml --cov-config=.coveragerc
```  
