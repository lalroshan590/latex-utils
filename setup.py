from setuptools import find_packages, setup

setup(
    name='latexutils',
    packages=find_packages(include=['latexutils']),
    version='0.0.1',
    description='LaTeX utils',
    author='Alessandro Sebastianelli',
    license='MIT',
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)
