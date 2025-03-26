Installation de pip (si non installé)
Sur Windows :

sh

python -m ensurepip --default-pip
Sur Linux/macOS :

sh

sudo apt install python3-pip  # (Ubuntu/Debian)
brew install python           # (macOS, si Homebrew est installé)
Vérifie l'installation avec :

sh

pip --version
🔹 Installation de la bibliothèque glpi
Si une bibliothèque officielle glpi pour Python n'existe pas, tu devras utiliser requests pour interagir avec l'API REST de GLPI.

sh

pip install requests python-dotenv
Si une bibliothèque spécifique GLPI existe sur PyPi, tu peux essayer :

sh
pip install glpi ou telecharger glpi sur: https://glpi-project.org/fr/telecharger-glpi/
✅ Ajout au requirements.txt
Ajoute ces lignes dans ton requirements.txt pour faciliter l'installation sur un autre environnement :

nginx

requests
python-dotenv
Ensuite, pour installer toutes les dépendances :

sh

pip install -r requirements.txt
