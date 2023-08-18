"""wutils: handy tools
"""
import subprocess
from codecs import open
from os import path

from setuptools import Command, find_packages, setup


class InstallMermaidCLI(Command):
    """Install mermaid-cli"""
    description = "install mermaid-cli"
    user_options = []

    def run(self):
        """
        The run function is the entry point for setuptools.
        It will be called with no arguments and should do whatever your project's setup script does: run other setup commands, print project information, or anything else you want to do before users can use your project.


        :param self: Represent the instance of the class
        :return: A list of strings
        :doc-author: Trelent
        """

        try:
            subprocess.check_call(["npm", "install", "-g", "@mermaid-js/mermaid-cli"])
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e.output}")


here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line]

setup(
    name="metagpt",
    version="0.1",
    description="The Multi-Role Meta Programming Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grahamwaters/MetaGPT_engl.git",
    author=["Alexander Wu", "Graham Waters"],
    author_email="alexanderwu@fuzhi.ai",
    license="Apache 2.0",
    keywords="metagpt multi-role multi-agent programming gpt llm",
    packages=find_packages(exclude=["contrib", "docs", "examples"]),
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "playwright": ["playwright>=1.26", "beautifulsoup4"],
        "selenium": ["selenium>4", "webdriver_manager", "beautifulsoup4"],
    },
    cmdclass={
        "install_mermaid": InstallMermaidCLI,
    },
)
