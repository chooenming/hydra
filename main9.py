from omegaconf import DictConfig, OmegaConf
import hydra

# as all the config files are stored in the directory: configs
@hydra.main(config_path="configs", config_name="config")
def main(config: DictConfig) -> None:
    print(OmegaConf.to_yaml(config))

if __name__ == "__main__":
    main()

# multi-run using CLI
# python main9.py -m experiment=experiment-with-resnet18,experiment-with-resnet50
# python main9.py --multirun experiment=experiment-with-resnet18,experiment-with-resnet50

# sweep over all combinations of the experiments and loss functions
# python main9.py -m experiment=experiment-with-resnet18,experiment-with-resnet50 loss_function=arcface,cosface,softmax

# another cli syntax to run all experiments
# python main9.py -m experiment='glob(*)'

# run all but excluding certain keywords
# python main9.py -m experiment='glob(*)' loss_function='glob(*, exclude=soft*)'
