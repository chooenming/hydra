from main3 import OmegaConf, DictConfig
import hydra

@hydra.main(config_path=None)
# the decorator will pass the config_path to the function
def main(config: DictConfig) -> None:
    print(OmegaConf.to_yaml(config)) # convert the config file to yaml format and print it

if __name__ == "__main__":
    main()
