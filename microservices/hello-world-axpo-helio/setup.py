import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hello_world_axpo_helio", # Replace with your own username
    version="0.0.1",
    author="Antonio Hermosilla",
    author_email="ahermosi@everis.com",
    description="Helio Hello World Miroservice",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hermosillaeveris/helio.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
