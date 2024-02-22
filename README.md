# MyModel

This repository packages the `Mymodel` in `mymodel/model.py ` for execution with [Prefect](https://docs.prefect.io/) using the flow described in `mymodel/flow/flow.py` using the variables:

<!--- The input and output variable tables are replaced when generating the project in template/hooks/post_gen_project.py-->
# input_variables
|variable name| type |default|
|-------------|------|------:|
|input1       |scalar|      1|
|input2       |scalar|      2|


# output_variables
|variable_name| type |
|-------------|------|
|output2      |scalar|
|output3      |scalar|



## Installation

This package may be installed using pip:
```
pip install git+https://github.com/MatInGit/my_lume_model.git
```


## Dev

Install dev environment:
```
conda env create -f dev-environment.yml
```

Activate your environment:
```
conda activate mymodel-dev
```

Install package:
```
pip install -e .
```

Tests can be executed from the root directory using:
```
pytest .
```

### Note
This README was automatically generated using the template defined in https://github.com/slaclab/lume-services-model-template with the following configuration:

```json
{
    "author": "Mat",
    "email": "mateusz.leputa@stfc.ac.uk",
    "github_username": "MatInGit",
    "github_url": "https://github.com/MatInGit/my_lume_model.git",
    "project_name": "MyModel", 
    "repo_name": "mymodel", 
    "package": "mymodel",
    "model_class": "Mymodel"
}
```
