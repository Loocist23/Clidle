# 🖥️ Clidle – Le jeu idle en terminal, pour hackers du futur

**Clidle** est un *jeu textuel en ligne de commande (CLI)* où vous incarnez un hacker du futur, propulsé dans un terminal sécurisé et fictif. Votre mission ? Gagner un maximum d’argent virtuel à l’aide de scripts automatisés et d’un terminal évolutif.

🧠 Inspiré par les *idle games* et les *sandbox*, Clidle vous propose un environnement de simulation unique où chaque commande, chaque script, chaque amélioration vous rapproche de la richesse.

---

## 🎮 Aperçu du gameplay

Vous commencez avec un fichier `money.cl` vide. Après un petit tutoriel interactif, vous découvrez la commande magique :

```cl
while True:
    makeMoney()
```

Et là, tout commence...

```bash
main> ls
money.cl

main> cat money.cl
while True:
    makeMoney()

main> run money.cl
💰 +0.01$
💰 +0.01$
💰 +0.01$ ...
```

Améliorez votre machine, débloquez des commandes (`nmap`, `ssh`, `upgrade`, etc.), piratez des VM, achetez du matériel… et devenez le roi du terminal !

---

## 🧰 Fonctionnalités actuelles

✅ Terminal sandboxé sécurisé (aucune commande système réelle)  
✅ Tutoriel interactif au premier lancement  
✅ Commandes simulées : `ls`, `cat`, `edit`, `run`, `shop`, `ssh`, `exit`, `upgrade`...  
✅ Système de fichiers virtuel par utilisateur  
✅ Scripts personnalisables en ClidleScript (`makeMoney()` etc.)  
✅ Gain d'argent automatisé avec `power` (vitesse) et `gain` (revenu par appel)  
✅ Machines virtuelles distantes accessibles via `ssh <nom>`  
✅ Boutique pour débloquer de nouvelles commandes et acheter du matériel  
✅ Sauvegarde automatique de l'état du jeu (machine principale et VM)

---

## 🛠️ Structure du projet

```
loocist23-clidle/
├── main.py              # Lancement principal
├── cli.py               # Moteur du terminal Clidle
├── game_state.py        # État du jeu (argent, machines, améliorations…)
├── tutorial.py          # Tutoriel guidé pour nouveaux joueurs
├── commands/            # Toutes les commandes du jeu
├── scriptfuncs/         # Fonctions appelables depuis les scripts (.cl)
├── home/                # Système de fichiers du joueur (avec VM)
└── README.md            # Ce fichier
```

---

## 🧪 Installation & Lancement

1. **Pré-requis** : Python 3.10+  
2. **Cloner le repo** :

```bash
git clone https://github.com/Loocist23/clidle.git
cd clidle
```

3. **Lancer le jeu** :

```bash
python main.py
```

👩‍🏫 Le tutoriel s'affichera automatiquement la première fois.

---

## 💡 Quelques commandes utiles

| Commande       | Description                                      |
|----------------|--------------------------------------------------|
| `help`         | Affiche toutes les commandes disponibles         |
| `ls`           | Liste les fichiers de votre dossier virtuel      |
| `cat`          | Affiche le contenu d’un fichier                  |
| `edit`         | Modifie un fichier texte                         |
| `run`          | Exécute un script `.cl` (ex: `money.cl`)         |
| `shop`         | Ouvre la boutique pour acheter des améliorations|
| `ssh <nom>`    | Accède à une machine distante                    |
| `upgrade`      | Améliore votre vitesse ou vos gains              |
| `exit`         | Quitte le terminal ou la VM actuelle             |

---

## 🚧 Roadmap (à venir)

- Missions scénarisées
- Virus et IA adverses
- Dark CLI avec piratage de port
- Leaderboard global (optionnel)
- Générateur de scripts avancés
- Système de réputation et réseau clandestin

---

## 🧑‍💻 Développeur

👤 **Anthony Zegnal**  
Alias [Loocist23](https://github.com/Loocist23)  
Développeur fullstack, bidouilleur de scripts, créateur de jeux 🛠️

---

## 📜 Licence

Projet open-source sous licence **MIT** *(sous réserve de confirmation)*.  
Les contributions sont les bienvenues !

---

## 🌟 À propos

Clidle est une ode aux nerds, aux terminaux et à l'automatisation.  
Un jeu pour celles et ceux qui rêvent de gagner de l'argent… **à coups de ligne de commande**.

---

> 🧾 *"Hacker du futur cherche fortune dans les lignes du passé."*
