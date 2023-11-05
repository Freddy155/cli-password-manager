import click
import json
import secrets
import string
from cryptography.fernet import Fernet
import os

home_directory = os.path.expanduser("~")
hidden_directory = os.path.join(home_directory, ".password-manager")

os.makedirs(hidden_directory, exist_ok=True)

def generate_key():
    return Fernet.generate_key()

def encrypt(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt(data, key):
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()

def load_key():
    key_file = os.path.join(hidden_directory, "key.key")
    if os.path.isfile(key_file):
        with open(key_file, "rb") as file:
            key = file.read()
    else:
        key = generate_key()
        with open(key_file, "wb") as file:
            file.write(key)
    return key

def save_password(encrypted_credentials):
    password_file = os.path.join(hidden_directory, "passwords.json")
    with open(password_file, "wb") as file:
        file.write(encrypted_credentials)

def load_password():
    password_file = os.path.join(hidden_directory, "passwords.json")
    if os.path.isfile(password_file):
        with open(password_file, "rb") as file:
            encrypted_credentials = file.read()
        return encrypted_credentials
    else:
        return None

@click.group()
def cli():
    """Password Manager"""

@cli.command()
def generate_password():
    """Generate a secure password"""
    length = int(input("Enter the desired length of the generated password: "))
    password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
    click.echo(f"Generated Password: {password}")

@cli.command()
def store_password():
    """Store a password securely"""
    service = input("Enter the service name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    
    key = load_key()
    credentials = {
        'service': service,
        'username': username,
        'password': password
    }
    encrypted_credentials = encrypt(json.dumps(credentials), key)
    save_password(encrypted_credentials)
    click.echo(f"Password for {service} stored securely.")

@cli.command()
def retrieve_password():
    """Retrieve a stored password"""
    service = input("Enter the service name: ")
    
    key = load_key()
    encrypted_credentials = load_password()
    if encrypted_credentials:
        credentials = json.loads(decrypt(encrypted_credentials, key))
        if 'service' in credentials and credentials['service'] == service:
            click.echo(f"Service: {credentials['service']}")
            click.echo(f"Username: {credentials['username']}")
            click.echo(f"Password: {credentials['password']}")
        else:
            click.echo(f"No stored password found for service: {service}")
    else:
        click.echo("No stored passwords found.")

if __name__ == '__main__':
    cli()
