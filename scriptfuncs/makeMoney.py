def run(cli, *args):
    cli.state.balance += cli.state.income_per_call
    cli.state.total_money_earned += cli.state.income_per_call
