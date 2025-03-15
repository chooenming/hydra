import os

from omegaconf import DictConfig, OmegaConf

def main() -> None:
    os.environ["USER"] = "enming"
    os.environ["PASSWORD1"] = "some_password"

    config = OmegaConf.load("./environment-variables-config.yaml")
    print(OmegaConf.to_yaml(config, resolve=True))


if __name__ == "__main__":
    main()


# another way to set os.environ
# using cli: PASSWORD2=some_other_password python main6.py