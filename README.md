# web-challenge-solver

Programme python qui détecte automatiquement des potentiels flag sur un challenge web facile d'un CTF


```
pip install requests
pip install beautifulsoup4
```
or
```
pip install -r requirements.txt
```

changer ligne 7 si il y a un format de ctf :
```
 flag_pattern = re.compile(r'\w+\{[^\}]*\}')
 flag_pattern = re.compile(r'CTF{\w+}')
```
