# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 12:15:31 2016

@author: Kazuki
"""

#==============================================================================
import hdpath
path_org,path_sub = hdpath.load()
#==============================================================================

import re
import pandas as pd
import numpy as np
import time
import homedepot_product as hdp
import hd_list as hdl
from stemming.porter2 import stem

#syn_tbl = pd.read_csv(path_sub+'07syn.csv')

prepos = ['for','in','with','on','of','from']
conj = ['and','or']

"caetgory"
category_header = ['ca_timber','ca_inte','ca_garden','ca_kitchen','ca_bath',
                   'ca_bath2','ca_pet','ca_car','ca_outdoor','ca_reform',
                   'ca_tool','ca_drug']
ca_timber  = ['timber','lumber']
ca_inte    = ['interior','interiors','furniture','furniture','shelf','shelves']
ca_garden  = ['garden','gardens','gardening','gardenings','plant','planter',
              'patio']
ca_kitchen = ['kitchen','kitchens','cook','cooking']
ca_bath    = ['bath','bathroom','bathrooms','tub','tubs','bathtub','bathtubs']
ca_bath2   = ['shower','vanity','toilet','toilets']
ca_balc    = ['balcony']
ca_pet     = ['dog','cat','pet']
ca_car     = ['car','cars','bike','bikes']
ca_outdoor = ['outdoor','outdoors','camp']
ca_reform  = ['reform','reforms','repair','repairs']
ca_tool    = ['blade','blades','saw','chainsaw','knife','knives','nipper','nippers',
              'hammer','hammers','drill','drills','driver','drivers',
              'bolt','bolts']
ca_drug    = ['drug','drugs']
category = [ca_timber,ca_inte,ca_garden,ca_kitchen,ca_bath,ca_bath2,
            ca_pet,ca_car,ca_outdoor,ca_reform,ca_tool,ca_drug]

"power"
power_header = ['po_el','po_led','po_gas','po_mo']
po_el  = ['electric','electrical','electronic']
po_led = ['led']
po_gas = ['gas']
po_mo  = ['motor']
#power = [po_el,po_led,po_gas,po_mo]
power = ['electr', 'electron', 'led', 'gas', 'motor', 'oil', 'solar', 'propan',
         'halogen']

"material"
materials = ['steel', 'wood', 'plastic', 'vinyl', 'metal', 'aluminum', 'liquid',
             'stainless', 'bronz', 'zinc', 'stone', 'iron', 'ceram', 'copper',
             'rubbermaid', 'polyurethan', 'glass', 'plywood', 'pvc']
             
"mobility"
mobility = ['codeless', 'portabl', 'cordless', 'compact']

"case"
case = ['privaci', 'emerg', 'secur', 'repair', 'rain', 'christma']

"color"
colors = ['red','white','black','blue','yellow']

"size"
sizes = ['in.','ft.','oz.','cm.','mm.','deg.','volt.','watt.','amp.']

ng = hdp.ng
#TODO: descriptions are included many unnecessary words, 
#      so I have to find out how to evalate those

#==============================================================================
# def
#==============================================================================
def str_stem(s): 
    if isinstance(s, str):
        s = re.sub(r"(\w)\.([A-Z])", r"\1 \2", s) #Split words with a.A
        s = re.sub(r"\s([a-z]+)([A-Z])", r" \1 \2", s)
        s = s.replace("All-in-One","")
        s = s.replace("All in One","")
        s = s.replace("Built-in","")
        s = s.replace("Built in","")
        s = s.lower()
#        s = s.replace(",","") #could be number / segment later
        s = s.replace("hampton bay","hamptonbay")
        s = s.replace("air conditioner","airconditioner")
        s = s.replace("nail gun","nailgun")
        s = s.replace("home decorators","homedecorators")
        s = s.replace("hole saw","holesaw")
        s = s.replace("electrical","electric")
        s = s.replace("moulding","molding")
        s = s.replace("trash can","trashcan")
        s = s.replace("fire place","fireplace")
        s = s.replace("$"," ")
        s = s.replace("?"," ")
        s = s.replace("-"," ")
        s = s.replace("//","/")
        s = s.replace("..",".")
        s = s.replace(" / "," ")
        s = s.replace(" \\ "," ")
        s = s.replace("("," ")
        s = s.replace(")"," ")
        s = s.replace("{"," ")
        s = s.replace("}"," ")
        s = s.replace(":"," ")
#        s = s.replace("."," . ")
        s = s.replace('"',"")
        s = s.replace("'","")
#        s = re.sub(r"(^\.|/)", r"", s)
#        s = re.sub(r"(\.|/)$", r"", s)
        s = s.replace(" x "," xbi ")
        s = s.replace("*"," xbi ")
        s = s.replace(" by "," xbi")
        s = s.replace("x0"," xbi 0")
        s = s.replace("x1"," xbi 1")
        s = s.replace("x2"," xbi 2")
        s = s.replace("x3"," xbi 3")
        s = s.replace("x4"," xbi 4")
        s = s.replace("x5"," xbi 5")
        s = s.replace("x6"," xbi 6")
        s = s.replace("x7"," xbi 7")
        s = s.replace("x8"," xbi 8")
        s = s.replace("x9"," xbi 9")
        s = s.replace("0x","0 xbi ")
        s = s.replace("1x","1 xbi ")
        s = s.replace("2x","2 xbi ")
        s = s.replace("3x","3 xbi ")
        s = s.replace("4x","4 xbi ")
        s = s.replace("5x","5 xbi ")
        s = s.replace("6x","6 xbi ")
        s = s.replace("7x","7 xbi ")
        s = s.replace("8x","8 xbi ")
        s = s.replace("9x","9 xbi ")
        s = re.sub(r"([a-z]),", r"\1", s)
        s = re.sub(r"([0-9])([a-z])", r"\1 \2", s)
        s = re.sub(r"([a-z])([0-9])", r"\1 \2", s)
        s = re.sub(r"(\sx$)", r"\1bi", s)
        s = re.sub(r"([a-z])( *)\.( *)([a-z])", r"\1 \4", s)
        s = re.sub(r"([a-z])( *)/( *)([a-z])", r"\1 \4", s)
        s = s.replace("*"," xbi ")
        s = s.replace(" by "," xbi ")
        s = re.sub(r"([0-9])( *)\.( *)([0-9])", r"\1.\4", s)
        s = re.sub(r"([0-9]+)( *)(inches|inch|in)\.?", r"\1in. ", s)
        s = re.sub(r"([0-9]+)( *)(foot|feet|ft)\s", r"\1ft. ", s)
        s = re.sub(r"([0-9]+)( *)(pounds|pound|lbs|lb)\s", r"\1lb. ", s)
        s = re.sub(r"([0-9]+)( *)(square|sq) ?\.?(feet|foot|ft)\.?", r"\1sq.ft. ", s)
        s = re.sub(r"([0-9]+)( *)(cubic|cu) ?\.?(feet|foot|ft)\.?", r"\1cu.ft. ", s)
        s = re.sub(r"([0-9]+)( *)(gallons|gallon|gal)\.?", r"\1gal. ", s)
        s = re.sub(r"([0-9]+)( *)(ounces|ounce|oz)\.?", r"\1oz. ", s)
        s = re.sub(r"([0-9]+)( *)(centimeters|cm)\.?", r"\1cm. ", s)
        s = re.sub(r"([0-9]+)( *)(milimeters|mm)\.?", r"\1mm. ", s)
        s = re.sub(r"([a-z]+)( *)&amp;( *)\s", r"\1&", s)# 'pass &amp; seymour→'pass&seymour'
        s = s.replace("°"," degrees ")
        s = re.sub(r"([0-9]+)( *)(degrees|degree)\.?", r"\1deg. ", s)
        s = s.replace(" v "," volts ")
        s = re.sub(r"([0-9]+)( *)(volts|volt)\.?", r"\1volt. ", s)
        s = re.sub(r"([0-9]+)( *)(watts|watt)\.?", r"\1watt. ", s)
        s = re.sub(r"([0-9]+)( *)(amperes|ampere|amps|amp)\.?", r"\1amp. ", s)
        s = s.replace("  "," ")
        s = s.replace(" . "," ")
#        s = s.replace("airconditioner","air conditioner")
        s = (" ").join([stem(z) for z in s.split(" ")])
        s = s.replace("  "," ")
        return s
    else:
        return "null"
    
typo = [x[0] for x in hdl.typo]
def str_stem_for_typo_sub(s):
    if isinstance(s, str):
        if s in typo:
            ind = typo.index(s)
            s = hdl.typo[ind][1]
        return s
    else:
        return "null"
        
def fix_typo(li):
    return [str_stem_for_typo_sub(s) for s in li]

typo_g = [x[0] for x in hdl.typo_google]
def fix_typo_google(s):
    if isinstance(s, str):
        if s in typo_g:
            ind = typo_g.index(s)
            s = hdl.typo_google[ind][1]
        return s
    else:
        return "null"

def del_ng(li):
    return [s for s in li if s not in hdp.ng]
    
#def istypo(li,s):
    
def str_common_word(str1, str2):
    words, cnt = str1.split(), 0
    for word in words:
        if str2.find(word)>=0:
            cnt+=1
    return cnt

def str_whole_word(str1, str2, i_):
    cnt = 0
    while i_ < len(str2):
        i_ = str2.find(str1, i_)
        if i_ == -1:
            return cnt
        else:
            cnt += 1
            i_ += len(str1)
    return cnt
    
def get_sitem(li):
    li2 = list(li)
    if 'for' in li2:
        ind = li2.index('for')-1
        if ind>=0:
            return li2[ind]
    if 'with' in li2:
        ind = li2.index('with')-1
        if ind>=0:
            return li2[ind]
    if 'over' in li2:
        ind = li2.index('over')-1
        if ind>=0:
            return li2[ind]
    if 'in' in li2:
        ind = li2.index('in')-1
        if ind>=0:
            return li2[ind]
    for i in li:
        if i.isdigit():
            ind = li2.index(i)-1
            if ind>=0:
                return li2[ind]
            else:
                break
    li2 = [x for x in li2 if x not in ng+prepos and x.isalpha() and len(x)>2]
    if len(li2)>0:
        return li2[-1]
    return ''
    
def get_item_by_imp(li,imp):
    item = ''
    if is_list_in_list(li,imp.s.tolist()):
        ind = imp[imp.s.isin(li)].imp.argmax()
        item = imp.s[ind]
    return item
    
def mk_freq_table(s):
    li = []
    s = s.tolist()
    for i in range(len(s)):#i is index
        for j in s[i]:#j is word
            if j.isalpha():
                li.append(j)
    if len(li)>0:
        li = sorted(li)
        df = pd.DataFrame(li)
        df.columns = ['freq']
        freq_table = df.freq.value_counts()
        return freq_table
#    return []
    
def get_syn(w):
    li = []
    li += syn_tbl[syn_tbl.s==w].t.unique().tolist()
    return list(set(li)-set([w]))
    
def rep_syn(words,title):
    sw = False
    if len(words)<3:
        if is_list_in_list(words,syn_tbl.t.unique().tolist()):
            for w in words:
                if w in syn_tbl.t.unique().tolist() and not w in title:
                    syns = syn_tbl[syn_tbl.s==w].t.unique().tolist()
                    syn = get_item_list_in_list(syns,title)
                    if syn != 'null' and not syn in words:
                        ind = words.index(w)
                        words[ind] = syn
                        print "replace!!!",w,"-->>",syn
                        sw = True
    return words,sw
    
def rep_comb_sub(words,title):
#    words_ = list(words)
#    sw = 0
    if len(words)>1:
        for i in range(1,len(words)):
            ww = stem(words[i-1]+words[i])
            if ww in title:
                print ww,'exist!'
                words[i-1:i+1] = [ww]
                break
        for i in range(1,len(words)):
            ww = stem(words[i-1]+words[i])
            if ww in title:
                print ww,'exist!'
                words[i-1:i+1] = [ww]
                break
    return words
    
def rep_comb(df):
    for i in df.index:
        df.s_[i] = rep_comb_sub(df.s_[i],df.t_[i])
        if i%10==0:
            print 'index',i
    del df['t_']
    return df
    
def get_item_list_in_list(li1,li2):
    for i in li1:
        if i in li2:
            return i
    return ''
    
def count_list_in_list(li1,li2):
    if isinstance(li1, list) and isinstance(li2, list):
        cnt = 0
        for i in li1:
            cnt += li2.count(i)
        return cnt
    return -1
    
def is_list_in_list(li1,li2):
    if isinstance(li1, list) and isinstance(li2, list):
        for i in li1:
            if i in li2:
                return True
        return False
    return False
    
def get_size(li):
    size = []
    for i in li:
        if 'in.' in i:
            size.append(i.replace("in.","").replace("ft.",""))
    if 'xbi' in li:
        ind = li.index('xbi')
        if ind-1>=0:
            size.append(li[ind-1].replace("in.","").replace("ft.",""))
        if ind+1<len(li):
            size.append(li[ind+1].replace("in.","").replace("ft.",""))
    return list(set(size))
    
def get_num(s):
    li = []
    for w in s:
        if w.replace(".","").replace("/","").isdigit():
            li.append(w)
    return li
    
def get_category_in_search(tt):
    li = []
    lili =[]
    for i in tt.index:
        for ca in category:
            li.append(is_list_in_list(ca,tt.s_[i]))
        lili.append(li)
        li = []
    h = [x+'S' for x in category_header]
    df = pd.DataFrame(lili,columns=h)
    tt = pd.concat([tt,df],axis=1)
    col = [x for x in tt.columns if tt[x].dtype == 'bool']
    tt[col] = tt[col]*1
    return tt
    
def sparse_matrix(s,sli,col):
    li = []
    lili =[]
    for i in s.index:
        for x in sli:
            li.append(x in s[i])
        lili.append(li)
        li = []
    h = [x+col for x in sli]
    df = pd.DataFrame(lili,columns=h)
    return df*1
    
#def is_contain_w(li,w):
#    if w in li:
#        return True
#    return False
#    
def is_contain_words(li,words):
    cnt = 0
    for w in words:
        if w in li:
            cnt +=1
    if cnt == len(words):
        return True
    return False
    
def get_query_rarelity(query,title):
    cnt = 0
    for t in title:
        if len(query)==count_list_in_list(query,t):
            cnt +=1
    return cnt
    
def lowest_entropy_item(li,weight):
    if is_list_in_list(li,weight.s.tolist()):
        ind = weight[weight.s.isin(li)].w.argmin()
        return weight.s[ind]
    else:
        return ''
    
def get_score(merged,weight):
    sum_score = []
    ave_score = []
    max_score = []
    most_heavy_weight = []
    reg_sum_score = []
    reg_ave_score = []
    reg_max_score = []
    reg_most_heavy_weight = []
    mhw_in_title = []
    w0 = weight[weight.w==0].s.tolist()
    for i in merged.index:
        score = []
        reg_score = []
        words = [x for x in merged.s_[i] if x in weight.s.tolist() and x not in w0]
        if len(words)>0:
            weight_list = []
            reg_weight_list = []
            for j in words:
                weight_list.append(1./weight[weight.s==j].w.values[0])
            sum_w = sum(weight_list)
            for j in range(len(weight_list)):
                reg_weight_list.append(weight_list[j]/sum_w)
                score.append((words[j] in merged.t_[i])*1.*weight_list[j])
                reg_score.append((words[j] in merged.t_[i])*1.*reg_weight_list[j])
            sum_score.append(sum(score))
            ave_score.append(float(sum(score))/len(words))
            max_score.append(max(score))
            most_heavy_weight.append(max(weight_list))
            reg_sum_score.append(sum(score))
            reg_ave_score.append(float(sum(score))/len(words))
            reg_max_score.append(max(score))
            reg_most_heavy_weight.append(max(reg_weight_list))
            mhw_in_title.append((max(score)==max(weight_list))*1)
        else:
            sum_score.append(0)
            ave_score.append(0)
            max_score.append(0)
            most_heavy_weight.append(0)
            reg_sum_score.append(0)
            reg_ave_score.append(0)
            reg_max_score.append(0)
            reg_most_heavy_weight.append(0)
            mhw_in_title.append(-1)
    return sum_score,ave_score,max_score,most_heavy_weight,reg_sum_score,\
            reg_ave_score,reg_max_score,reg_most_heavy_weight,mhw_in_title
#==============================================================================
# #attributes
#==============================================================================
def load_att():
    infile = "attributes.csv"
    att = pd.read_csv(path_org+infile)
    #['product_uid', 'name','value']
    att.columns = [['pid', 'name','value']]
    return att
#==============================================================================
# train test
#==============================================================================

def load_all(size=1, onlytrain=False,mod='a',mk_csv=False,word=0):
    start = time.clock()
    if isinstance(mod,int) and not (0<=mod<=4):
        raise Exception("Invalid mod")
    if mod == 4:
        for i in range(4):
            if i == 0:
                tt = pd.read_csv(path_sub+'tt_mod'+str(i)+'.csv')
                prd = pd.read_csv(path_sub+'prd_mod'+str(i)+'.csv')
            else:
                tt = pd.concat([tt,pd.read_csv(path_sub+'tt_mod'+str(i)+'.csv')])
                prd = pd.concat([prd,pd.read_csv(path_sub+'prd_mod'+str(i)+'.csv')])
        prd.drop_duplicates(subset='pid',inplace=True)
        prd.reset_index(drop=True,inplace=True)
        tt.sort_values(by='id',inplace=True)
        tt.reset_index(drop=True,inplace=True)
        return tt,prd
            
    infile = "train.csv"
    train = pd.read_csv(path_org+infile)
    #['id', 'product_uid', 'product_title', 'search_term', 'relevance']
    train.columns = [['id','pid','t','s','r']]
    train.drop(['s'], axis=1, inplace=True)
    
    infile = "product_descriptions.csv"
    desc = pd.read_csv(path_org+infile)
    #['product_uid', 'product_description']
    desc.columns = [['pid','d']]
    
    if onlytrain:
        tt = train
        prd = tt.drop_duplicates(subset='pid').copy()
        prd.drop(['id', 'r'], axis=1, inplace=True)
        
    else:
        infile = "test.csv"
        test = pd.read_csv(path_org+infile)
        #['id', 'product_uid', 'product_title', 'search_term']
        test.columns = [['id','pid','t','s']]
        test.drop(['s'], axis=1, inplace=True)
        
        """train test"""
        tt = pd.concat([train,test])
        tt.reset_index(drop=True,inplace=True)
        """product_table"""
        prd = pd.concat([train,test])
        prd = prd.drop_duplicates(subset='pid')
        prd.drop(['id', 'r'], axis=1, inplace=True)
        
    """subset"""
    if size!=1:
        tt = tt.iloc[np.random.choice(len(tt),len(tt)*size,False)].reset_index(drop=True)
        prd = prd[prd.pid.isin(tt.pid)].reset_index(drop=True)
        
    if size==1 and isinstance(mod,int):
        tt = tt[tt.id%4==mod].reset_index(drop=True)
        prd = prd[prd.pid.isin(tt.pid)].reset_index(drop=True)
    
    """"============================
        SEARCH TERMS FEATURES
        ============================"""
    print '========== SEARCH =========='
    st = time.clock()
    tt.drop(['t'], axis=1, inplace=True)
    query = pd.read_csv(path_sub+'04query_comb.csv')
    tt = pd.merge(tt,query,on='id',how='left')
    tt['slen'] = tt.s.str.len()
    tt['s_'] = tt.s.str.split()
    tt['s_len'] = tt.s_.str.len()
    
    if isinstance(word,int) and (1<=word<=4):
        print 'extract length is:',word
        tt = tt[tt.s_len==word].reset_index(drop=True)
        prd = prd[prd.pid.isin(tt.pid)].reset_index(drop=True)
        
    if mk_csv:
        prd.reset_index(drop=True,inplace=True)
        prd['tlen'] = prd.t.str.len()
        prd['t_'] = prd.t.map(lambda x:str_stem(x)).str.split()
        prd.loc[:,'t_len'] = prd.t_.str.len()
        return tt,prd
        
    items = pd.read_csv(path_sub+'06sort_items_query.csv',index_col=0)['0'].tolist()
    tt['s_item_myrule'] = tt.s_.map(lambda x:get_sitem(x))
    tt['s_item_list'] = tt.s_.map(lambda x:get_item_list_in_list(items,x))
    tt['s_item'] = ''
    for i in tt.index:
        if tt['s_item_list'].values[i]=='':
            tt['s_item'].values[i] = tt['s_item_myrule'].values[i]
        else:
            tt['s_item'].values[i] = tt['s_item_list'].values[i]
#    tt['for'] = 
#    imp = pd.read_csv(path_sub+"04item_imp.csv")
#    tt['s_item_imp'] = tt.s_.map(lambda x:get_item_by_imp(x,imp))
    imp = pd.read_csv(path_sub+"04item_imp2.csv")
    tt['s_item_imp2'] = tt.s_.map(lambda x:get_item_by_imp(x,imp))
    weight = pd.read_csv(path_sub+"05tfidf_weight.csv")
    tt['s_item_weight'] = tt.s_.map(lambda x:lowest_entropy_item(x,weight))
    tt['s_size_'] = tt.s_.map(lambda x:get_size(x))
    tt['s_num_'] = tt.s_.map(lambda x:get_num(x))
#    sli = colors+power+materials+mobility+case
#    tt = pd.concat([tt,sparse_matrix(tt.s_,sli,'S')],axis=1)#SPARSE!!!
#    tt = get_category_in_search(tt)
    tt['s_color'] = tt.s_.map(lambda x:get_item_list_in_list(colors,x))
    tt['s_case'] = tt.s_.map(lambda x:get_item_list_in_list(case,x))
    tt['s_power'] = tt.s_.map(lambda x:get_item_list_in_list(power,x))
    tt['s_material'] = tt.s_.map(lambda x:get_item_list_in_list(materials,x))
    tt['s_mobility'] = tt.s_.map(lambda x:get_item_list_in_list(mobility,x))
#    freq_s = mk_freq_table(tt.s_)
#    freq_s = freq_s/freq_s.sum()
    print 'loaded SEARCH',time.clock() - st
    
    """"============================
        PRODUCT FEATURES
        ============================"""
    print '========== PRODUCT =========='
    prd = prd.sort_values(by='pid')
    "TITLE"
    st = time.clock()
    prd.reset_index(drop=True,inplace=True)
    prd['tlen'] = prd.t.str.len()
    prd['t_'] = prd.t.map(lambda x:str_stem(x)).str.split()
    prd['t_len'] = prd.t_.str.len()
    prd['t_main'] = prd.t_.map(lambda x:hdp.split_title(x))
    prd['t_main_len'] = prd.t_main.str.len()
#    prd['t_sub'] = prd.t_sub.str.len()
    items = pd.read_csv(path_sub+'06sort_items_title.csv',index_col=0)['0'].tolist()
    prd['t_item_myrule'] = hdp.pred_item_in_title(prd)
    prd['t_item_myrule'] = prd.t_item_myrule.map(lambda x:str_stem(x))
    prd['t_item_list'] = prd.t_.map(lambda x:get_item_list_in_list(items,x))
    prd['t_item'] = ''
    for i in prd.index:
        if prd['t_item_list'].values[i]=='':
            prd['t_item'].values[i] = prd['t_item_myrule'].values[i]
        else:
            prd['t_item'].values[i] = prd['t_item_list'].values[i]
    prd['t_item_imp'] = prd.t_.map(lambda x:get_item_by_imp(x,imp))
#    prd['t_item_weight'] = prd.t_.map(lambda x:lowest_entropy_item(x,weight))
    prd['t_size_'] = prd.t_.map(lambda x:get_size(x))
    prd['t_num_'] = prd.t_.map(lambda x:get_num(x))
#    prd = pd.concat([prd,sparse_matrix(prd.t_,sli,'T')],axis=1)#SPARSE!!!
#    prd = hdp.get_category_in_title(prd)
    prd['t_color'] = prd.t_.map(lambda x:get_item_list_in_list(colors,x))
    prd['t_case'] = prd.t_.map(lambda x:get_item_list_in_list(case,x))
    prd['t_power'] = prd.t_.map(lambda x:get_item_list_in_list(power,x))
    prd['t_material'] = prd.t_.map(lambda x:get_item_list_in_list(materials,x))
    prd['t_mobility'] = prd.t_.map(lambda x:get_item_list_in_list(mobility,x))
    print 'loaded title',time.clock() - st
    
    "DESCRIPTION"
    st = time.clock()
    prd = prd.merge(desc,on='pid')
    prd.reset_index(drop=True,inplace=True)
    prd['d_'] = prd.d.map(lambda x:str_stem(x)).str.split()
#    prd['d_'] = prd.d_.map(lambda x:del_ng(x))
    prd.loc[:,'d_len'] = prd.d_.str.len()
    prd['d_size_'] = prd.d_.map(lambda x:get_size(x))
    prd['d_num_'] = prd.d_.map(lambda x:get_num(x))
#    prd = pd.concat([prd,sparse_matrix(prd.d_,sli,'D')],axis=1)
#    prd = hdp.pred_item_in_desc(prd)
#    prd.d_item = prd.d_item.str.lower()
    prd = hdp.get_category_in_desc(prd)
    prd['d_item'] = prd.d_.map(lambda x:get_item_list_in_list(hdl.items,x))
    prd['d_color'] = prd.d_.map(lambda x:get_item_list_in_list(colors,x))
    prd['d_case'] = prd.d_.map(lambda x:get_item_list_in_list(case,x))
    prd['d_power'] = prd.d_.map(lambda x:get_item_list_in_list(power,x))
    prd['d_material'] = prd.d_.map(lambda x:get_item_list_in_list(materials,x))
    prd['d_mobility'] = prd.d_.map(lambda x:get_item_list_in_list(mobility,x))
    print 'loaded description',time.clock() - st
    
    "MERGE ATTRIBUTE"
    st = time.clock()
    prd = hdp.merge_att(prd)
    brand = pd.read_csv(path_sub+"01att_brand.csv").p_brand.unique().tolist()
    print 'loaded attribute',time.clock() - st
    
    "FERQ"
    st = time.clock()
#    freq_item     = mk_freq_table(prd.t_item_weight.str.split())
    freq_brand    = pd.read_csv(path_sub+"01att_brand.csv").p_brand.value_counts()
    freq_brand.name = 'freq'
#    prd = hdp.set_freq(prd,freq_item,'t_item_weight')
    prd = hdp.set_freq(prd,freq_brand,'p_brand')
    print ' FINISH !!!',time.clock() - st
    
    
    """"============================
        SEARCH 2
        ============================"""
    tt['s_brand'] = tt.s_.map(lambda x:get_item_list_in_list(brand,x))
#    tt['rarelity'] = tt.s_.map(lambda x:get_query_rarelity(x,prd.t_))
    
    """"============================
        SEARCH &&& PRODUCTS
        ============================"""
    print '========== SEARCH &&& PRODUCTS =========='
    st = time.clock()
    
    if word == 0:
        import homedepot_match as hdm
        tt = hdm.match_unmatch(tt,prd)
    elif word == 1:
        import homedepot_match1 as hdm1
        tt = hdm1.match_unmatch(tt,prd)
    elif word == 2:
        import homedepot_match2 as hdm2
        tt = hdm2.match_unmatch(tt,prd)
    elif word == 3:
        import homedepot_match3 as hdm3
        tt = hdm3.match_unmatch(tt,prd)
    elif word == 4:
        import homedepot_match4 as hdm4
        tt = hdm4.match_unmatch(tt,prd)
#    elif word == 5:
#        tt = hdm.match_unmatch5(tt,prd)
    
    merged = pd.merge(tt,prd,on='pid',how='left')
    weight = pd.read_csv(path_sub+"05tfidf_weight.csv")
    tt['TF_sum_score'],tt['TF_ave_score'],tt['TF_max_score'],tt['TF_most_heavy_weight'],\
    tt['TF_reg_sum_score'],tt['TF_reg_ave_score'],tt['TF_reg_max_score'],\
    tt['TF_reg_most_heavy_weight'],tt['TF_mhw_in_title'] = get_score(merged,weight)
    tt['TF_mhw_'] = tt['TF_most_heavy_weight']*tt['TF_mhw_in_title']
    tt['TF_reg_mhw_'] = tt['TF_reg_most_heavy_weight']*tt['TF_mhw_in_title']
    
#    weight = pd.read_csv(path_sub+"06entropy_weight1.csv")
#    tt['lowest_entropy_item'] = tt['s_'].map(lambda x:lowest_entropy_item(x,weight))
#    tt['EN_sum_score'],tt['EN_ave_score'],tt['EN_max_score'],tt['EN_most_heavy_weight'],\
#    tt['EN_reg_sum_score'],tt['EN_reg_ave_score'],tt['EN_reg_max_score'],\
#    tt['EN_reg_most_heavy_weight'],tt['EN_mhw_in_title'] = get_score(merged,weight)
#    tt['EN_mhw_'] = tt['EN_most_heavy_weight']*tt['EN_mhw_in_title']
#    tt['EN_reg_mhw_'] = tt['EN_reg_most_heavy_weight']*tt['EN_mhw_in_title']
    
    tt['product_info'] = merged['s_'].map(lambda x:' '.join(x))+"\t"+\
                         merged['t_'].map(lambda x:' '.join(x)) +"\t"+\
                         merged['d_'].map(lambda x:' '.join(x))
    tt['query_in_title'] = tt['product_info'].map(lambda x:str_whole_word(x.split('\t')[0],x.split('\t')[1],0))
    tt['query_in_description'] = tt['product_info'].map(lambda x:str_whole_word(x.split('\t')[0],x.split('\t')[2],0))
    tt['word_in_title'] = tt['product_info'].map(lambda x:str_common_word(x.split('\t')[0],x.split('\t')[1]))
    tt['word_in_description'] = tt['product_info'].map(lambda x:str_common_word(x.split('\t')[0],x.split('\t')[2]))
    tt['ratio_title'] = tt['word_in_title']/tt['s_len']
    tt['ratio_description'] = tt['word_in_description']/tt['s_len']
    
#    tt['syn_product_info'] = merged['s_syn'].map(lambda x:' '.join(x))+"\t"+\
#                             merged['t_'].map(lambda x:' '.join(x)) +"\t"+merged['d_'].map(lambda x:' '.join(x))
#    tt['syn_query_in_title'] = tt['syn_product_info'].map(lambda x:str_whole_word(x.split('\t')[0],x.split('\t')[1],0))
#    tt['syn_query_in_description'] = tt['syn_product_info'].map(lambda x:str_whole_word(x.split('\t')[0],x.split('\t')[2],0))
#    tt['syn_word_in_title'] = tt['syn_product_info'].map(lambda x:str_common_word(x.split('\t')[0],x.split('\t')[1]))
#    tt['syn_word_in_description'] = tt['syn_product_info'].map(lambda x:str_common_word(x.split('\t')[0],x.split('\t')[2]))
#    tt['syn_ratio_title'] = tt['syn_word_in_title']/tt['s_len']
#    tt['syn_ratio_description'] = tt['syn_word_in_description']/tt['s_len']
    
    tt['attr'] = tt['s_'].map(lambda x:' '.join(x))+"\t"+merged['p_brand']
    tt['word_in_brand'] = tt['attr'].map(lambda x:str_common_word(x.split('\t')[0],x.split('\t')[1]))
    tt['len_of_brand'] = merged.p_brand.str.split().str.len()
    tt['ratio_brand'] = tt['word_in_brand']/tt['len_of_brand']
    df_brand = pd.unique(merged.p_brand.ravel())
    d={}
    i = 1
    for s in df_brand:
        d[s]=i
        i+=1
    tt['brand_feature'] = merged['p_brand'].map(lambda x:d[x])
    
    col = [x for x in tt.columns if tt[x].dtype == 'bool']
    tt[col] = tt[col]*1
    print ' FINISH !!!',time.clock() - st
    print ' TOTAL TIME:',time.clock() - start
    
    if mod == 'a':
        return tt,prd
    
    
    out(prd,'prd_mod'+str(mod))
    out(tt,'tt_mod'+str(mod))
    print "FINISH"
    return "FINISH","FINISH"


#==============================================================================
# sub
#==============================================================================
def load_sub():
    infile = "sample_submission.csv"
    sub = pd.read_csv(path_org+infile)
    #['id', 'relevance']
    return sub
    
def out(sub,name,index=False):
    sub.to_csv(path_sub+name+".csv",index=index)

def find_next(s,li):
    li = ['will']
    ng = ['not','be','never','also']
    find = []
    for i in range(len(s)):
        for j in li:
            if j in s[i]:
                ind = s[i].index(j)
                if ind+1 < len(s[i]):
                    if s[i][ind+1].isalpha() and s[i][ind+1] not in ng:
                        find.append(s[i][ind+1])
    find = sorted(find)
    df = pd.DataFrame(find)
    df.columns = ['freq']
    freq_table = df.freq.value_counts()
    return freq_table
    
def find_before(s,li):
    ng = []
    find = []
    for i in range(len(s)):
        for j in li:
            if j in s[i]:
                ind = s[i].index(j)
                if ind != 0 and s[i][ind-1].isalpha() and s[i][ind-1] not in ng:
                    find.append(s[i][ind-1])
    find = sorted(find)
    df = pd.DataFrame(find)
    df.columns = ['freq']
    freq_table = df.freq.value_counts()
    return freq_table




if __name__ == "__main__":
    """FOR DEBUG!!!"""
#    prd[prd.pid.duplicated()].pid

    
#    tag = 'item' # title, last, item, brand, power, mobility, material, color, size
    
#    col = ['t_','t_main','s','s_','title06','title07','title08',
#           'title19','title20','title26','title27','title28',
#           'title70', 'title71','r']
    
    col = ['t_','t_main','s','s_','title23','title24','title25',
           'r']
           
#    col = ['t_','p_brand',
#           's_','s_brand','brand1','brand2','brand3','brand4','r']
#           
    col = ['t','t_','t_item_myrule',
           's','s_','s_item_myrule','s_item2','r']#item myrurle
    
    merged = tt.merge(prd,on='pid')
    subset = merged[col]
    
    def match_count_li_in_li(li1,li2):
        if isinstance(li1, list) and isinstance(li2, list):
            cnt = 0
            for i in range(len(li1)):
                if li1[i]==li2[i]:
                    cnt += 1
            return cnt
        return -1
        
    def debug(df):
        low = df[df.r<2].reset_index(drop=True)
        high = df[df.r>2.3].reset_index(drop=True)
        col = [x for x in df.columns if 't' in x][:20]
#        col = ['title06','title07','title08','title09']
        debug = False
        ind = low.index.tolist()
        np.random.shuffle(ind)
        for i in ind:
            for j in high.index:
                if match_count_li_in_li(low[col].values[i].tolist(),\
                                        high[col].values[j].tolist())>len(col)*0.8:
#                    debug = pd.concat([low.ix[i,],high.ix[j,]])
                    debug = df[df.id.isin([low.id.values[i],high.id.values[j]])]\
                                [['t_','s_','s_item','r']+col]
                    break
            break
        return debug
    
    subset = debug(merged)
    
    
    
    
    
    
    
    
    



