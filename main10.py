import os

from omegaconf import DictConfig, OmegaConf
import hydra
from hydra.utils import get_original_cwd, to_absolute_path

# as all the config files are stored in the directory: configs
@hydra.main(config_path="configs", config_name="config")
def main(config: DictConfig) -> None:
    print(OmegaConf.to_yaml(config))
    print("CURRENT WORKING DIRECTORY: ", os.getcwd()) # show output directory
    print("ORIGINAL WORKING DIRECTORY: ", get_original_cwd()) # show the directory of where the script is running
    print("TO ABSOLUTE PATH('some_file.txt)", to_absolute_path("some_file.txt"))

if __name__ == "__main__":
    main()