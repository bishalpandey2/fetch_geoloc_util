from setuptools import setup, find_packages

setup(
    name="fetch-geoloc-util",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=["requests"],
    entry_points={
        'console_scripts': [
            'geoloc-util=main:main'  # Updated CLI command
]
    },
)
