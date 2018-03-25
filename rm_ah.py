# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 23:46:55 2018

@author: Aditya
"""


#hectare=(obtained from the other file)
#para_in_animals = ["no. of cows","no. of bull","no. of buffalo","no. of goats","no. of hens","no. of beeboxes"]
para_in = [1,2,3,4,5,6]
hectare = 20
recommended_crop = "Rice"



def recommendation_husbandary(para_in,hectare,recommended_crop):
    cows=int(para_in[0])
    buffalo=int(para_in[2])
    hen=int(para_in[4])
    bee=int(para_in[5])
    investment = []
    for crop in recommended_crop:
        if (crop == "Rice") or (crop == "Maize"):
            investment.append((1500*bee)+(hectare*1000*0.5))
        else:
            investment.append(1500*bee)
    

    income= cows*1600*24 + buffalo*1350*36.5 + bee*110*450 + 500*750*hen
    
    
    
    weights = [29.5,42,36.782,4.5359,0.0566,0]
    for i in range(len(para_in)):
        para_in[i] = int(para_in[i])
    product = []
    for i in range(len(para_in)):
        product.append(float(para_in[i])*float(weights[i]))
    N_values = [product[0]*0.6,product[1]*0.6,product[2]*0.6,product[3]*0.7,product[4]*1.1]
    P_values = [product[0]*0.4,product[1]*0.4,product[2]*0.4,product[3]*0.3,product[4]*0.8]
    K_values = [product[0]*0.5,product[1]*0.5,product[2]*0.5,product[3]*0.9,product[4]*0.5]
    total_N = sum(N_values)*1.8
    total_P = sum(P_values)*1.8
    total_K = sum(K_values)*1.8
    savings = total_N*5.5 + total_P*7.37 + total_K*14.4
    
    recommend = [total_N,total_P,total_K,savings,investment,income]
    return recommend

