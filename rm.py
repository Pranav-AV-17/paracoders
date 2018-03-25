# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 19:00:24 2018

@author: Aditya
"""

def recommendation_agriculture(para_in):
    kharif = ["Rice","Sugarcane","Tea","Coffee","Maize"]
    rabi = ["Rice","Wheat","Cotton","Sugarcane","Tea","Coffee"]
    crop_recommend_season = []
    if para_in[1] == "Kharif":
        if para_in[0] in kharif:
            crop_recommend_season  = [para_in[0]]
        else:
            crop_recommend_season = kharif
    if para_in[1] == "Rabi":
        if para_in[0] in rabi:
            crop_recommend_season = [para_in[0]]
        else:
            crop_recommend_season = rabi
    
    clay_soil = ["Rice"]
    black_soil = ["Cotton","Wheat","Sugarcane"]
    red_soil = ["Rice","Wheat","Sugarcane","Maize"]
    alluvial_soil = ["Rice","Wheat","Sugarcane","Cotton","Maize"]   
    laterite_soil = ["Tea","Coffee"]
    
    crop_recommend_soil = []
    if para_in[4] == "Clay soil":
        if para_in[0] in clay_soil:
            crop_recommend_soil  = [para_in[0]]
        else:
            crop_recommend_soil = clay_soil
            
    if para_in[4] == "Black soil":
        if para_in[0] in black_soil:
            crop_recommend_soil  = [para_in[0]]
        else:
            crop_recommend_soil = black_soil
    
    if para_in[4] == "Red soil":
        if para_in[0] in red_soil:
            crop_recommend_soil  = [para_in[0]]
        else:
            crop_recommend_soil = red_soil
    
    if para_in[4] == "Alluvial soil":
        if para_in[0] in alluvial_soil:
            crop_recommend_soil  = [para_in[0]]
        else:
            crop_recommend_soil = alluvial_soil
    
    if para_in[4] == "Laterite soil":
        if para_in[0] in laterite_soil:
            crop_recommend_soil  = [para_in[0]]
        else:
            crop_recommend_soil = laterite_soil
    
    recommend_crop = [val for val in crop_recommend_soil if val in crop_recommend_season]
    if not recommend_crop:
        recommend_crop.append(para_in[0])
    
        
    if para_in[2] == "Plateau":
        recommend_irrigation = "Drip"
    if para_in[2] == "Coastal":
        recommend_irrigation = "Sprinkle"
    if para_in[2] == "Mountains":
        recommend_irrigation = "Surface"
    
    if para_in[5] == recommend_irrigation:
        irrigation_flag = 0
    else:
        irrigation_flag = 1
    
    
    
    
    
    
    rice = [81.7,24.3,13.1]
    wheat = [99.6,30.2,6.9]
    cotton = [89.5,22.6,4.8]
    maize = [41.7,14.7,3.8]
    sugarcane = [124.8,44,38.3]
    coffee = [360,50,550]
    tea = [335,35,120]
    
    #Rs/Ha
    rice_seed = 1150
    wheat_seed = 2750
    cotton_seed = 10000
    maize_seed = 2500
    sugarcane_seed = 6000
    coffee_seed = 50000
    tea_seed = 12000
    seed = 0
    N_recommend = 0
    P_recommend = 0
    K_recommend = 0
    crop_investment = []
    fertilizers = []
    for crop in recommend_crop:
        investment = 0  
        if crop == "Rice":
            N_recommend = rice[0]
            P_recommend = rice[1]
            K_recommend = rice[2]
            seed = rice_seed
            
        if crop == "Wheat":
            N_recommend = wheat[0]
            P_recommend = wheat[1]
            K_recommend = wheat[2]
            seed = wheat_seed
            
        if crop == "Cotton":
            N_recommend = cotton[0]
            P_recommend = cotton[1]
            K_recommend = cotton[2]
            seed = cotton_seed
            
        if crop == "Maize":
            N_recommend = maize[0]
            P_recommend = maize[1]
            K_recommend = maize[2]
            seed = maize_seed
            
        if crop == "Sugarcane":
            N_recommend = sugarcane[0]
            P_recommend = sugarcane[1]
            K_recommend = sugarcane[2]
            seed = sugarcane_seed
            
        if crop == "Tea":
            N_recommend = tea[0]
            P_recommend = tea[1]
            K_recommend = tea[2]
            seed = tea_seed
            
        if crop == "Coffee":
            N_recommend = coffee[0]
            P_recommend = coffee[1]
            K_recommend = coffee[2]
            seed = coffee_seed
            
        investment = 0.405*seed*int(para_in[3])
        if irrigation_flag == 1:
           if recommend_irrigation == "Drip":
               investment += int(para_in[3])*55000
           if recommend_irrigation == "Sprinkle":
               investment += int(para_in[3])*25000
        investment += 0.405*int(para_in[3])*((N_recommend)*5.5+ (P_recommend)*7.37+(K_recommend)*17.4)
        crop_investment.append(investment)
        npk = [(N_recommend)*0.405*int(para_in[3]), (P_recommend)*0.405*int(para_in[3]),(K_recommend)*0.405*int(para_in[3])]
        fertilizers.append(npk)
    recommendations = [recommend_crop,recommend_irrigation,fertilizers,crop_investment]
    return recommendations


#para_in = ["Wheat","Rabi","Mountains","2","Laterite soil","Surface","11111"]
#
#
#recommendation_agriculture(para_in)


