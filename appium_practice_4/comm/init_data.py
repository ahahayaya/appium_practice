import yaml,os
class get_data:
    def __init__(self,file_name):
        self.file_path = os.getcwd() + os.sep +'data' + os.sep + file_name
    def read_yaml(self):
        with open(self.file_path,'r') as f:
            return yaml.load(f)
    def write_yaml(self,data):
        with open(self.file_path,'w') as f:
            return yaml.dump(data,f)
