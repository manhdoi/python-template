import click


@click.group()
def cli():
    pass


@cli.command()
def version():
    pass
