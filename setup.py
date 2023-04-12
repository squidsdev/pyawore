import setuptools

setuptools.setup(
    name='pyawore',
    version='0.1',
    author='squids',
    description='Awore simple api',
    long_description='See https://github.com/squidsdev/pyawore',
    url='https://github.com/squidsdev/pyawore',
    install_requires=['requests', 'uuid'],
    packages=setuptools.find_packages()
)
