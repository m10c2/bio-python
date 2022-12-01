import requests
import re
import numpy as np
from numpy import nan

def get_data(gen_name, count):
        url = f'https://www.kegg.jp/ssdb-bin/ssdb_best?org_gene={gen_name}'
        resp = requests.get(url=url)
        
        r_block = r"<INPUT(.)*</a>"
        r_name = r"[a-z]+:[0-9]+"
        r_numbers = r"[0-9]+ \s+ ([0-9]+)\s+\(.*\) \s+ [0-9]+ \s+ ((0|[1-9]\d*)([.,]\d+))"
        
        orthologs = []
        sw_score = []
        identity = []

        blocks = re.finditer(r_block, resp.text)
        for i,block in enumerate(blocks):
                
                name = re.search(r_name, block.group()).group()
                data = re.search(r_numbers, block.group())
                
                orthologs.append([name, data.group(1), data.group(2)])
                sw_score.append(int(data.group(1)))
                identity.append(float(data.group(2)))

                if i >= count - 1:
                        return sw_score, identity

        return sw_score, identity

def corr(data1, data2):
        data1, data2 = np.array(data1), np.array(data2)
        pcm = np.corrcoef(data1, data2)

        if np.isnan(pcm[0][1]):
                return 0
        else:
                return pcm[0][1]


def compare(gen_name):
        x1, y1 = get_data(gen_name, 10)
        corr1 = corr(x1, y1)

        x2, y2 = get_data(gen_name, 100)
        corr2 = corr(x2, y2)

        print('corr1 =', corr1,', corr2 =', corr2)
        print('корреляция увеличилась' if corr1 > corr2 else 'корреляция уменьшилась')

                
gen_name = 'hsa:7314'
compare(gen_name)




















