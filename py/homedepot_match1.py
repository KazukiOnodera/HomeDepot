# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 19:55:56 2016

@author: Kazuki
"""
import homedepot as hd
import homedepot_match as hdm
import pandas as pd

    
def match_unmatch(base,prd):
    
#    li_query_syn =[]
#    li_syn = []
    
    li_t01,li_t02,li_t03,li_t04,li_t05 = [],[],[],[],[]
    li_t06,li_t07,li_t08,li_t09,li_t10 = [],[],[],[],[]
    li_t11,li_t12,li_t13,li_t14,li_t15 = [],[],[],[],[]
    li_t16,li_t17,li_t18,li_t19,li_t20 = [],[],[],[],[]
    li_t21,li_t22,li_t23,li_t24,li_t25 = [],[],[],[],[]
    li_t26,li_t27,li_t28,li_t29,li_t30 = [],[],[],[],[]
#    li_t31,li_t32,li_t33,li_t34,li_t35 = [],[],[],[],[]
#    li_t36,li_t37,li_t38,li_t39,li_t40 = [],[],[],[],[]
#    li_t41,li_t42,li_t43,li_t44,li_t45 = [],[],[],[],[]
#    li_t46,li_t47,li_t48,li_t49,li_t50 = [],[],[],[],[]
#    li_t51,li_t52,li_t53,li_t54,li_t55 = [],[],[],[],[]
#    li_t56,li_t57,li_t58,li_t59,li_t60 = [],[],[],[],[]
#    li_t61,li_t62,li_t63,li_t64,li_t65 = [],[],[],[],[]
#    li_t66,li_t67,li_t68,li_t69,li_t70 = [],[],[],[],[]
#    li_t71,li_t72,li_t73,li_t74,li_t75 = [],[],[],[],[]
#    li_t76,li_t77,li_t78,li_t79,li_t80 = [],[],[],[],[]
#    li_t81,li_t82,li_t83,li_t84,li_t85 = [],[],[],[],[]
    
    li_d01,li_d02,li_d03,li_d04,li_d05 = [],[],[],[],[]
    li_d06,li_d07,li_d08,li_d09,li_d10 = [],[],[],[],[]
    li_d11,li_d12,li_d13,li_d14,li_d15 = [],[],[],[],[]
    li_d16,li_d17,li_d18,li_d19,li_d20 = [],[],[],[],[]
    
    li_td01,li_td02,li_td03,li_td04,li_td05 = [],[],[],[],[]
    li_td06,li_td07,li_td08,li_td09,li_td10 = [],[],[],[],[]
    li_td11,li_td12,li_td13,li_td14,li_td15 = [],[],[],[],[]
    li_td16,li_td17,li_td18,li_td19,li_td20 = [],[],[],[],[]
    
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
    
    
    li_freq1,li_freq2,li_freq3 = [],[],[]
    
    merged = pd.merge(base,prd,on='pid',how='left')
    for i in merged.index:
        query = list(merged.s_[i])
        tt = merged.t_[i]
        desc = merged.d_[i]
        s_size = merged.s_size_[i]
        t_size = merged.t_size_[i]
        d_size = merged.d_size_[i]
        att_size = merged.att_size_[i]
        s_num = merged.s_num_[i]
        t_num = merged.t_num_[i]
        d_num = merged.d_num_[i]
#        query_syn,sw = hd.rep_syn(query,tt)
#        li_query_syn.append(query_syn)
#        li_syn.append(sw)
        """EVALUATE MATCH"""
        "title"
        li_t01.append(''.join(query) in ''.join(tt))
        li_t02.append(''.join(tt).count(''.join(query)))
        li_t03.append(hd.count_list_in_list(query,tt))
        li_t04.append(hdm.get_ratio_in_prd(query,tt))
        li_t05.append(hdm.get_ratio_in_prd(tt,query))
        li_t06.append(hdm.comb_match(query,tt))
        li_t07.append(hdm.back_is_important(query,tt))
        li_t08.append(hdm.is_all_in_back(query,tt))
        li_t09.append(hdm.is_hit_b4_prepos(query,tt,'in'))
        li_t10.append(hdm.is_hit_b4_prepos(query,tt,'with'))
        li_t11.append(hdm.is_hit_b4_prepos(query,tt,'for'))
        li_t12.append(query[0] in tt)
        li_t13.append(query[0] == tt[-1])
        li_t14.append(tt[-1] in query)
        li_t16.append(hdm.get_ind(tt[-1],query))
        li_t17.append(hdm.get_ind(query[0],tt))
        li_t18.append(hdm.get_ind(query[0],tt[::-1]))
        li_t19.append(tt[0] in query)
        
        v1,v2 = hdm.is_part_inc(query[0],tt)
        li_t20.append(v1)
        li_t21.append(v2)
        li_t22.append(hdm.is_prepos_after_word(query[0],tt,'in'))
        li_t23.append(hdm.is_prepos_after_word(query[0],tt,'with'))
        li_t24.append(hdm.is_prepos_after_word(query[0],tt,'for'))
        
        "DESCRIPTION"
        li_d01.append(''.join(query) in ''.join(desc))
        li_d02.append(''.join(desc).count(''.join(query)))
        li_d03.append(hd.count_list_in_list(query,desc))
        li_d04.append(hdm.get_ratio_in_prd(query,desc))
        li_d05.append(hdm.get_ratio_in_prd(desc,query))
        li_d06.append(hdm.comb_match(query,desc))
        li_d07.append(hdm.back_is_important(query,desc))
        li_d08.append(hdm.is_all_in_back(query,desc))
        li_d09.append(hdm.is_hit_b4_prepos(query,desc,'in'))
        li_d10.append(hdm.is_hit_b4_prepos(query,desc,'with'))
        li_d11.append(hdm.is_hit_b4_prepos(query,desc,'for'))
        li_d12.append(query[0] in desc)
        li_d13.append(hdm.get_ind(query[0],desc))
        li_d14.append(hdm.get_ind(query[0],desc[::-1]))
        li_d15.append(query[0] in ''.join(desc))
        li_d16.append(desc.count(query[0]))
        
        "TITLE & DESCRIPTION"
        li_td01.append(''.join(query) in ''.join(tt+desc))
        li_td02.append(''.join(tt+desc).count(''.join(query)))
        li_td03.append(hd.count_list_in_list(query,tt+desc))
        li_td04.append(hdm.get_ratio_in_prd(query,tt+desc))
        li_td05.append(hdm.get_ratio_in_prd(tt+desc,query))
        li_td06.append(query[0] in tt+desc)
        li_td07.append(hdm.get_ind(query[0],tt+desc))
        li_td08.append((tt+desc).count(query[0]))
        #TODO:position(sentense part),ambiguous match
        
        "size,num"#TODO:weight
        li_size1.append(hd.is_list_in_list(s_size,t_size))
        li_size2.append(hd.is_list_in_list(s_size,d_size))
        li_size3.append(hd.is_list_in_list(s_size,att_size))
        li_size4.append(hd.is_list_in_list(s_size,t_size+d_size+att_size))
        li_size5.append(hdm.get_ratio_in_prd(s_size,t_size))
        li_size6.append(hdm.get_ratio_in_prd(s_size,d_size))
        li_size7.append(hdm.get_ratio_in_prd(s_size,att_size))
        li_size8.append(hdm.get_ratio_in_prd(s_size,list(set(t_size+d_size+att_size))))
        li_size9.append(hdm.get_ratio_in_prd(t_size,s_size))
        li_size10.append(hdm.get_ratio_in_prd(d_size,s_size))
        li_size11.append(hdm.get_ratio_in_prd(att_size,s_size))
        li_size12.append(hdm.get_ratio_in_prd(t_size+d_size+att_size,s_size))
        li_size13.append(hd.count_list_in_list(s_size,t_size))
        li_size14.append(hd.count_list_in_list(s_size,d_size))
        li_size15.append(hd.count_list_in_list(s_size,att_size))
        li_size16.append(hd.count_list_in_list(s_size,list(set(t_size+d_size+att_size))))
        
        li_num1.append(hd.is_list_in_list(s_num,tt))
        li_num2.append(hd.is_list_in_list(s_num,desc))
        li_num3.append(hd.is_list_in_list(s_num,tt+desc))
        li_num4.append(hdm.get_ratio_in_prd(t_num,s_num))
        li_num5.append(hdm.get_ratio_in_prd(d_num,s_num))
        li_num6.append(hdm.get_ratio_in_prd(t_num+d_num,s_num))
        
        "FREQ"
        li_freq1.append(hdm.get_freq(query[0]))
        
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
#        li_item7.append('' != merged.s_item_weight[i] and merged.s_item_weight[i] in tt)
#        li_item8.append('' != merged.s_item_weight[i] and merged.s_item_weight[i] in desc)
#        li_item6.append('' != merged.s_item2[i] and merged.s_item2[i] in tt+desc)
#        li_item7.append('' != merged.s_item_imp2[i] and hd.is_list_in_list(syn1,tt))
#        li_item8.append('' != merged.s_item_imp2[i] and hd.is_list_in_list(syn1,desc))
#        li_item9.append('' != merged.s_item1[i] and hd.is_list_in_list(syn1,tt+desc))
#        li_item10.append('' != merged.s_item1[i] and hd.count_list_in_list(syn1,tt))
#        li_item11.append('' != merged.s_item1[i] and hd.count_list_in_list(syn1,desc))
#        li_item12.append('' != merged.s_item1[i] and hd.count_list_in_list(syn1,tt+desc))
#        li_item13.append('' != merged.s_item2[i] and hd.is_list_in_list(syn2,tt))
#        li_item14.append('' != merged.s_item2[i] and hd.is_list_in_list(syn2,desc))
#        li_item15.append('' != merged.s_item2[i] and hd.is_list_in_list(syn2,tt+desc))
#        li_item16.append('' != merged.s_item2[i] and hd.count_list_in_list(syn2,tt))
#        li_item17.append('' != merged.s_item2[i] and hd.count_list_in_list(syn2,desc))
#        li_item18.append('' != merged.s_item2[i] and hd.count_list_in_list(syn2,tt+desc))
#        li_item19.append('' != merged.t_item1[i] and merged.t_item1[i] in query)
#        li_item20.append('' != merged.t_item2[i] and merged.t_item2[i] in query)
#        li_item21.append('' != merged.s_item1[i] and merged.s_item1[i] in ''.join(tt))
#        li_item22.append('' != merged.s_item1[i] and merged.s_item1[i] in ''.join(desc))
#        li_item23.append('' != merged.s_item2[i] and merged.s_item2[i] in ''.join(tt))
#        li_item24.append('' != merged.s_item2[i] and merged.s_item2[i] in ''.join(desc))
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
        li_brand2.append('' != merged.s_brand[i] and merged.s_brand[i] in desc) #TODO: handle 'sharkbite:shark'
        li_brand3.append('' != merged.s_brand[i] and merged.s_brand[i] in merged.p_brand_[i])
        li_brand4.append('' != merged.s_brand[i] and merged.s_brand[i] in ''.join(merged.p_brand_[i]))
#        
        """EVALUATE UNMATCH"""
        li_perfect1_.append(not hd.is_list_in_list(query,tt))
        li_perfect2_.append(not hd.is_list_in_list(query,desc))
        li_perfect3_.append(not hd.is_list_in_list(query,tt+desc))
        #TODO: title,desc kumiawase
#        li_item1_.append('' != merged.s_item1[i] and not hd.count_list_in_list(syn1,tt))
#        li_item2_.append('' != merged.s_item1[i] and not hd.count_list_in_list(syn1,desc))
#        li_item3_.append('' != merged.s_item1[i] and not hd.count_list_in_list(syn1,tt+desc))
        
        li_color1_.append('' != merged.s_color[i] and merged.s_color[i] not in tt)
        li_color2_.append('' != merged.s_color[i] and merged.s_color[i] not in desc)
        li_color3_.append('' != merged.s_color[i] and merged.s_color[i] not in merged.att_color_[i])
        li_color4_.append('' != merged.s_color[i] and merged.s_color[i] not in tt+desc+merged.att_color_[i])
        
        li_case_.append('' != merged.s_case[i] and merged.s_case[i] not in tt+desc)
        li_power_.append('' != merged.s_power[i] and merged.s_power[i] not in tt+desc+merged.att_power_[i])
        li_mater_.append('' != merged.s_material[i] and merged.s_material[i] not in tt+desc+merged.att_material_[i])
        li_mobil_.append('' != merged.s_mobility[i] and ('corded' in tt+desc or 'plug' in merged.att_power_[i]))
        li_brand_.append('' != merged.s_brand[i] and merged.s_brand[i] not in tt+desc+merged.p_brand_[i])
    
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
#    base['title15'] = li_t15
    base['title16'] = li_t16
    base['title17'] = li_t17
    base['title18'] = li_t18
    base['title19'] = li_t19
    base['title20'] = li_t20
    base['title21'] = li_t21
    base['title22'] = li_t22
    base['title23'] = li_t23
    base['title24'] = li_t24
#    base['title25'] = li_t25
#    base['title26'] = li_t26
#    base['title27'] = li_t27
#    base['title28'] = li_t28
#    base['title29'] = li_t29
#    base['title30'] = li_t30
#    base['title31'] = li_t31
#    base['title32'] = li_t32
#    base['title33'] = li_t33
#    base['title34'] = li_t34
#    base['title35'] = li_t35
#    base['title36'] = li_t36
#    base['title37'] = li_t37
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
    base['title_r2'] = base['title16']/merged['t_len']
    base['title_r3'] = base['title17']/merged['t_len']
    base['title_r4'] = base['title18']/merged['t_len']
#    base['title_r6'] = base['title53']/base['s_len']
#    base['title_r7'] = base['title63']/merged['t_main_len']
#    base['title_r8'] = base['title64']/merged['t_main_len']
#    base['title_r9'] = base['title65']/merged['t_main_len']
#    base['title_r10'] = base['title66']/merged['t_main_len']
    
    
    base['desc01'] = li_d01
    base['desc02'] = li_d02
    base['desc03'] = li_d03
    base['desc04'] = li_d04
    base['desc05'] = li_d05
    base['desc06'] = li_d06
    base['desc07'] = li_d07
    base['desc08'] = li_d08
    base['desc09'] = li_d09
    base['desc10'] = li_d10
    base['desc11'] = li_d11
    base['desc12'] = li_d12
    base['desc13'] = li_d13
    base['desc14'] = li_d14
    base['desc15'] = li_d15
    base['desc16'] = li_d16
    base['desc_r1'] = base['desc03']/base['s_len']
    base['desc_r2'] = base['desc13']/merged['d_len']
    base['desc_r3'] = base['desc14']/merged['d_len']
    
    base['td01'] = li_td01
    base['td02'] = li_td02
    base['td03'] = li_td03
    base['td04'] = li_td04
    base['td05'] = li_td05
    base['td06'] = li_td06
    base['td07'] = li_td07
    base['td08'] = li_td08
#    base['td09'] = li_td09
#    base['td10'] = li_td10
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