from setuptools import find_packages, setup


setup(
    name="project-b-utils",
    version="1.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="SunRay",
    description=(
        "Utilities for dates, strings, "
        "files and logging"
    ),
    python_requires=">=3.8",
)