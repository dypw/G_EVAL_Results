import json
import numpy
from scipy import stats
sets = ["GRADE-DailyDialog","GRADE-Convai2","GRADE-Empa"]
sub = ["generator","ranker"]
for se in sets:
    for su in sub:
        for n in [1,20]:
            alldata = []
            print(se+"_"+su+"_n="+str(n))
            for t in range(3):
                with open("{}/new_GRADE-{}_GPT4_GPTEVAL_Results_{}.json".format(se,su,t),"r")as f:
                    l = json.load(f)
                alldata+=l

            scores = []
            human=[]
            for tem in alldata:
                try:
                    ttt = [tem['results']['choices'][i]['message']['content'][0] for i in range(20)]
                    tt=[]
                    for tp in ttt:
                        if tp in ['1','2','3','4','5']:
                            tt.append(int(tp))
                    if len(tt)==0:
                        tt.append(3)
                        print(1)
                    if n==20:
                        scores.append(float(numpy.array(tt).mean()))
                    else:
                        scores.append(float(numpy.array(tt)[0]))
                    human.append(float(tem['human_score']))
                except:
                    ggg=5

            r, p = stats.pearsonr(scores, human)
            spearmanr = stats.spearmanr(scores, human)

            # print("pearson_score: {}   p_value: {}".format(r, p))
            print("spearmanr_score: {}   p_value: {}".format(spearmanr.correlation, spearmanr.pvalue))