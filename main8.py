from omegaconf import DictConfig, OmegaConf
import hydra

# as all the config files are stored in the directory: configs
@hydra.main(config_path="configs", config_name="config")
def main(config: DictConfig) -> None:
    print(OmegaConf.to_yaml(config))

if __name__ == "__main__":
    main()

# ./configs/config.yaml is an empty file
# add values to the config file = setting default value

# use cli
# python main8.py +experiment=experiment-with-resnet18
# have to use "+" as config file is empty

# overwrite the config
# python main8.py +experiment=experiment-with-resnet18 experiment.learning_rate=3e-4