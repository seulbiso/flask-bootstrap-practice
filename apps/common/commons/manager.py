# from flask_script import Manager
import click

from apps.controllers.router import create_app 
from config import Config


app = create_app()

@app.cli.command("runserver")
@click.option('-h', '--host', default=Config.APP_HOST)
@click.option('-p', '--port', default=Config.APP_PORT)
def runserver(host, port):
    """run flask server"""
    app.run(host, port=int(port))
