import os
from random import SystemRandom


def generate_secret_key():
    """
    Returns a securely generated random string.
    """
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)'
    return ''.join(SystemRandom().choice(allowed_chars) for i in range(50))


def make_secret_key(project_directory):
    """Generates and saves random secret key"""
    # Determine the setting_file_location
    setting = os.path.join(project_directory, 'env.txt')

    with open(setting) as f:
        file_ = f.read()

    # Replace "CHANGEME!!!" with SECRET_KEY
    file_ = file_.replace('{SECRET_KEY}', generate_secret_key(), 1)

    # Write the results to the file
    with open(setting, 'w') as f:
        f.write(file_)


# 1. Generates and saves random secret key
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
make_secret_key(PROJECT_DIRECTORY)
