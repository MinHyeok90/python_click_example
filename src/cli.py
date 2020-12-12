import click

@click.group()
def cli():
    """
        Hello cli space!
    """


@cli.command("command1")
def command1():
    """
        Hello cli space!
    """
    click.echo("Command1")


@cli.command("command2")
def command2():
    """
        Hello cli space!
    """
    click.echo("Command2")


if __name__ == '__main__':
    cli()
