# -*- coding: utf-8 -*-
import json

import pandas as pd

def write(filename,datas):
    data = []
    for k, v in datas.items():
        v.file = k
        json_str = json.dumps(v.__dict__)
        json_o = json.loads(json_str)
        data.append(json_o)
    # data_df = pd.DataFrame.from_dict(datas,orient='index',columns=['E'])
    # data_df = data_df.reset_index().rename(columns={'index':'file'})
    data_df = pd.DataFrame(data)
    write = pd.ExcelWriter(filename)
    data_df.to_excel(write,'page_1')
    write.save()