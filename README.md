# Assistant Vocal Python (Speech Recognition + WeatherAPI)

Ce projet est un **assistant vocal en Python** capable d’écouter l’utilisateur, comprendre des commandes simples, répondre oralement et fournir la météo grâce à l’API **WeatherAPI**.

## 🎤 Fonctionnalités

* Écoute vocale (SpeechRecognition)
* Réponse vocale (pyttsx3)
* Donne l’heure actuelle
* Donne la météo d’une ville via **WeatherAPI**
* Ouvre YouTube et Google dans un navigateur
* Comprend des commandes simples
* Possibilité d’arrêter l’assistant avec "stop" ou "au revoir"

---

## 📦 Installation

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/TON-UTILISATEUR/assistant-vocal.git
cd assistant-vocal
```

### 2️⃣ Créer un environnement virtuel (recommandé)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux / macOS
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration API (WeatherAPI)

Ce projet utilise
👉 [https://www.weatherapi.com/](https://www.weatherapi.com/)

Dans le code, modifiez la clé :

```python
API_KEY = "VOTRE_CLE_API"
```

---

## ▶️ Exécution du programme

```bash
python assistant.py
```

Assurez-vous d’avoir :

* un **microphone fonctionnel**
* une **connexion Internet**

---

## 🧩 Structure du projet

```
assistant-vocal/
│── assistant.py
│── requirements.txt
│── README.md
```

---

## 🔧 Problèmes fréquents

### ✔ Erreur : "No module named PyAudio"

Installez PyAudio selon votre OS :

🔹 **Windows** : télécharger la roue sur
[https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

Puis :

```bash
pip install nom_du_fichier_whl
```

🔹 **Linux** :

```bash
sudo apt install portaudio19-dev python3-pyaudio
```

---

## 📜 Licence

Libre d'utilisation à des fins éducatives.
