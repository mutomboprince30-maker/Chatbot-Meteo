import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialisation du moteur de voix
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # vitesse de parole
engine.setProperty('volume', 1)  # volume max

def parler(texte):
    print("IA :", texte)
    engine.say(texte)
    engine.runAndWait()

def ecouter():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 J'écoute...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        texte = r.recognize_google(audio, language="fr-FR")
        print("Vous :", texte)
        return texte.lower()
    except sr.UnknownValueError:
        parler("Je n'ai pas compris, peux-tu répéter ?")
        return ""
    except sr.RequestError:
        parler("Problème de connexion à internet.")
        return ""

def assistant_vocal():
    parler("Bonjour, je suis ton assistant vocal. Que puis-je faire pour toi ?")

    while True:
        commande = ecouter()

        if "heure" in commande:
            heure = datetime.datetime.now().strftime("%H:%M")
            parler(f"Il est {heure}.")
        
        elif "ouvre youtube" in commande:
            parler("J'ouvre YouTube pour toi.")
            webbrowser.open("https://www.youtube.com")

        elif "ouvre google" in commande:
            parler("J'ouvre Google.")
            webbrowser.open("https://www.google.com")

        elif "ton nom" in commande:
            parler("Je suis ton assistant IA, créé en Python.")

        elif "stop" in commande or "au revoir" in commande:
            parler("Au revoir, à bientôt !")
            break

        elif commande != "":
            parler("Désolé, je ne connais pas encore cette commande.")

# Lancer l'assistant
assistant_vocal()
