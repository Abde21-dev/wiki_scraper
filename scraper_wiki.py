import requests
from bs4 import BeautifulSoup

# L'URL de la page Wikipédia à scraper
url = "https://fr.wikipedia.org/wiki/Annapurna"

# Téléchargement
response = requests.get(url)


if response.status_code == 200:
    print("Page téléchargée avec succès !")
else:
    print("Erreur lors du téléchargement :", response.status_code)
    exit()

# Analyser le HTML avec BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Récupérer le titre de la page
titre = soup.find("h1").text
print("Titre de la page :", titre)

# Récupérer le premier paragraphe
paragraphe = soup.find("p").text
print("\nPremier paragraphe :\n")
print(paragraphe)

# Récupérer tous les titres de sections (h2)
print("\nTitres des sections :")
sections = soup.find_all("h2")

for s in sections:
    titre_section = s.text.strip()
    # Wikipédia met parfois "[modifier | modifier le code]", on le retire
    titre_section = titre_section.replace("[modifier | modifier le code]", "")
    print("-", titre_section)
