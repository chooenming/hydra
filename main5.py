from omegaconf import OmegaConf, DictConfig

def main() -> None:
    config = OmegaConf.load("./variable-interpolation-config.yaml")
    print(OmegaConf.to_yaml(config, resolve=True)) # if dont put resolve=True here, will not resolve the variable interpolation

if __name__ == "__main__":
    main()