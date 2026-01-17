from subprocess import run

def run_aerich_wise(*args):
    """Run Aerich commands for the WISE database."""
    base_cmd = ["aerich", "-t", "config.tortoise.TORTOISE_ORM", "--location", "migrations/wise"]
    run(base_cmd + list(args), check=True)

def run_aerich_developer(*args):
    """Run Aerich commands for the DEVELOPER database."""
    base_cmd = ["aerich", "-t", "config.tortoise.TORTOISE_ORM", "--location", "migrations/developer"]
    run(base_cmd + list(args), check=True)
