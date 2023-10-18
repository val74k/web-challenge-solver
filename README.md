# web-challenge-solver

Python program that automatically detects potential flags in an easy web challenge of a CTF


```
pip install requests
pip install beautifulsoup4
```
or
```
pip install -r requirements.txt
```

Change line 7 if there's a different CTF flag format:
```
 flag_pattern = re.compile(r'\w+\{[^\}]*\}')
 flag_pattern = re.compile(r'CTF{\w+}')
```
