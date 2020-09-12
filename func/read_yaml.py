import yaml
import os
def readYaml(file_name,key=None,key1=None):
    curPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    yamlPath =curPath +  "\\ui\\config\\{0}".format(file_name)
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    d = yaml.safe_load(cfg)
    if key1 is None and key is None:
        return d
    elif key != None and key1 == None:
        return d[key]
    else:
        return d[key][key1]
