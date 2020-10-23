from setuptools import setup
setup(
    name = 'E_commerce',
    version = '0.1.0',
    packages = ['Ecom'],
    entry_points = {
        'console_scripts': [
            'E_commerce = E_commerce.__main__:main'
        ]
    })