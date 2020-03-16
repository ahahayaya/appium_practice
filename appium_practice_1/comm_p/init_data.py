import sys,yaml,os
class read_data:
    def __init__(self,filename):
        self.file_name = os.getcwd() + os.sep + "data" + os.sep + filename
    def read_yaml(self):
        with open(self.file_name,"r") as f:
            return yaml.load(f)
    def write_yaml(self,data):
        with open(self.file_name,"w")as f:
            return yaml.dump(data,f)
def get_data():
    data_list = []
    data = read_data("data.yaml").read_yaml().get("Login_data")
    for i in data:
        for o in i.keys():
            data_list.append((o,i.get(o).get("uid"),i.get(o).get("passwd")))
    return data_list