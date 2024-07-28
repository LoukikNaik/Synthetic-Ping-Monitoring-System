import yaml

def read_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = yaml.safe_load(file)
            return content

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return None

    except yaml.YAMLError as e:
        print(f"There is a possible syntax error in '{file_path}'.")
        print(f"Details: {e}")
        return None

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    config_file_path = "test.yaml" 
    config = read_yaml_file(config_file_path)

    if config is not None:
        print("YAML file loaded successfully!")
        print(config)
    else:
        print("Failed to load the YAML file.")
