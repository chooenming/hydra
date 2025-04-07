import os
import logging

from omegaconf import DictConfig, OmegaConf
import hydra
from hydra.utils import get_original_cwd, to_absolute_path

logger = logging.getLogger(__name__)

# as all the config files are stored in the directory: configs
@hydra.main(config_path="configs", config_name="config")
def main(config: DictConfig) -> None:
    print(OmegaConf.to_yaml(config))
    logger.info("Some info message")
    logger.debug("Some debug message")

if __name__ == "__main__":
    main()

# using CLI to change logger in debug level, as by default, it is in info level
# python main11.py hydra.verbose=true
# can also do the same by specifying in the yaml file

# using CLI 
# python main11.py --cfg job
# another option: hydra configuration
# python main11.py --cfg hydra
# only specific package
# python main11.py --cfg job --package experiment