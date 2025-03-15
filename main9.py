from omegaconf import DictConfig, OmegaConf
import hydra

# as all the config files are stored in the directory: configs
@hydra.main(config_path="configs", config_name="config")
def main(config: DictConfig) -> None:
    print(OmegaConf.to_yaml(config))

if __name__ == "__main__":
    main()