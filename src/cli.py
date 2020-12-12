import click

@click.group()
def cli():
    """
        Hello cli space!
    """


@cli.command("command1")
@click.argument("arg1")
@click.option("-o", "--option", default="hello")
def command1(arg1, option):
    """
        Hello cli space!
    """
    click.echo(arg1)
    click.echo(option)


@cli.command("command2")
def command2():
    """
        Hello cli space!
    """
    click.echo("Command2")


if __name__ == '__main__':
    cli()
