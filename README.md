# Hydra
Python package that simplifies the configuration management

`main.py` refers to using hydra in python and cmd
`main2.py` refers to using `config.yaml` file
`main3.py` refers to OmegaConf

For `config2.yaml`, to make the field mandatory to fill in while calling the yaml, use ???
Else, will raise an error if not specified
Refer to the code main4.py

For `variable-interpolation-config.yaml`, this is to show OmegaConf ability to interpolate variables
Refer to the code main5.py

For `environment-variables-config.yaml`, this is to show how to use environment variables in YAML configuration files
Refer to the code main6.py

For `config-to-merge-1.yaml`, `config-to-merge-2.yaml`, these are two show how to merge multiple config files
Refer to the code main7.py

For grouping config files (in a directory), refer to the code main8.py and configs directory
To select default config: insert values to ./configs/config.yaml
Need to use keyword `override` if want to override the configs in config.yaml

