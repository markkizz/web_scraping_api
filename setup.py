from setuptools import setup, find_packages


# with open('README.rst') as f:
#     readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

setup(
    name='webscraping',
    version='0.1.0',
    description='simple webscraping api',
    # long_description=readme,
    author='Markkizz',
    author_email='mark.pattanapara@gmail.com',
    url='https://github.com/markkizz/webscraping',
    # license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
