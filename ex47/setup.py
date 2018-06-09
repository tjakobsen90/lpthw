except ImportError:
	from distutils.core import setup

config = {
	'description': 'Excersise 47',
	'author': 'Tijmen Jakobsen',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'tjakobsen@live.nl',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'ex47'
}

setup(**config)
