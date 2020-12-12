import click

@click.command()
def cli():
    """
        Hello cli space!
    """
    click.echo("hello world")

if __name__ == '__main__':
    cli()
