# web-challenge-solver

script python qui détecte automatiquement des potentiels flag sur un challenge web d'un CTF

pip install requests
pip install beautifulsoup4


or pip install -r requirements.txt


changer ligne 7 en quand de paterne 
 flag_pattern = re.compile(r'\w+\{[^\}]*\}')
 flag_pattern = re.compile(r'CTF{\w+}') par exemple
