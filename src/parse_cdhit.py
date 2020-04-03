

import pandas as pd
import re
input ="test_cdhit.clstr"

with open(input) as file:
    cdhit_clstr=file.read()

all_genomes= set(re.findall("(?<=!!)GCF_.+?(?=!!)",cdhit_clstr))
all_clusters= cdhit_clstr.split(">Cluster ")[1:]


rep_names=[]
genome_tally=[]
for genome in all_genomes:
    clstr_tally=[]
    for cluster in all_clusters:
        split_cluster= cluster.split("!!")
        rep_names.append(split_cluster[7]+"_"+split_cluster[9])
        clstr_tally.append(cluster.count("!!"+genome+"!!"))
    genome_tally.append(clstr_tally)        

clustr_df=pd.DataFrame(data=genome_tally, columns=["Cluster_"+str(i) for i in range(0,len(all_clusters))], index= all_genomes).transpose()

clustr_df['freq'] = (clustr_df > 0).sum(axis=1)/len(all_genomes)


clustr_df['rep_name'] = rep_names




