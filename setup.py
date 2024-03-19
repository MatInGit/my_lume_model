from setuptools import setup, find_packages
from os import path
import versioneer

cur_dir = path.abspath(path.dirname(__file__))

# parse requirements
with open(path.join(cur_dir, "requirements.txt"), "r") as f:
    requirements = f.read().split()

setup(
    name="my_lume_model",
    author="Mat",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    #  license="...",
    install_requires=requirements,
    url="git@github.com:MatInGit/my_lume_model.git",
    include_package_data=True,
    python_requires=">=3.8",
    entry_points={
        "orchestration": [
            "my_lume_model.model=\
                my_lume_model.model:My_Lume_Model",
            "my_lume_model.flow=\
                my_lume_model.flow:flow",
        ]
    },
)
