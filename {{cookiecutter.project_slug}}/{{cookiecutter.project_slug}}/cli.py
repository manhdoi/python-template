import click


@click.group()
def cli():
    pass


@cli.command()
def version():
    from {{cookiecutter.project_slug}}.version import version
    print(version)
