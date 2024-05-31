import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()


__version__="0.0.0"

REPO_NAME = "TextSummarizer"
AUTHOR_USER_NAME="sibiranjan"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "sibiranjan.j2021ai@sece.ac.in"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"":"src"},
    package=setuptools.find_packages(where="src")

)