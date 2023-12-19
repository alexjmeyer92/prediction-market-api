from setuptools import find_packages, setup

dependencies = [
    'fastapi[all]==0.63.0',
    'uvicorn >= 0.13.0',
    'numpy >= 1.20.0',
    'pymongo >= 3.11.0'
]

setup(
        name="PredictionMarketApi",
        version="0.1.0",
        description="POC to create an API to facilitate a continuous double auction market",
        packages=find_packages(),
        install_requires=dependencies,
        author="Alex Meyer",
        author_email="alex@alxmyr.com",
        maintainer="Alex Meyer",
        maintainer_email="alex@alxmyr.com",
        url="https://github.com/alexjmeyer92/prediction-market-api",
        license='MIT',

)
