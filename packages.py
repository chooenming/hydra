"""
task/model/backbone/resnet18.yaml -> task.model.backbone

1. The most important is the package you specified in the defaults list
2. Next, the package specified in the Package directive
3. Finally, the default package of the config file itself
"""

import hydra
from omegaconf import OmegaConf

@hydra.main(config_path="./packages/configs", config_name="config", version_base=None)
def main(config) -> None:
    print(OmegaConf.to_yaml(config))

if __name__ == "__main__":
    main()