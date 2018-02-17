# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 07:05:35 2016

@author: Kazuki
"""
import pandas as pd
import homedepot as hd

ng = ['base','comb','combo','set','sets','kit','kits','system','systems','ii','case',
      'unit','top','onli','accessori','pack']


    
def split_title(tt):
    tt_ = list(tt)
    if hd.is_list_in_list(['in','with','for'],tt_):
        ind_in = ind_with = ind_for =len(tt_)
        if 'in' in tt_:
            ind_in = tt_.index('in')
        if 'with' in tt_:
            ind_with = tt_.index('with')
        if 'for' in tt_:
            ind_for = tt_.index('for')
        ind = min(ind_in,ind_with,ind_for)
        tt_main = tt_[:ind]
#        tt_sub = tt_[ind:]
        return tt_main#tt_sub
    return ''#''
    
def pred_item_in_title(prd):
    li_b4_in_with = []
    li_b4_in = []
    li_b4_with = []
    li_last = []
    li_item = []
    ng2 = ng + hd.colors + hd.prepos
    for i in prd.index:
        t_ = list(prd.t_[i])
        t_ = [x for x in t_ if x not in ng]
        
        if 'in' in t_ and 'with' in t_:
            ind_in = t_.index('in')
            ind_with = t_.index('with')
            if ind_in>ind_with:
                ind = ind_with
            else:
                ind = ind_in
            w = t_[ind-1]
            if not w.isalpha():
                w = 'null'
            li_b4_in_with.append(w)
        else:
            li_b4_in_with.append('null')
            
        if 'in' in t_ and li_b4_in_with[i] == 'null' and 'in' != t_[0]:
            ind_in = t_.index('in')
            for k in range(ind_in)[::-1]:
                w = t_[k]
                if w==t_[0]:
                    li_b4_in.append('null')
                    break
                elif w.lower() not in ng2 and w.isalpha() and len(w)>2:
                    li_b4_in.append(w)
                    break
        else:
            li_b4_in.append('null')
            
        if 'with' in t_ and li_b4_in_with[i] == 'null' and 'with' != t_[0]:
            ind_with = t_.index('with')
            for k in range(ind_with)[::-1]:
                w = t_[k]
                if w==t_[0]:
                    li_b4_with.append('null')
                    break
                elif w.lower() not in ng2 and w.isalpha() and len(w)>2:
                    li_b4_with.append(w)
                    break
        else:
            li_b4_with.append('null')
            
        if 'null' == li_b4_in_with[i] == li_b4_in[i] == li_b4_with[i]:
            if ')' == prd.t[i][-1]:
                for j in prd.t[i].split():
                    if '(' in j:
                        ind = prd.t[i].split().index(j)
                        for k in range(ind)[::-1]:
                            w = prd.t[i].split()[k]
                            if w == prd.t[i].split()[0]:
                                li_last.append('null')
                                break
                            elif w.lower() not in ng2 and w.isalpha() and len(w)>2:
                                li_last.append(w)
                                break
                        break
            else:
                for j in prd.t_[i][::-1]:
                    if j == prd.t_[i][0]:
                        li_last.append('null')
                        break
                    elif j not in ng2 and j.isalpha() and len(j)>2:
                        li_last.append(j)
                        break
        else:
            li_last.append('null')
            
        if li_b4_in_with[i] not in ['null']+ng2:
            li_item.append(li_b4_in_with[i])
        elif li_b4_in[i] not in ['null']+ng2:
            li_item.append(li_b4_in[i])
        elif li_b4_with[i] not in ['null']+ng2:
            li_item.append(li_b4_with[i])
        elif li_last[i] not in ['null']+ng2:
            li_item.append(li_last[i])
        else:
            li_item.append('null')
            
    print len(li_last),len(prd)
#    prd['t_b4_in_with'] = li_b4_in_with
#    prd['t_b4_in'] = li_b4_in
#    prd['t_b4_with'] = li_b4_with
#    prd['t_last'] = li_last
    return li_item
    
def get_category_in_title(prd):
    li = []
    lili =[]
    for i in prd.index:
        for ca in hd.category:
            li.append(hd.is_list_in_list(ca,prd.t_[i]))
        lili.append(li)
        li = []
    h = [x+'T' for x in hd.category_header]
    df = pd.DataFrame(lili,columns=h)
    prd = pd.concat([prd,df],axis=1)
    col = [x for x in prd.columns if prd[x].dtype == 'bool']
    prd[col] = prd[col]*1
    return prd
    
def get_category_in_desc(prd):
    li = []
    lili =[]
    for i in prd.index:
        for ca in hd.category:
            li.append(hd.is_list_in_list(ca,prd.d_[i]))
        lili.append(li)
        li = []
    h = [x+'D' for x in hd.category_header]
    df = pd.DataFrame(lili,columns=h)
    prd = pd.concat([prd,df],axis=1)
    col = [x for x in prd.columns if prd[x].dtype == 'bool']
    prd[col] = prd[col]*1
    return prd
    
def pred_item_in_desc(prd):
    #TODO:later
    return
    
def rep_alpha(s):
    if isinstance(s,str):
        if ' in' in s:
            s = s.translate(None,' in')
        if ' lb' in s:
            s = s.translate(None,' lb')
        if ' ' in s:
            s = s.translate(None,' ')
    return s
    
def get_size(prd):
    pid = prd.pid.tolist()
    att = hd.load_att()
    att = att[att.pid.isin(pid)]
    depth = att[att.name.str.contains('Depth')==True]
    depth.value = depth.value.map(lambda x:rep_alpha(x))
    depth = depth[depth.value.str.replace(".","").str.isdigit()==True]
    
    height = att[att.name.str.contains('Height')==True]
    height.value = height.value.map(lambda x:rep_alpha(x))
    height = height[height.value.str.replace(".","").str.isdigit()==True]
    
    width = att[att.name.str.contains('Width')==True]
    width.value = width.value.map(lambda x:rep_alpha(x))
    width = width[width.value.str.replace(".","").str.isdigit()==True]
    
    weight = att[att.name.str.contains('Weight')==True]
    weight.value = weight.value.map(lambda x:rep_alpha(x))
    weight = weight[weight.value.str.replace(".","").str.isdigit()==True]
    del weight['name']
    
    merged = pd.concat([depth,height,width])
    del merged['name']
    merged.sort_values(by='pid',inplace=True)
    merged.reset_index(drop=True,inplace=True)
    
    li = []
    for pid in merged.pid.unique().tolist():
        li.append([int(pid),merged[merged.pid==pid].value.tolist()])
    size = pd.DataFrame(li,columns=['pid','att_size_'])
    prd = pd.merge(prd,size,on='pid',how='left')
    
    li = []
    for pid in weight.pid.unique().tolist():
        li.append([int(pid),weight[weight.pid==pid].value.tolist()])
    weight = pd.DataFrame(li,columns=['pid','att_weight_'])
    prd = pd.merge(prd,weight,on='pid',how='left')
    
    return prd
    
def get_att_sub(base,name):
    pid = base.pid.tolist()
    att = hd.load_att()
    att = att[att.name==name]
    del att['name']
    att.columns = [['pid',name]]
    att = att[att.pid.isin(pid)]
    att[name] = att[name].map(lambda x:hd.str_stem(x)).str.split()
    dup_pids = att[att.pid.duplicated()].pid.tolist()
    dup_inds = att[att.pid.duplicated()].index.tolist()#second ind
    if len(dup_pids)>0:
        for i,j in zip(dup_pids,dup_inds):
            att[name][j] = sum(att[att.pid==i][name].tolist(),[])
        att.drop_duplicates(subset='pid',keep='last',inplace=True)
    return pd.merge(base,att,on='pid',how='left')
    
def get_att(base):
    base = get_att_sub(base,'Style Type')
    base = get_att_sub(base,'Application Method')
    base = get_att_sub(base,'Interior/Exterior')
    base = get_att_sub(base,'Indoor/Outdoor')
    base = get_size(base)
    base.reset_index(drop=True,inplace=True)
    return base
    
def merge_att(prd):
    infile = "01att_brand.csv"
    df = pd.read_csv(hd.path_sub+infile)
    prd = pd.merge(prd,df,on='pid',how='left')
    
    infile = "02att_color_power_material.csv"
    df = pd.read_csv(hd.path_sub+infile)
    prd = pd.merge(prd,df,on='pid',how='left')
    prd.att_color.fillna('',inplace=True)
    prd.att_power.fillna('',inplace=True)
    prd.att_material.fillna('',inplace=True)
    
    infile = "03att_size_weight.csv"
    df = pd.read_csv(hd.path_sub+infile)
    prd = pd.merge(prd,df,on='pid',how='left')
    prd.att_size.fillna('',inplace=True)
    prd.att_weight.fillna('',inplace=True)
    
    prd['p_brand_'] = prd.p_brand.map(lambda x:hd.str_stem(x)).str.split()
    prd['att_color_'] = prd.att_color.str.split()
    prd['att_power_'] = prd.att_power.str.split()
    prd['att_material_'] = prd.att_material.str.split()
    prd['att_size_'] = prd.att_size.str.split()
    prd['att_weight_'] = prd.att_weight.str.split()
    
    return prd
    
    
def set_freq(prd,freq,key):
    freq = freq.to_frame()
    freq[key] = freq.index
    freq.columns = [[key+'_freq',key]]
    prd = pd.merge(prd,freq,on=key,how='left')
    return prd

def t_d_match(df,freq_s,freq_t,freq_noun):
    t_d_matchs = []
    items = []
    ng = hd.prepos + hd.colors + ['xbi','and','pro','or','ft.','pack','set','kit'] + hd.materials+hd.power
    t_ = df.t_
    d_ = df.d_
    for i in df.index:
        t__ = hd.get_syns(t_[i])
        t_d_match = list(set(t__+t_[i]) & set(d_[i]))
        t_d_matchs.append(t_d_match)
        best_w = ""
        best_score = 0
        score = 0
        
        "get item"
        if 'tile' in t_[i] or 'tiles' in t_[i]:
            items.append('tile')
            
#        elif 'kit' in t_[i]:
#            for w in t_d_match:
#                if w not in ng and w.isalpha() and w in freq_s and w in freq_t and \
#                    w in freq_noun and w != t_[i][0] and len(w)>2 and w != 'kit':
#                    score = freq_s[freq_s.index==w].values[0]*3\
#                            +freq_t[freq_t.index==w].values[0]\
#                            +freq_noun[freq_noun.index==w].values[0]
#                    if best_score<score:
#                        best_score = score
#                        best_w = w
#            if best_w =="":
#                ind = t_[i].index('kit')
#                best_w = t_[i][ind-1]
#            items.append(best_w)
            
        elif 'in' in t_[i] and 'with' in t_[i]:
            ind_in = t_[i].index('in')
            ind_with = t_[i].index('with')
            if ind_in>ind_with:
                ind = ind_with
            else:
                ind = ind_in
            w = t_[i][ind-1]
            if w not in ['all','only','top']:
                items.append(w)
            else:
                for w in t_d_match:
                    if w not in ng and w.isalpha() and w in freq_s and w in freq_t and \
                        w in freq_noun and w != t_[i][0] and len(w)>2:
                        score = freq_s[freq_s.index==w].values[0]*3\
                                +freq_t[freq_t.index==w].values[0]\
                                +freq_noun[freq_noun.index==w].values[0]
                        if best_score<score:
                            best_score = score
                            best_w = w
                if best_w =="":
                    best_w = t_[i][-1]
                items.append(best_w)
                
        elif 'in' in t_[i]:
            ind = t_[i].index('in')
            w = t_[i][ind-1]
            if w not in ['all','only','top']:
                items.append(w)
            else:
                for w in t_d_match:
                    if w not in ng and w.isalpha() and w in freq_s and w in freq_t and \
                        w in freq_noun and w != t_[i][0] and len(w)>2:
                        score = freq_s[freq_s.index==w].values[0]*3\
                                +freq_t[freq_t.index==w].values[0]\
                                +freq_noun[freq_noun.index==w].values[0]
                        if best_score<score:
                            best_score = score
                            best_w = w
                if best_w =="":
                    best_w = t_[i][-1]
                items.append(best_w)
                
        elif 'with' in t_[i]:
            ind = t_[i].index('with')
            w = t_[i][ind-1]
            if w not in ['all','only','top']:
                items.append(w)
            else:
                for w in t_d_match:
                    if w not in ng and w.isalpha() and w in freq_s and w in freq_t and \
                        w in freq_noun and w != t_[i][0] and len(w)>2:
                        score = freq_s[freq_s.index==w].values[0]*3\
                                +freq_t[freq_t.index==w].values[0]\
                                +freq_noun[freq_noun.index==w].values[0]
                        if best_score<score:
                            best_score = score
                            best_w = w
                if best_w =="":
                    best_w = t_[i][-1]
                items.append(best_w)
        else:
            for w in t_d_match:
                if w not in ng and w.isalpha() and w in freq_s and w in freq_t and \
                    w in freq_noun and w != t_[i][0] and len(w)>2:
                    score = freq_s[freq_s.index==w].values[0]*3\
                            +freq_t[freq_t.index==w].values[0]\
                            +freq_noun[freq_noun.index==w].values[0]
                    if best_score<score:
                        best_score = score
                        best_w = w
            if best_w =="":
                for w in t_d_match+t_[i]:
                    if w not in ng and w.isalpha() and w in freq_s and w in freq_t and \
                         w != t_[i][0] and len(w)>2:
                        score = freq_s[freq_s.index==w].values[0]\
                                +freq_t[freq_t.index==w].values[0]
                        if best_score<score:
                            best_score = score
                            best_w = w
            items.append(best_w)
            
    df.loc[:,'match'] = t_d_matchs
    df.loc[:,'p_item'] = items
    return df

def get_item_syn(base):
    df = base.copy()
    freq = hd.mk_freq_table(base.d_)
    other = freq.index.tolist()[:10]+['xbi']
    df = df.drop_duplicates(subset='p_item')
    df = df.reset_index()
    item_syns = []
    items = df.p_item
    for i in df.index:
        item = items[i]
        if item.isalpha():
            freq = hd.mk_freq_table(pd.concat([base[base.p_item==item].match,
                                            base[base.p_item==item].t_]))
            if len(freq)>0:
                item_syns.append(list(set(freq.index.tolist()[:15])- \
                set(hd.prepos+hd.colors+hd.conj+other)))
            else:
                item_syns.append([])
        else:
            item_syns.append([])
    df.loc[:,'p_item_analogy'] = item_syns
    base = pd.merge(base,df[['p_item','p_item_analogy']],on='p_item',how='left')
    return base