import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fastapi-mnist",
    version="0.0.1",
    author="markdavidmc0",
    author_email="mark@thetechbattalion.com",
    description="Prediction API for hand written digits trained on MNIST dataset.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/markdavidmc0/tech-battalion-mnist",
    project_urls={
        "Bug Tracker": "https://github.com/markdavidmc0/tech-battalion-mnist/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "fastapi-mnist"},
    packages=setuptools.find_packages(where="fastapi-mnist"),
    python_requires=">=3.6",
)