import click

@click.group("mycmd")
def mycmd():
    """
        Hello mycmd space!
    """

@mycmd.command("method")
def firstmethod():
    """
        Hello mycmd space!
    """
    click.echo("hello world!")

if __name__ == '__main__':
    mycmd()