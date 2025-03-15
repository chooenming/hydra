from omegaconf import DictConfig, OmegaConf

# create configuration using OmegaConf
# def main() -> None:
#     # create config
#     config = OmegaConf.create({
#         "some_key": "some_value",
#         "list_of_times": [1, "2", {"nested_dict_key": "nested_dict_value",
#                                    "nested_list": [1, 2, 3]}]
#     })
#     print(OmegaConf.to_yaml(config))

 # load config.yaml file using OmegaConf
# def main() -> None:
#     config = OmegaConf.load("./config.yaml")
#     print(OmegaConf.to_yaml(config))

# another way to create config
# def main() -> None:
#     my_items = ["training.batch_size=1024",
#                 "training.nrof_epochs=30",
#                 "training.optimizer.lr=5e-3"]
    
#     config = OmegaConf.from_dotlist(my_items)
#     print(OmegaConf.to_yaml(config))

# create config using cmd line
# def main() -> None:
#     config = OmegaConf.from_cli()
#     print(OmegaConf.to_yaml(config))

# cli: python main3.py training.batch_size=1024 training.nrof_epochs=30 training.optimizer.lr=5e-3

# using config file
def main() -> None:
    config = OmegaConf.load("./config.yaml")
    print(OmegaConf.to_yaml(config))

    # get specified value
    print("batch_size:", config.training.batch_size)
    # another to get the value (dictionary style)
    print("batch_size:", config["training"]["batch_size"])

    # overwrite the config value
    config.training.batch_size = 2048
    print("batch_size:", config.training.batch_size)

    # create new config
    config.new_key = "new_value"
    print("new_key:", config.new_key)


if __name__ == "__main__":
    main()