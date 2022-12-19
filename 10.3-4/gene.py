import requests
import re
import matplotlib.pyplot as plt
import numpy as np

class Gene:
    def __init__(self, gen_name):

        url = f'https://rest.kegg.jp/get/{gen_name}'
        resp = requests.get(url=url)
        text = resp.text

        self.entry = self.get_entry(gen_name)
        self.organism = self.get_organism(gen_name)
        self.motif = self.get_motif(text)
        self.aaseq = self.get_aaseq(text)
        self.ntseq = self.get_ntseq(text)

    def get_entry(self, gen_name):
        entry = gen_name.split(':')[1]
        return entry

    def get_organism(self, gen_name):
        organism = gen_name.split(':')[0]
        return organism

    def get_motif(self, text):
        regex = r"MOTIF\s+\w+:\s+.+"
        motif = re.search(regex, text)

        if motif:
            motif = motif[0].replace('MOTIF', '').strip().split(' ')[1:]
        else:
            motif = None
        return motif

    def get_aaseq(self, text):
        regex = r"AASEQ\s+\d+((?:[\sA-Z]+)+)\n"
        tmp_seq = re.search(regex, text).group()

        if tmp_seq:
            aaseq = re.sub("\s", "", tmp_seq)
            return aaseq
        else:
            return None

    def get_ntseq(self, text):
        regex = r"NTSEQ\s+\d+((?:[\satgc]+)+)\n"
        tmp_seq = re.search(regex, text).group()

        if tmp_seq:
            ntseq = re.sub("\s", "", tmp_seq)
            return ntseq
        else:
            return None

    "График pie для частоты встречаемости нуклеотидов в ntseq"

    def ntseq_pie(self, ax):

        seq = self.ntseq
        nucl = 'atgc'
        freq = []
        for symbol in nucl:
            freq.append(seq.count(symbol))
        freq = np.array(freq)
        labels = ['A', 'T', 'G', 'C']
        explode = [0.05]*4

        ax.pie(freq, labels=labels, autopct = lambda val: np.round(val/100.*freq.sum(), 0), explode=explode)
        ax.legend(labels, bbox_to_anchor=(1, 1.025), loc="upper left")
        ax.set_title('График pie для частоты встречаемости нуклеотидов в ntseq')

        return ax

    "График bar для частоты встречаемости аминокислот в aaseq"

    def aaseq_bar(self, ax):
        seq = self.aaseq
        amins = 'ARNDCQEGHILKMFPSTWYV'

        freq = []
        labels = []
        ind = range(len(amins))
        
        for symbol in amins:
            freq.append(seq.count(symbol))
            labels.append(symbol)

        ax.bar(ind, freq)
        ax.set_xticks(ind)
        ax.set_xticklabels(labels)
        ax.set_xlabel('Аминокислоты')
        ax.set_ylabel('Частота')
        ax.set_title('График bar для частоты встречаемости аминокислот в aaseq')

        return ax

    def graphs(self):
        fig = plt.figure()

        ax1 = fig.add_subplot(121)
        ax1 = self.ntseq_pie(ax1)

        ax2 = fig.add_subplot(122)
        ax2 = self.aaseq_bar(ax2)

        plt.show()
