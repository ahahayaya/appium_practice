import os,yaml
def read_yaml(file):
    file_name= os.getcwd() + os.sep+ "Data" + os.sep+file
    with open(file_name,'r') as f:
        data = yaml.load(f).get('test_data')
    data_list=[]
    for i in data:
        for j in i.keys():
            data_list.append((i.get(j).get('acceptor'),i.get(j).get('message')))
    return data_list



