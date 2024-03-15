import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

REPO_NAME = "NLP-text-summarizer" # connects to my github
AUTHOR_USER_NAME = "rohit-sram"
SRC_REPO = "text_summarizer" # the name of the local (machine) src repo
AUTHOR_EMAIL = "rohitsram10@outlook.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL, 
    description="A Tidy package for text summarization(NLP)", 
    long_description=long_description, 
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}", 
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")    
)
