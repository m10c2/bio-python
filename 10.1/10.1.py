import requests
from numpy import nan
import re

class Gene:
    
    def  __init__(self, url):
        
        resp = requests.get(url = url)
        lines = resp.text.split('\n')
        
        self.entry = get_entry(self, lines)
        self.organism = get_organism(self, lines)
        self.motif = get_motif(self, lines)
        self.aaseq = get_aaseq(self, lines)

def line_with_keyword(self, lines, arg):
    
    for line in lines:
        if arg in line:
            return line
    return nan

def get_entry(self, lines):
    
    line = line_with_keyword(self, lines, 'ENTRY')  
    if  line != nan:
        line = line.replace(' ','').replace('ENTRY','')
        numbers = []
        n = ''
        for char in line:
            if char.isdigit():
                n += char
            else:
                if n.isdigit():
                    numbers.append(n)
                    n = ''
        if n != '':
            numbers.append(n)      
        return numbers[0]
    
    else:
        return nan

def get_organism(self, lines):
    line = line_with_keyword(self, lines, 'ORGANISM')

    if line != nan:
        line = line.replace('ORGANISM','').strip()
        return line.split(' ')[0]      
    else:
        return nan

def get_motif(self, lines):

    line = line_with_keyword(self, lines, 'MOTIF')
    
    if line != nan:
        line = line.replace('MOTIF','').replace('Pfam:','').strip()
        splitter = line.split(' ')
        return splitter
    else:
        return nan

def get_aaseq(self, lines):

    line = line_with_keyword(self, lines, 'AASEQ')

    if line != nan:
        pass
    else:
        return nan
    
url = 'https://rest.kegg.jp/get/hsa:7314'

resp = requests.get(url = url)
text = resp.text
arg1 = 'AASEQ'
arg2 = 'NTSEQ'

