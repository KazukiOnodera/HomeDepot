# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 19:55:56 2016

@author: Kazuki
"""

import homedepot as hd
import pandas as pd
weight = pd.read_csv(hd.path_sub+"05tfidf_weight.csv")


def get_ratio_in_prd(li1,li2):
    if isinstance(li1, list) and isinstance(li2, list) and len(li2)>0:
        n = len(li2)
        cnt = 0
        for i in li1:
            cnt += li2.count(i)
        ratio = float(cnt)/n
        return ratio
    return -1
    
def isorder(li1,li2,p):
    if p:
        ind_bk = -1
        for i in li1[::-1]:
            if i in li2:
                ind = li2[::-1].index(i)
                if ind_bk > ind:
                    return 0
                ind_bk = ind
        return 1
    return -1
    
def ispair(li1,li2):#length of li1 is 2
    for i in range(len(li1)-1):
        if li1[i] in li2:
            ind = li2.index(li1[i])+1
            if ind < len(li2):
                if li1[i+1] == li2[ind]:
                    return (ind/(len(li2)*1.))
                else:
                    return 0
            else:
                return -1
        if i == li1[-1]:
            return -2
    return -3
    
def get_ind(w,li):
    ind = -1
    if w in li:
        ind = li[::-1].index(w)
    return ind
    
def comb_match(qq,tt):
    if len(qq)<2:
        return -1
    cnt = 0
    for i in range(len(qq)-1):
        if hd.stem(qq[i]+qq[i+1]) in ''.join(tt):
            cnt += 1
    return cnt
    
def back_is_important(qq,tt):
    #TODO: brand remove
    cnt = 0.
    ss = [x/float(len(tt)) for x in range(1,len(tt)+1)]
    s_sum = sum(ss)
    ss = [x/s_sum for x in ss]
    for q in qq:
        if q in tt:
            ind = tt.index(q)
            cnt += ss[ind]
    return cnt
    
def is_all_in_back(qq,tt):
    for t in tt[::-1][:len(qq)]:
        if not t in qq:
            return 0
    return 1
    
def is_hit_b4_prepos(qq,tt,pre):
    if pre in tt:
        ind = tt.index(pre)-1
        if tt[ind] in qq:
            return (ind/(len(tt)*1.))
        else:
            return -1
    return -2
    
def is_prepos_after_word(w,tt,pre):
    if w in tt:
        if pre in tt:
            ind = tt.index(w)+1
            if ind < len(tt):
                if tt[ind]==pre:
                    return (ind/(len(tt)*1.))
                else:
                    return -1
            else:
                return -2
        else:
            return -3
    return -4
    
def get_freq(w):
    freq = -1
    if w in weight.s.tolist():
        freq = weight[weight.s==w].w.values[0]
    return freq
    
def is_part_inc(w,tt):
    if w not in tt: 
        for t in tt:
            if w in t and w!= t:
                return 1,(tt.index(t)/(len(tt)*1.))
        return 0,-1
    return -1,-2
    
def match_unmatch(base,prd):
    
    li_t01,li_t02,li_t03,li_t04,li_t05 = [],[],[],[],[]
    li_t06,li_t07,li_t08,li_t09,li_t10 = [],[],[],[],[]
    li_t11,li_t12,li_t13,li_t14,li_t15 = [],[],[],[],[]
    li_t16,li_t17,li_t18,li_t19,li_t20 = [],[],[],[],[]
    li_t21,li_t22,li_t23,li_t24,li_t25 = [],[],[],[],[]
    li_t26,li_t27,li_t28,li_t29,li_t30 = [],[],[],[],[]
    li_t31,li_t32,li_t33,li_t34,li_t35 = [],[],[],[],[]
    li_t36,li_t37,li_t38,li_t39,li_t40 = [],[],[],[],[]
    li_t41,li_t42,li_t43,li_t44,li_t45 = [],[],[],[],[]
    li_t46,li_t47,li_t48,li_t49,li_t50 = [],[],[],[],[]
    li_t51,li_t52,li_t53,li_t54,li_t55 = [],[],[],[],[]
    li_t56,li_t57,li_t58,li_t59,li_t60 = [],[],[],[],[]
    li_t61,li_t62,li_t63,li_t64,li_t65 = [],[],[],[],[]
    li_t66,li_t67,li_t68,li_t69,li_t70 = [],[],[],[],[]
    li_t71,li_t72,li_t73,li_t74,li_t75 = [],[],[],[],[]
    li_t76,li_t77,li_t78,li_t79,li_t80 = [],[],[],[],[]
    li_t81,li_t82,li_t83,li_t84,li_t85 = [],[],[],[],[]
    
    li_t14_1,li_t09_2,li_t09_3,li_t09_4 = [],[],[],[]
    li_t08_2 = []
    
    
    
    li_d1,li_d2,li_d3,li_d4,li_d5,li_d6,li_d7,li_d8 = [],[],[],[],[],[],[],[]
    li_d9,li_d10,li_d11,li_d12,li_d13,li_d14,li_d15,li_d16 = [],[],[],[],[],[],[],[]
    
    li_td1,li_td2,li_td3,li_td4,li_td5,li_td6,li_td7 = [],[],[],[],[],[],[]
    li_td8,li_td9,li_td10 = [],[],[]
    
    li_item_s01,li_item_s02,li_item_s03,li_item_s04,li_item_s05 = [],[],[],[],[]
    li_item_s06,li_item_s07,li_item_s08,li_item_s09,li_item_s10 = [],[],[],[],[]
    
    li_item_t01,li_item_t02,li_item_t03,li_item_t04,li_item_t05 = [],[],[],[],[]
    li_item_t06,li_item_t07,li_item_t08,li_item_t09,li_item_t10 = [],[],[],[],[]
    
    
    
#    
    li_color1,li_color2,li_color3,li_color4 = [],[],[],[]
    li_case1,li_case2,li_case3 = [],[],[]
    li_power1,li_power2,li_power3,li_power4 = [],[],[],[]
    li_material1,li_material2,li_material3 = [],[],[]
    li_mobility1,li_mobility2,li_mobility3,li_mobility4 = [],[],[],[]
    li_brand1,li_brand2,li_brand3,li_brand4 = [],[],[],[]
#    
    li_perfect1_,li_perfect2_,li_perfect3_ = [],[],[]
#    li_item1_,li_item2_,li_item3_   = [],[],[]
    li_brand_   = []
    li_power_   = []
    li_mater_   = []
    li_mobil_   = []
    li_case_    = []
    li_color1_,li_color2_,li_color3_,li_color4_   = [],[],[],[]
#    
    li_size1,li_size2,li_size3,li_size4,li_size5,li_size6 = [],[],[],[],[],[]
    li_size7,li_size8,li_size9,li_size10,li_size11,li_size12 = [],[],[],[],[],[]
    li_size13,li_size14,li_size15,li_size16 = [],[],[],[]
    
    li_num1,li_num2,li_num3,li_num4,li_num5,li_num6 = [],[],[],[],[],[]
#    li_num7 = []
    
    merged = pd.merge(base,prd,on='pid',how='left')
    for i in merged.index:
        query = list(merged.s_[i])
        tt = merged.t_[i]
#        tt_main = merged.t_main[i]
        desc = merged.d_[i]
        s_size = merged.s_size_[i]
        t_size = merged.t_size_[i]
        d_size = merged.d_size_[i]
        att_size = merged.att_size_[i]
        s_num = merged.s_num_[i]
        t_num = merged.t_num_[i]
        d_num = merged.d_num_[i]
#        query,sw = hd.rep_comb(query,tt)
#        li_comb.append(sw)
#        query_syn,sw = hd.rep_syn(query,tt)
#        li_query_syn.append(query_syn)
#        li_syn.append(sw)
        """EVALUATE MATCH"""
        "tt"
        li_t01.append(''.join(query) in ''.join(tt))
        li_t02.append(''.join(tt).count(''.join(query)))
        li_t03.append(hd.count_list_in_list(query,tt))
        li_t04.append(get_ratio_in_prd(query,tt))
        li_t05.append(get_ratio_in_prd(tt,query))
        li_t06.append(comb_match(query,tt))
        li_t07.append(back_is_important(query,tt))
        li_t08.append(is_all_in_back(query,tt))
        li_t09.append(is_hit_b4_prepos(query,tt,'in'))
        li_t10.append(is_hit_b4_prepos(query,tt,'with'))
        li_t11.append(is_hit_b4_prepos(query,tt,'for'))
        
        li_t12.append(query[-1] in tt)
        li_t13.append(query[-1] == tt[-1])
        li_t14.append(tt[-1] in query)
        li_t15.append(get_ind(tt[-1],query))
        li_t16.append(get_ind(query[-1],tt))
        li_t17.append(get_ind(query[-1],tt[::-1]))
        li_t18.append(is_hit_b4_prepos([query[-1]],tt,'in'))
        li_t19.append(is_hit_b4_prepos([query[-1]],tt,'with'))
        li_t20.append(is_hit_b4_prepos([query[-1]],tt,'for'))
        
        li_t21.append(merged.s_item[i] in tt)
        li_t22.append(merged.s_item[i] == tt[-1])
        li_t23.append(get_ind(merged.s_item[i],tt))
        li_t24.append(get_ind(merged.s_item[i],tt[::-1]))
        li_t25.append(is_hit_b4_prepos([merged.s_item[i]],tt,'in'))
        li_t26.append(is_hit_b4_prepos([merged.s_item[i]],tt,'with'))
        li_t27.append(is_hit_b4_prepos([merged.s_item[i]],tt,'for'))
        
        li_t29.append(query[0] in tt)
        li_t28.append(query[0] == tt[-1])
        li_t30.append(isorder(query,tt,li_t03[i]))
        li_t31.append(get_ind(query[0],tt))
        li_t32.append(get_ind(query[0],tt[::-1]))
        li_t33.append(query[0]in ''.join(tt))
        li_t34.append(query[-1]in ''.join(tt))
        li_t35.append(tt[0] in query)
        
        li_t36.append(ispair(query,tt))
        li_t37.append(ispair(query[::-1],tt[::-1]))
#        if len(query)>1:
#            li_t26.append(query[-2] == tt[-2])
#            li_t27.append(query[-2] in tt)
#            li_t28.append(tt[-2] in query)
#            li_t29.append(get_ind(query[-2],tt))
#            li_t30.append(get_ind(query[-2],tt[::-1]))
#            li_t31.append(query[-2]in ''.join(tt))
#            
#            li_t32.append(query[-2:] == tt[-2:])
#            li_t33.append(''.join(query[-2:]) in ''.join(tt))
#            li_t34.append(''.join(tt[-2:]) in ''.join(query))
#            li_t35.append(get_ind(''.join(query[-2:]),tt))
#            li_t36.append(get_ind(''.join(query[-2:]),tt[::-1]))
#        else:
#            li_t26.append(-2)
#            li_t27.append(-2)
#            li_t28.append(-2)
#            li_t29.append(-2)
#            li_t30.append(-2)
#            li_t31.append(-2)
#            li_t32.append(-2)
#            li_t33.append(-2)
#            li_t34.append(-2)
#            li_t35.append(-2)
#            li_t36.append(-2)
            
        
#        if len(tt_main)>0:
#            li_t51.append(''.join(query) in ''.join(tt_main))
#            li_t52.append(''.join(tt_main).count(''.join(query)))
#            li_t53.append(hd.count_list_in_list(query,tt_main))
#            li_t54.append(get_ratio_in_prd(query,tt_main))
#            li_t55.append(get_ratio_in_prd(tt_main,query))
#            li_t56.append(query[-1] == tt_main[-1])
#            li_t57.append(query[-1] in tt_main)
#            li_t58.append(tt_main[-1] in query)
#            li_t59.append(merged.s_item2[i] in tt_main)
#            li_t60.append(query[0] == tt_main[-1])
#            li_t61.append(query[0] in tt_main)
#            li_t62.append(isorder(query,tt_main,li_t53[i]))
#            li_t63.append(get_ind(query[0],tt_main))
#            li_t64.append(get_ind(query[0],tt_main[::-1]))
#            li_t65.append(get_ind(query[-1],tt_main))
#            li_t66.append(get_ind(query[-1],tt_main[::-1]))
#            li_t67.append(query[0]in ''.join(tt_main))
#            li_t68.append(query[-1]in ''.join(tt_main))
#            li_t69.append(comb_match(query,tt_main))
#            li_t70.append(back_is_important(query,tt_main))
#            li_t71.append(is_all_in_back(query,tt_main))
#            
#            if len(query)>1 and len(tt_main)>1:
#                li_t72.append(query[-2] == tt_main[-2])
#                li_t73.append(query[-2] in tt_main)
#                li_t74.append(tt_main[-2] in query)
#                li_t75.append(get_ind(query[-2],tt_main))
#                li_t76.append(get_ind(query[-2],tt_main[::-1]))
#                li_t77.append(query[-2]in ''.join(tt_main))
#                li_t78.append(query[-2:] == tt_main[-2:])
#                li_t79.append(''.join(query[-2:]) in ''.join(tt_main))
#                li_t80.append(''.join(tt_main[-2:]) in ''.join(query))
#                li_t81.append(get_ind(''.join(query[-2:]),tt_main))
#                li_t82.append(get_ind(''.join(query[-2:]),tt_main[::-1]))
#            else:
#                li_t72.append(-2)
#                li_t73.append(-2)
#                li_t74.append(-2)
#                li_t75.append(-2)
#                li_t76.append(-2)
#                li_t77.append(-2)
#                li_t78.append(-2)
#                li_t79.append(-2)
#                li_t80.append(-2)
#                li_t81.append(-2)
#                li_t82.append(-2)
#        else:
#            li_t51.append(-2)
#            li_t52.append(-2)
#            li_t53.append(-2)
#            li_t54.append(-2)
#            li_t55.append(-2)
#            li_t56.append(-2)
#            li_t57.append(-2)
#            li_t58.append(-2)
#            li_t59.append(-2)
#            li_t60.append(-2)
#            li_t61.append(-2)
#            li_t62.append(-2)
#            li_t63.append(-2)
#            li_t64.append(-2)
#            li_t65.append(-2)
#            li_t66.append(-2)
#            li_t67.append(-2)
#            li_t68.append(-2)
#            li_t69.append(-2)
#            li_t70.append(-2)
#            li_t71.append(-2)
#            li_t72.append(-2)
#            li_t73.append(-2)
#            li_t74.append(-2)
#            li_t75.append(-2)
#            li_t76.append(-2)
#            li_t77.append(-2)
#            li_t78.append(-2)
#            li_t79.append(-2)
#            li_t80.append(-2)
#            li_t81.append(-2)
#            li_t82.append(-2)
        
        "DESCRIPTION"
        li_d1.append(''.join(query) in ''.join(desc))
        li_d2.append(''.join(desc).count(''.join(query)))
        li_d3.append(hd.count_list_in_list(query,desc))
        li_d4.append(get_ratio_in_prd(query,desc))
        li_d5.append(get_ratio_in_prd(desc,query))
        li_d6.append(query[-1] in desc)
        li_d7.append(query[0] in desc)
        li_d8.append(isorder(query,desc,li_d3[i]))
        li_d9.append(get_ind(query[0],desc))
        li_d10.append(get_ind(query[0],desc[::-1]))
        li_d11.append(get_ind(query[-1],desc))
        li_d12.append(get_ind(query[-1],desc[::-1]))
        li_d13.append(query[0] in ''.join(desc))
        li_d14.append(query[-1] in ''.join(desc))
        li_d15.append(desc.count(query[0]))
        li_d16.append(desc.count(query[-1]))
        
        "TITLE & DESCRIPTION"
        li_td1.append(''.join(query) in ''.join(tt+desc))
        li_td2.append(''.join(tt+desc).count(''.join(query)))
        li_td3.append(hd.count_list_in_list(query,tt+desc))
        li_td4.append(get_ratio_in_prd(query,tt+desc))
        li_td5.append(get_ratio_in_prd(tt+desc,query))
        li_td6.append(query[-1] in tt+desc)
        li_td7.append(query[0] in tt+desc)
        li_td8.append(isorder(query,tt+desc,li_td3[i]))
        li_td9.append(get_ind(query[0],tt+desc))
        li_td10.append(get_ind(query[-1],tt+desc))
        #TODO:position(sentense part),ambiguous match
        
        "size,num"#TODO:weight
        li_size1.append(hd.is_list_in_list(s_size,t_size))
        li_size2.append(hd.is_list_in_list(s_size,d_size))
        li_size3.append(hd.is_list_in_list(s_size,att_size))
        li_size4.append(hd.is_list_in_list(s_size,t_size+d_size+att_size))
        li_size5.append(get_ratio_in_prd(s_size,t_size))
        li_size6.append(get_ratio_in_prd(s_size,d_size))
        li_size7.append(get_ratio_in_prd(s_size,att_size))
        li_size8.append(get_ratio_in_prd(s_size,list(set(t_size+d_size+att_size))))
        li_size9.append(get_ratio_in_prd(t_size,s_size))
        li_size10.append(get_ratio_in_prd(d_size,s_size))
        li_size11.append(get_ratio_in_prd(att_size,s_size))
        li_size12.append(get_ratio_in_prd(t_size+d_size+att_size,s_size))
        li_size13.append(hd.count_list_in_list(s_size,t_size))
        li_size14.append(hd.count_list_in_list(s_size,d_size))
        li_size15.append(hd.count_list_in_list(s_size,att_size))
        li_size16.append(hd.count_list_in_list(s_size,list(set(t_size+d_size+att_size))))
        
        li_num1.append(hd.is_list_in_list(s_num,tt))
        li_num2.append(hd.is_list_in_list(s_num,desc))
        li_num3.append(hd.is_list_in_list(s_num,tt+desc))
        li_num4.append(get_ratio_in_prd(t_num,s_num))
        li_num5.append(get_ratio_in_prd(d_num,s_num))
        li_num6.append(get_ratio_in_prd(t_num+d_num,s_num))
        
        
#        "OTHER"
#        syn1 = hd.get_syn(merged.s_item1[i])
#        syn2 = hd.get_syn(merged.s_item2[i])
        li_item_s01.append('' != merged.s_item_myrule[i] and merged.s_item_myrule[i] in tt)
        li_item_s02.append('' != merged.s_item_myrule[i] and merged.s_item_myrule[i] in desc)
        li_item_s03.append('' != merged.s_item_list[i] and merged.s_item_list[i] in tt)
        li_item_s04.append('' != merged.s_item_list[i] and merged.s_item_list[i] in desc)
        li_item_s05.append('' != merged.s_item[i] and merged.s_item[i] in tt)
        li_item_s06.append('' != merged.s_item[i] and merged.s_item[i] in desc)
        li_item_s07.append('' != merged.s_item_imp2[i] and merged.s_item_imp2[i] in tt)
        li_item_s08.append('' != merged.s_item_imp2[i] and merged.s_item_imp2[i] in desc)
        
        li_item_t01.append('' != merged.t_item_myrule[i] and merged.t_item_myrule[i] in query)
        li_item_t02.append('' != merged.t_item_list[i] and merged.t_item_list[i] in query)
        li_item_t03.append('' != merged.t_item[i] and merged.t_item[i] in query)
#        li_item6.append('null' != merged.s_item2[i] and merged.s_item2[i] in tt+desc)
#        li_item7.append('null' != merged.s_item_imp2[i] and hd.is_list_in_list(syn1,tt))
#        li_item8.append('null' != merged.s_item_imp2[i] and hd.is_list_in_list(syn1,desc))
#        li_item9.append('null' != merged.s_item1[i] and hd.is_list_in_list(syn1,tt+desc))
#        li_item10.append('null' != merged.s_item1[i] and hd.count_list_in_list(syn1,tt))
#        li_item11.append('null' != merged.s_item1[i] and hd.count_list_in_list(syn1,desc))
#        li_item12.append('null' != merged.s_item1[i] and hd.count_list_in_list(syn1,tt+desc))
#        li_item13.append('null' != merged.s_item2[i] and hd.is_list_in_list(syn2,tt))
#        li_item14.append('null' != merged.s_item2[i] and hd.is_list_in_list(syn2,desc))
#        li_item15.append('null' != merged.s_item2[i] and hd.is_list_in_list(syn2,tt+desc))
#        li_item16.append('null' != merged.s_item2[i] and hd.count_list_in_list(syn2,tt))
#        li_item17.append('null' != merged.s_item2[i] and hd.count_list_in_list(syn2,desc))
#        li_item18.append('null' != merged.s_item2[i] and hd.count_list_in_list(syn2,tt+desc))
#        li_item19.append('null' != merged.t_item1[i] and merged.t_item1[i] in query)
#        li_item20.append('null' != merged.t_item2[i] and merged.t_item2[i] in query)
#        li_item21.append('null' != merged.s_item1[i] and merged.s_item1[i] in ''.join(tt))
#        li_item22.append('null' != merged.s_item1[i] and merged.s_item1[i] in ''.join(desc))
#        li_item23.append('null' != merged.s_item2[i] and merged.s_item2[i] in ''.join(tt))
#        li_item24.append('null' != merged.s_item2[i] and merged.s_item2[i] in ''.join(desc))
#        
#        #TODO:count
        li_color1.append('' != merged.s_color[i] and merged.s_color[i] in tt)
        li_color2.append('' != merged.s_color[i] and merged.s_color[i] in desc)
        li_color3.append('' != merged.s_color[i] and merged.s_color[i] in merged.att_color_[i])
        li_color4.append('' != merged.s_color[i] and merged.s_color[i] in tt+desc+merged.att_color_[i])
        
        li_case1.append('' != merged.s_case[i] and merged.s_case[i] in tt)
        li_case2.append('' != merged.s_case[i] and merged.s_case[i] in desc)
        li_case3.append('' != merged.s_case[i] and merged.s_case[i] in tt+desc)
        
        li_power1.append('' != merged.s_power[i] and merged.s_power[i] in tt)
        li_power2.append('' != merged.s_power[i] and merged.s_power[i] in desc)
        li_power3.append('' != merged.s_power[i] and merged.s_power[i] in merged.att_power_[i])
        li_power4.append('' != merged.s_power[i] and merged.s_power[i] in tt+desc+merged.att_power_[i])
        
        li_material1.append('' != merged.s_material[i] and merged.s_material[i] in tt)
        li_material2.append('' != merged.s_material[i] and merged.s_material[i] in desc)
        li_material3.append('' != merged.s_material[i] and merged.s_material[i] in tt+desc+merged.att_material_[i])
        
        li_mobility1.append('' != merged.s_mobility[i] and merged.s_mobility[i] in tt)
        li_mobility2.append('' != merged.s_mobility[i] and merged.s_mobility[i] in desc)
        li_mobility3.append('' != merged.s_mobility[i] and '' != merged.t_mobility[i])
        li_mobility4.append('' != merged.s_mobility[i] and '' != merged.d_mobility[i])
        
        li_brand1.append('' != merged.s_brand[i] and merged.s_brand[i] in tt)
        li_brand2.append('' != merged.s_brand[i] and merged.s_brand[i] in desc)
        li_brand3.append('' != merged.s_brand[i] and merged.s_brand[i] in merged.p_brand_[i])
        li_brand4.append('' != merged.s_brand[i] and merged.s_brand[i] in ''.join(merged.p_brand_[i]))
#        
        """EVALUATE UNMATCH"""
        li_perfect1_.append(not hd.is_list_in_list(query,tt))
        li_perfect2_.append(not hd.is_list_in_list(query,desc))
        li_perfect3_.append(not hd.is_list_in_list(query,tt+desc))
        #TODO: title,desc kumiawase
#        li_item1_.append('null' != merged.s_item1[i] and not hd.count_list_in_list(syn1,tt))
#        li_item2_.append('null' != merged.s_item1[i] and not hd.count_list_in_list(syn1,desc))
#        li_item3_.append('null' != merged.s_item1[i] and not hd.count_list_in_list(syn1,tt+desc))
        
        li_color1_.append('null' != merged.s_color[i] and merged.s_color[i] not in tt)
        li_color2_.append('null' != merged.s_color[i] and merged.s_color[i] not in desc)
        li_color3_.append('null' != merged.s_color[i] and merged.s_color[i] not in merged.att_color_[i])
        li_color4_.append('null' != merged.s_color[i] and merged.s_color[i] not in tt+desc+merged.att_color_[i])
        
        li_case_.append('null' != merged.s_case[i] and merged.s_case[i] not in tt+desc)
        li_power_.append('null' != merged.s_power[i] and merged.s_power[i] not in tt+desc+merged.att_power_[i])
        li_mater_.append('null' != merged.s_material[i] and merged.s_material[i] not in tt+desc+merged.att_material_[i])
        li_mobil_.append('null' != merged.s_mobility[i] and ('corded' in tt+desc or 'plug' in merged.att_power_[i]))
        li_brand_.append('null' != merged.s_brand[i] and merged.s_brand[i] not in tt+desc+merged.p_brand_[i])
    
    
    base['title01'] = li_t01
    base['title02'] = li_t02
    base['title03'] = li_t03
    base['title04'] = li_t04
    base['title05'] = li_t05
    base['title06'] = li_t06
    base['title07'] = li_t07
    base['title08'] = li_t08
    base['title09'] = li_t09
    base['title10'] = li_t10
    base['title11'] = li_t11
    base['title12'] = li_t12
    base['title13'] = li_t13
    base['title14'] = li_t14
    base['title15'] = li_t15
    base['title16'] = li_t16
    base['title17'] = li_t17
    base['title18'] = li_t18
    base['title19'] = li_t19
    base['title20'] = li_t20
    base['title21'] = li_t21
    base['title22'] = li_t22
    base['title23'] = li_t23
    base['title24'] = li_t24
    base['title25'] = li_t25
    base['title26'] = li_t26
    base['title27'] = li_t27
    base['title28'] = li_t28
    base['title29'] = li_t29
    base['title30'] = li_t30
    base['title31'] = li_t31
    base['title32'] = li_t32
    base['title33'] = li_t33
    base['title34'] = li_t34
    base['title35'] = li_t35
    base['title36'] = li_t36
    base['title37'] = li_t37
#    base['title38'] = li_t38
#    base['title39'] = li_t39
#    base['title40'] = li_t40
    
#    base['title51'] = li_t51
#    base['title52'] = li_t52
#    base['title53'] = li_t53
#    base['title54'] = li_t54
#    base['title55'] = li_t55
#    base['title56'] = li_t56
#    base['title57'] = li_t57
#    base['title58'] = li_t58
#    base['title59'] = li_t59
#    base['title60'] = li_t60
#    base['title61'] = li_t61
#    base['title62'] = li_t62
#    base['title63'] = li_t63
#    base['title64'] = li_t64
#    base['title65'] = li_t65
#    base['title66'] = li_t66
#    base['title67'] = li_t67
#    base['title68'] = li_t68
#    base['title69'] = li_t69
#    base['title70'] = li_t70
#    base['title71'] = li_t71
#    base['title72'] = li_t72
#    base['title73'] = li_t73
#    base['title74'] = li_t74
#    base['title75'] = li_t75
#    base['title76'] = li_t76
#    base['title77'] = li_t77
#    base['title78'] = li_t78
#    base['title79'] = li_t79
#    base['title80'] = li_t80
#    base['title81'] = li_t81
#    base['title82'] = li_t82
#    base['title83'] = li_t83
#    base['title84'] = li_t84
#    base['title85'] = li_t85
#    base['title86'] = li_t86
#    base['title87'] = li_t87
#    base['title88'] = li_t88
#    base['title89'] = li_t89
    base['title_r1'] = base['title03']/base['s_len']
    base['title_r2'] = base['title15']/merged['t_len']
    base['title_r3'] = base['title16']/merged['t_len']
    base['title_r4'] = base['title17']/merged['t_len']
    base['title_r5'] = base['title23']/merged['t_len']
    base['title_r6'] = base['title24']/merged['t_len']
    base['title_r7'] = base['title31']/merged['t_len']
    base['title_r8'] = base['title32']/merged['t_len']
#    base['title_r6'] = base['title53']/base['s_len']
#    base['title_r7'] = base['title63']/merged['t_main_len']
#    base['title_r8'] = base['title64']/merged['t_main_len']
#    base['title_r9'] = base['title65']/merged['t_main_len']
#    base['title_r10'] = base['title66']/merged['t_main_len']
    
    
    base['desc01'] = li_d1
    base['desc02'] = li_d2
    base['desc03'] = li_d3
    base['desc04'] = li_d4
    base['desc05'] = li_d5
    base['desc06'] = li_d6
    base['desc07'] = li_d7
    base['desc08'] = li_d8
    base['desc09'] = li_d9
    base['desc10'] = li_d10
    base['desc11'] = li_d11
    base['desc12'] = li_d12
    base['desc13'] = li_d13
    base['desc14'] = li_d14
    base['desc15'] = li_d15
    base['desc16'] = li_d16
    base['desc_r1'] = base['desc03']/base['s_len']
    base['desc_r2'] = base['desc09']/merged['d_len']
    base['desc_r3'] = base['desc10']/merged['d_len']
    base['desc_r4'] = base['desc11']/merged['d_len']
    base['desc_r5'] = base['desc12']/merged['d_len']
    
    base['td01'] = li_td1
    base['td02'] = li_td2
    base['td03'] = li_td3
    base['td04'] = li_td4
    base['td05'] = li_td5
    base['td06'] = li_td6
    base['td07'] = li_td7
    base['td08'] = li_td8
    base['td09'] = li_td9
    base['td10'] = li_td10
    base['td_r'] = base['td03']/base['s_len']
    
    base['size1'] = li_size1
    base['size2'] = li_size2
    base['size3'] = li_size3
    base['size4'] = li_size4
    base['size5'] = li_size5
    base['size6'] = li_size6
    base['size7'] = li_size7
    base['size8'] = li_size8
    base['size9'] = li_size9
    base['size10'] = li_size10
    base['size11'] = li_size11
    base['size12'] = li_size12
    base['size13'] = li_size13
    base['size14'] = li_size14
    base['size15'] = li_size15
    base['size16'] = li_size16
    
    base['num1'] = li_num1
    base['num2'] = li_num2
    base['num3'] = li_num3
    base['num4'] = li_num4
    base['num5'] = li_num5
    base['num6'] = li_num6
    
    base['item_s01'] = li_item_s01
    base['item_s02'] = li_item_s02
    base['item_s03'] = li_item_s03
    base['item_s04'] = li_item_s04
    base['item_s05'] = li_item_s05
    base['item_s06'] = li_item_s06
    base['item_s07'] = li_item_s07
    base['item_s08'] = li_item_s08
    
    base['item_t01'] = li_item_t01
    base['item_t02'] = li_item_t02
    base['item_t03'] = li_item_t03
    
    base['color1'] = li_color1
    base['color2'] = li_color2
    base['color3'] = li_color3
    base['color4'] = li_color4
    base['case1'] = li_case1
    base['case2'] = li_case2
    base['case3'] = li_case3
    base['power1'] = li_power1
    base['power2'] = li_power2
    base['power3'] = li_power3
    base['power4'] = li_power4
    base['material1'] = li_material1
    base['material2'] = li_material2
    base['material3'] = li_material3
    base['mobility1'] = li_mobility1
    base['mobility2'] = li_mobility2
    base['mobility3'] = li_mobility3
    base['mobility4'] = li_mobility4
    base['brand1'] = li_brand1
    base['brand2'] = li_brand2
    base['brand3'] = li_brand3
    base['brand4'] = li_brand4
    base['perfect1_'] = li_perfect1_
    base['perfect2_'] = li_perfect2_
    base['perfect3_'] = li_perfect3_
#    base['item1_ '] = li_item1_
#    base['item2_ '] = li_item2_
#    base['item3_ '] = li_item3_
    base['color1_'] = li_color1_
    base['color2_'] = li_color2_
    base['color3_'] = li_color3_
    base['color4_'] = li_color4_
    
    base['brand_'] = li_brand_
    base['power_'] = li_power_
    base['mater_'] = li_mater_
    base['mobil_'] = li_mobil_
    base['case_'] = li_case_
    
    return base