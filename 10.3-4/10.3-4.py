import requests
import re
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

from gene import Gene

def get_data(gen_name, count):
        url = f'https://www.kegg.jp/ssdb-bin/ssdb_best?org_gene={gen_name}'
        resp = requests.get(url=url)
        
        r_block = r"<INPUT(.)*</a>"
        r_name = r"[a-z]+:[0-9]+"
        r_numbers = r"[0-9]+ \s+ ([0-9]+)\s+\(.*\) \s+ [0-9]+ \s+ ((0|[1-9]\d*)([.,]\d+))"
        
        orthologs = []
        sw_score = []
        identity = []
        names = []
        
        blocks = re.finditer(r_block, resp.text)
        for i,block in enumerate(blocks):
                
                name = re.search(r_name, block.group()).group()
                data = re.search(r_numbers, block.group())
                
                orthologs.append([name, int(data.group(1)), float(data.group(2))])
                sw_score.append(int(data.group(1)))
                identity.append(float(data.group(2)))
                names.append(name)

                if i >= count - 1:
                        return sw_score, identity, names

        return sw_score, identity, names

def corr(data1, data2):
        data1, data2 = np.array(data1), np.array(data2)
        pcm = np.corrcoef(data1, data2)

        if np.isnan(pcm[0][1]):
                return 0
        else:
                return pcm[0][1]

def compare(gen_name):
        x1, y1, foo1 = get_data(gen_name, 10)
        corr1 = corr(x1, y1)

        x2, y2, foo2 = get_data(gen_name, 100)
        corr2 = corr(x2, y2)

        print('corr1 =', corr1,', corr2 =', corr2)
        print('корреляция увеличилась' if corr1 > corr2 else 'корреляция уменьшилась')


"возвращает доменный состав первых count ортологов"
def get_domains(gen_name, count):
        foo1, foo2, orth_names = get_data(gen_name, count)
        domains = []
        for orth in orth_names:
                domains.append(Gene(orth).motif)
        return domains

def domain_freq(gen_name, count):
        domains = get_domains(gen_name, count)
        merged_domains = []
        
        for domain in domains:
                merged_domains += domain

        domain_counter = Counter(merged_domains)
        return domain_counter

def bar_graph(ax, data, n):
        ind = list(data.keys())
        ax.barh(ind, list(data.values()))
        ax.set_yticks(ind)
        ax.set_title(f'первые {n} ортологов')
        return ax
        
def bar_graphs(gen_name):
        freq1 = domain_freq(gen_name, 10)
        freq2 = domain_freq(gen_name, 50)
        
        fig = plt.figure()
        
        ax1 = fig.add_subplot(211)
        ax1 = bar_graph(ax1, freq1, 10)

        ax2 = fig.add_subplot(212)
        ax2 = bar_graph(ax2, freq2, 50)
        
        plt.show()
       
gen_name = 'hsa:7314'
url = f'https://rest.kegg.jp/get/{gen_name}'

compare(gen_name)
bar_graphs(gen_name)


































