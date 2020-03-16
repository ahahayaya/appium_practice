import yaml,os,sys
print('workddir',os.getcwd())
def get_data():
    with open('login_data.yaml', 'r', encoding='utf-8') as f:
        data_1 = yaml.load(f).get('data')
    data_list = []
    for i in data_1:
        for j in i:
            data_list.append((j, i.get(j).get('phone'), i.get(j).get('pwd'), i.get(j).get('except')))
    return data_list

