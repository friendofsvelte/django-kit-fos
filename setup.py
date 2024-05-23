from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="django-kit-fos",
    version="0.0.101",
    description="Python library to couple Svelte with Django. Use SvelteKit with Django, the easy way.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/friendofsvelte/django-kit-fos",
    py_modules=["django_kit_fos"],
    packages=find_packages(),
    project_urls={
        "Documentation": "https://github.com/friendofsvelte/django-kit",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "Django",
    ]
)
