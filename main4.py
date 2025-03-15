from omegaconf import DictConfig, OmegaConf

def main() -> None:
    config = OmegaConf.load("./config2.yaml")
    print(OmegaConf.to_yaml(config))

    # will get error
    # print(config.training.scheduler)

    config.training.scheduler = "MultiStepLR"
    print(config.training.scheduler)


if __name__ == "__main__":
    main()