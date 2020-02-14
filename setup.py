import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="django-wrapwith",
    version="0.0.1",
    author="Jamie Matthews",
    author_email="jamie@dabapps.com",
    description="A Django template tag for wrapping a template block in a reusable enclosing template",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dabapps/django-wrapwith",
    packages=setuptools.find_packages(),
    classifiers=[
        "Topic :: Internet :: WWW/HTTP",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Framework :: Django",
        "Operating System :: OS Independent",
    ]
)
