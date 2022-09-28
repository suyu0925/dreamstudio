from setuptools import setup

setup(
    name="dreamstudio",
    version="0.0.1",
    packages=["dreamstudio"],
    entry_points={
        "console_scripts": [
            "dreamstudio = dreamstudio.__main__:main"
        ]
    },
)
