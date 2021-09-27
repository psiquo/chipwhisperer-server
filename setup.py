import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chipwhisperer-server",
    version="0.1",
    author="psiquo",
    author_email="daviderusconi1@gmail.com",
    url="https://github.com/psiquo/chipwhisperer-server",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'chipwhisperer'
    ],
)