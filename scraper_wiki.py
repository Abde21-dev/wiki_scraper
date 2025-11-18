import requests
from bs4 import BeautifulSoup

# On peux changer l'URL avec une autre page, en gardant ?printable=yes à la fin
url = "https://fr.wikipedia.org/wiki/tahiti?printable=yes"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "fr-FR,fr;q=0.9"
}

# Téléchargement de la page
response = requests.get(url, headers=headers)
print("Code de réponse HTTP :", response.status_code)

if response.status_code != 200:
    print("Erreur lors du téléchargement :", response.status_code)
    exit()

# Pour parser le HTML avec BeautifulSoup
html = response.text
print("Taille du HTML reçu :", len(html), "caractères")

soup = BeautifulSoup(html, "html.parser")

paragraphes = soup.find_all("p")
print("Nombre de paragraphes trouvés :", len(paragraphes))

texte_final = ""

for p in paragraphes:
    texte = p.get_text(strip=True)
    if texte:  # on ignore les paragraphes vides
        texte_final += texte + "\n\n"

print("\n===== APERÇU DU CONTENU =====\n")
print(texte_final[:1500])  # on affiche les ~1500 premiers caractères

#Sauvegarde du contenu
nom_fichier = "contenu_wikipedia.txt"
with open(nom_fichier, "w", encoding="utf-8") as f:
    f.write(texte_final)

print(f"\nTout le contenu texte a été enregistré dans le fichier : {nom_fichier}")
