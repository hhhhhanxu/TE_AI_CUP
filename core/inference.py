import torch
from core import utils
import os

def infer(filename):
    file_name = 'G:/TE/TE_Project_V1.0/data/'+filename # 数据文件名称


    """构造数据集"""
    feature = utils.process_data(file_name)
    feature = torch.tensor(feature, dtype=torch.float32)
    """加载模型"""
    model_load = utils.SimpleNet()
    checkpoint = torch.load(r'G:\TE\TE_Project_V1.0\core\model.pth.tar') # 加载训练好的模型

    model_load.load_state_dict(checkpoint['state_dict'])
    outputs = model_load(feature.reshape(1, 12, 8, 8))

    predict = torch.max(outputs, dim=1)[1]
    print('推断结束')
    if predict==0:
        return "铆压结果为：NOK"
    else:
        return "铆压结果为：OK"

if __name__ == '__main__':
    print(infer(r'G:\TE\TE_Project_V1.0\data\1-结果-CSV_OK_20200608113635.csv'))