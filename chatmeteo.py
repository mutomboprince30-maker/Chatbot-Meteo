import requests

# ====== CONFIGURATION ======
API_KEY = "b4cfac75d49d4db7ba5171109253010"  # remplace par ta vraie clé
BASE_URL = "https://api.weatherapi.com/v1/current.json"

print("🤖 Bonjour ! Je suis ton assistant météo 🌦️")
print("Tape 'quit' pour quitter.\n")

while True:
    ville = input("👉 Entrez le nom d'une ville : ")

    if ville.lower() == "quit":
        print("👋 Au revoir !")
        break

    # Construction du lien vers l'API
    params = {
        "key": API_KEY,
        "q": ville,
        "lang": "fr"  # langue française
    }

    # Appel de l’API
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        nom_ville = data["location"]["name"]
        pays = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidite = data["current"]["humidity"]

        print(f"\n📍 Météo à {nom_ville}, {pays} :")
        print(f"   🌡️ Température : {temperature}°C")
        print(f"   🌤️ Condition : {condition}")
        print(f"   💧 Humidité : {humidite}%\n")

    else:
        print("❌ Erreur : impossible d'obtenir la météo. Vérifie la ville ou ta clé API.\n")
