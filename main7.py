import os

from omegaconf import DictConfig, OmegaConf

def main() -> None:
    config_to_merge_1 = OmegaConf.load("./config-to-merge-1.yaml")
    config_to_merge_2 = OmegaConf.load("./config-to-merge-2.yaml")
    config = OmegaConf.merge(config_to_merge_1, config_to_merge_2)

    # can also merge / update using cli
    # python main7.py server.port=82
    config.merge_with_cli()

    print(OmegaConf.to_yaml(config))


if __name__ == "__main__":
    main()