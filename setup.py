try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Twitter terminal client',
    'author': 'Viorel Sfetea',
    'url': 'http://viorel.sfetea.ro',
    'download_url': 'https://github.com/viorelsfetea/python-twitter-terminal-client.git',
    'author_email': 'viorel.sfetea@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': [],
    'scripts': [],
    'name': 'twitterclient'
}

setup(**config)