import requests
import re

def get_orthologs(gen_name):
        url = f'https://www.kegg.jp/ssdb-bin/ssdb_best?org_gene={gen_name}'
        resp = requests.get(url=url)
        
        reg1 = r"<INPUT(.)*</a>"
        reg4 = r"<INPUT(.)*<A(.)*>"
        
        blocks = list(re.finditer(reg4 ,resp.text))
        name = re.search(r'[a-z]+:[0-9]+',str(blocks[0]))   

        print(str(name))

gen_name = 'hsa:7314'

reg3 = r'[a-z]+:[0-9]+'

get_orthologs(gen_name)





