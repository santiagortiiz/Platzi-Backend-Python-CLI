import click


@click.group()
def clients():
    ''' Manage the clients lifecycle '''
    pass

@clients.command()
@click.pass_context
def create(ctx, name, company, email, position):
    ''' Creates a new client '''
    pass

@clients.command()
@click.pass_context
def list(ctx):
    ''' List all clients '''
    pass

all = clients