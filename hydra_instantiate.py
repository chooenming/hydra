import hydra
from omegaconf import DictConfig
from hydra.utils import instantiate
import torch

class MyClass:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def say_hello(self) -> None:
        print(f"Hello, {self.name}!")

# using normal class way
# def main() -> None:
#     my_class = MyClass(name= "John")
#     my_class.say_hello()

# using hydra instantiate
@hydra.main(config_path=".", config_name="hydra_config", version_base=None)
def main(config: DictConfig) -> None:
    my_class = MyClass(name= "John")
    my_class.say_hello()

    my_class_hydra = instantiate(config.my_class)
    my_class_hydra.say_hello()

    parameters = torch.nn.Parameter(torch.randn(10, 10))
    partial_optimizer = instantiate(config.optimizer)
    optimzer = partial_optimizer([parameters])
    print(optimzer)

if __name__ == "__main__":
    main()