import yaml


def getYaml():
    f = open('config.yml', 'r', encoding='utf-8')
    config = yaml.load(f.read(), Loader=yaml.FullLoader)
    return config
