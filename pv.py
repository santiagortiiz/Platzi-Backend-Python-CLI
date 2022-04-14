import click

from clients import commands as client_commands

@click.group() # Indicates the entry point
@click.pass_context
def cli(ctx):
    ctx.obj = {}


cli.add_command(client_commands.all)