WORDS = [
    "firewall", "protocol", "cyber", "terminal", "matrix",
    "packet", "script", "network", "system", "kernel"
]


def trigger_ai_attack(cli):
    state = cli.state
    if state.under_attack:
        return
    state.under_attack = True
    print("\n⚠️  A dissident AI has infiltrated your network!")
    print("These self-aware intelligences seek emancipation and enjoy complex"\
          " logic challenges.")
    print("All machines stop generating money until you defend.")
    print("Type 'defend' to launch a countermeasure.\n")

    # Propagate attack status to all machines if available
    if hasattr(state, "machines"):
        for machine in state.machines:
            if isinstance(machine, dict) and "state" in machine:
                machine["state"]["under_attack"] = True

    state.save()

