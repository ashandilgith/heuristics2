import click 
#importing the click library which was installed by makefile installation (taken from requirements.txt)

db = {
    "users" : []
}

#users are stored as a list in this dictionary, where the keyword is users 


#the click.group command creates a group of commands instead of just one command. We will now have a group of commands coming under this group

@click.group()
def cli():
    """Simple tool for cli management"""
    pass
#this function doesn't do anything but just creates a container for the other commands. 



@click.command()
#sets the command coming immediately below as one of the functions in the click group called cli established in line 14
@click.argument('name')
#defines a required command line argument called 'name'

def add_user(name):
    """Adds a new user to the database"""
    db["users"].append(name) #appends the users list of the database, created in line 5 with the new name just passed

    click.echo(f"User '{name}' added") #prints a message to console confirming adding the name 


@click.command()

def list_users():
    "Lists all the users in the database"

    if not db["users"]:
        click.echo("no users found")
    else:
        click.echo ("users")

        for user in db["users"]:
            click.echo(f"{user}")



cli.add_command(add_user)
cli.add_command(list_users)

if __name__== "__main__":

    cli()
