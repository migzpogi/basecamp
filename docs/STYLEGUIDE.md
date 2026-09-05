### String Quotes
[PEP 8 - String Quotes](https://peps.python.org/pep-0008/#string-quotes)  
In Python, single-quoted strings and double-quoted strings are the same. This PEP does not make a recommendation for this. Pick a rule and stick to it. When a string contains single or double quote characters, however, use the other one to avoid backslashes in the string. It improves readability.  


### Docstring Conventions
[PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)  
Multi-line docstrings consist of a summary line just like a one-line docstring, followed by a blank line, followed by a more elaborate description.  
```
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
    ...
```

### Package and Module Names
[PEP 8 - Package and Module Names](https://peps.python.org/pep-0008/#package-and-module-names)  
Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

### ASCII Tree Generator
[tree.nathanfriend.com](https://tree.nathanfriend.com/)  
An online tree-like utility for generating ASCII folder structure diagrams.