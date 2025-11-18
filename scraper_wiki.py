import requests
from bs4 import BeautifulSoup

# L'URL de la page Wikipédia à scraper
url = "https://fr.wikipedia.org/wiki/Cordill%C3%A8re_des_Andes"

# On ajoute un "User-Agent" pour imiter un vrai navigateur
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "fr-FR,fr;q=0.9"
}

# Télécharger le contenu de la page
response = requests.get(url, headers=headers)

print("Code de réponse HTTP :", response.status_code)

# Vérifier que le téléchargement s'est bien passé
if response.status_code != 200:
    print("Erreur lors du téléchargement :", response.status_code)
    exit()

# Analyser le HTML avec BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Récupérer le titre de la page
titre = soup.find("h1").text
print("Titre de la page :", titre)

# Récupérer le premier vrai paragraphe
paragraphe = None
for p in soup.find_all("p"):
    texte = p.get_text(strip=True)
    if texte:  # si le paragraphe contient du texte
        paragraphe = texte
        break

print("\nPremier paragraphe :\n")
print(paragraphe)

# Récupérer tous les titres de sections (h2)
print("\nTitres des sections :")
sections = soup.find_all("h2")

for s in sections:
    titre_section = s.text.strip()
    titre_section = titre_section.replace("[modifier | modifier le code]", "")
    print("-", titre_section)

