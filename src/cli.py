import click
import os

def get_path(ctx, args, incomplete):
    return [k for k in os.listdir() if incomplete in k]


@click.group()
@click.pass_context
def cli(ctx):
    """
        Hello cli space!
    """
    ctx.ensure_object(dict)
    ctx.obj['my_obj'] = "context_string"


@cli.command("command1")
@click.argument("arg1", autocompletion=get_path)
@click.option("-o", "--option", type=click.Choice(["hello", "world"], case_sensitive=False), default="hello")
def command1(arg1, option):
    """
        Hello cli space!
    """
    click.echo(arg1)
    click.echo(option)


@cli.command("command2")
@click.pass_context
def command2(ctx):
    """
        Hello cli space!
    """
    click.echo(ctx.obj['my_obj'])


if __name__ == '__main__':
    cli(obj={})
