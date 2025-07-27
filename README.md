# 🖥️ Clidle – The terminal idle game for future hackers

**Clidle** is a *command line idle game* where you play as a hacker of the future inside a secure fictional terminal. Your goal is to earn as much virtual money as possible using automated scripts and an upgradable terminal.

🧠 Inspired by *idle games* and *sandbox* environments, Clidle offers a unique simulation where each command, script and upgrade brings you closer to wealth.

---

## 🎮 Gameplay preview

You start with an empty `money.cl` file. After a short interactive tutorial you discover the magic command:

```cl
while True:
    makeMoney()
    upgrade()
```

Then the game begins...

```bash
main> ls
money.cl

main> cat money.cl
while True:
    makeMoney()
    upgrade()

main> run money.cl
💰 +0.01$
💰 +0.01$
💰 +0.01$ ...
```

Upgrade your machine, unlock commands (`nmap`, `ssh`, `upgrade`, etc.), hack VMs, buy hardware… and become the king of the terminal!

---

## 🧰 Current features

✅ Secure sandboxed terminal (no real system commands)
✅ Interactive tutorial on first launch
✅ Simulated commands: `ls`, `cat`, `edit`, `run`, `create`, `shop`, `ssh`, `exit`, `upgrade`...
✅ `idle` module (with `jobs`/`stop` commands) to purchase in the shop (unlocked after earning $200, costs $50)
✅ Per-user virtual filesystem
✅ Customizable scripts in ClidleScript (`makeMoney()`, `upgrade()` etc.)
✅ Automated money gain with `power` (speed) and `gain` (income per call)

✅ Remote virtual machines accessible via `ssh <name>`
✅ Shop to unlock new commands and buy hardware
✅ Automatic save of game state (main machine and VMs)

---

## 🛠️ Project structure

```
loocist23-clidle/
├── main.py              # Main entry point
├── cli.py               # Clidle terminal engine
├── game_state.py        # Game state (money, machines, upgrades…)
├── tutorial.py          # Guided tutorial for new players
├── commands/            # All game commands
├── scriptfuncs/         # Functions callable from scripts (.cl)
├── home/                # Player filesystem (with VMs)
└── README.md            # This file
```

---

## 🧪 Installation & launch

1. **Requirements**: Python 3.10+
2. **Clone the repo**:

```bash
git clone https://github.com/Loocist23/clidle.git
cd clidle
```

3. **Start the game**:

```bash
python main.py
```

👩‍🏫 The tutorial will appear automatically the first time.

---

## 💡 Useful commands

| Command        | Description                                       |
|----------------|---------------------------------------------------|
| `help`         | Display all available commands                     |
| `ls`           | List files in your virtual folder                  |
| `cat`          | Show a file’s content                              |
| `edit`         | Edit a text file                                  |
| `run`          | Execute a `.cl` script (e.g. `money.cl`)           |
| `idle`         | Run a script in the background (after purchase)    |
| `jobs`         | List scripts launched with `idle` (after purchase) |
| `stop <id>`    | Stop a background script (after purchase)          |
| `create`       | Create a new `.cl` script                          |
| `shop`         | Open the shop to buy upgrades                      |
| `ssh <name>`   | Connect to a remote machine                        |
| `upgrade`      | Improve your speed or gains                        |
| `exit`         | Leave the terminal or current VM                   |

---

## 🚧 Roadmap (planned)

- Story missions
- Viruses and enemy AIs
- Dark CLI with port hacking
- Optional global leaderboard
- Advanced script generator
- Reputation system and underground network

---

## 🧑‍💻 Developer

[Loocist23](https://github.com/Loocist23)
Fullstack developer, script tinkerer and game creator 🛠️

---

## 📜 License

Open-source project released under the **MIT** license *(subject to confirmation)*.
Contributions are welcome!

---

## 🌟 About

Clidle is an ode to nerds, terminals and automation.
A game for those who dream of earning money… **one command line at a time**.

---

> 🧾 *"Future hacker seeks fortune in the lines of the past."*
