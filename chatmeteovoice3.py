import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests

# --- Configuration météo (WeatherAPI) ---
API_KEY = "b4cfac75d49d4db7ba5171109253010"
URL_METEO = "https://api.weatherapi.com/v1/current.json"

# --- Initialisation de la voix ---
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1)

def parler(texte):
    print("IA :", texte)
    engine.say(texte)
    engine.runAndWait()

def ecouter():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 J'écoute...")
        audio = r.listen(source)
    try:
        texte = r.recognize_google(audio, language="fr-FR")
        print("Vous :", texte)
        return texte.lower()
    except:
        return ""

def get_meteo(ville):
    params = {"key": API_KEY, "q": ville, "lang": "fr"}
    response = requests.get(URL_METEO, params=params)
    if response.status_code == 200:
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        feels = data["current"]["feelslike_c"]
        return f"À {ville}, il fait actuellement {temp} degrés, avec {condition}. On le ressent comme {feels} degrés."
    else:
        return "Désolé, je n'ai pas trouvé la météo pour cette ville."

def assistant_vocal():
    parler("Bonjour, je suis ton assistant vocal. Que puis-je faire pour toi ?")

    attente_ville = False  # variable mémoire

    while True:
        commande = ecouter()

        if attente_ville:  # si on attend une ville
            ville = commande.strip()
            if ville:
                meteo = get_meteo(ville)
                parler(meteo)
            else:
                parler("Je n'ai pas entendu la ville.")
            attente_ville = False  # on revient au mode normal
            continue

        if "heure" in commande:
            heure = datetime.datetime.now().strftime("%H:%M")
            parler(f"Il est {heure}.")
        
        elif "météo" in commande or "temps" in commande:
            parler("Pour quelle ville veux-tu la météo ?")
            attente_ville = True  # on attend la prochaine réponse (ville)
        
        elif "ouvre youtube" in commande:
            parler("J'ouvre YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif "ouvre google" in commande:
            parler("J'ouvre Google.")
            webbrowser.open("https://www.google.com")

        elif "stop" in commande or "au revoir" in commande:
            parler("Au revoir, à bientôt !")
            break

        elif commande != "":
            parler("Désolé, je ne connais pas encore cette commande.")

# --- Lancer l'assistant ---
assistant_vocal()
