# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 17:22:38 2016

@author: onodera
"""
import homedepot as hd
from operator import itemgetter
import numpy as np
import pandas as pd
import time
import os
import copy
# calc time
start = time.time()
ospid = os.getpid()
print 'ospid:',ospid
#==============================================================================
po,ps = hd.hdpath.load()
tr,prd = hd.load_all(onlytrain=True,mk_csv=True)
base = pd.merge(tr,prd,on='pid',how='left')[['pid','t_','s_','r']]

rr = [2.33, 2.67, 3.] #need 2.?

#items = pd.read_csv(ps+'item_tbl_selected.csv')['Unnamed: 0'].to_frame()
#items.columns = ['terms']
#items['order'] = 0

items = pd.read_csv(ps+'items_opted_5888_131.csv',index_col=0)
items.reset_index(drop=True,inplace=True)


# set your seed
seed = int(time.time())
np.random.seed(seed)
# GA parameter
POP = 10              #num of population
GLENGTH = len(items)
P_MUTATE = 0.002         #prob of mutation. reciprocal of len(GLENGTH) is better 
                       #total mutate are about POP*len(THRESHOLD)*P_MUTATE
P_CROSS = 0.            #rate of cross
GENERATION = 100000         #num of generations
#SELECTION_METHOD = 1    #1 is tournament. so far, only tournament
#TOURNAMENT_SIZE = 5	    #num of tournament. only effective in tournament

#==============================================================================
class Pop:
    def __init__(self):
        self.max_f = 0.0
        self.avg_f = 0.0
        self.min_f = 0.0
        self.genes = [None] * POP
        self.mk_genes()
        
    def mk_genes(self):
        for i in range(POP):
            self.genes[i] = Gene()
            
    def kill_genes(self):
        # kill duplicated genes
        uniq_list = []
        for i in range(POP):
            while str(self.genes[i].gtype) in uniq_list:
                self.genes[i].mutate()
            uniq_list.append(str(self.genes[i].gtype))
        
    def calc_f(self):
        tmp_fitness = []
        tmp_fitness_rank = []
        order_list = []
        ret_ptr = []
        avg = 0.0
        # get f
        for i in range(POP):
            if self.genes[i].f == 0:
                self.genes[i].get_f()
                print i,':',self.genes[i].f
        # sort by f
        for i in range(POP):
            tmp_fitness.append(self.genes[i].f)
            avg += self.genes[i].f
        avg = avg/POP
        self.avg_f = avg
        for i, e in enumerate(tmp_fitness):
            tmp_fitness_rank.append((i,e))
        tmp_fitness_rank = sorted(tmp_fitness_rank, key=itemgetter(1), reverse=True)  #True is dec
        for i in range(POP):
            order_list.append(tmp_fitness_rank[i][0])
        for i in order_list:
            ret_ptr.append(self.genes[i])
        self.genes = ret_ptr
        self.max_f = self.genes[0].f
        self.min_f = self.genes[POP-1].f
        
    def print_f(self):
        print 'ALL FITNESS IS...'
        for i in range(POP):
            print self.genes[i].f
        
    def generate_population(self):
#        num_of_elite = int(POP*ELITE_RATE) # define elite
        generated = 1
        # cross or mutate
        while (generated < POP):
            #Mutant 1
            self.genes[generated].mutate()
            generated += 1
    
    def copy_top_gene(self):
        for i in range(1,POP):
            self.genes[i].gtype = copy.copy(self.genes[0].gtype)
    

def get_item_list_in_list(li1,li2):
    for i in li1:
        if i in li2:
            return i
    return ''

def set_flg(base):
    li = []
    li += [(base.item[i] in base.t_[i])*1 for i in base.index]
    return li

def fitness_function(base):
    ave = 0
    for r in rr[:3]:
        ba = base[base.r==r][base.item!='']#.reset_index(drop=True,inplace=True)
        if len(ba)>0:
            ave += ba.match.mean()
    return ave/3.
    
class Gene:
    def __init__(self):
        self.f = 0.0
        self.gtype = range(GLENGTH)
    
    def get_f(self):
        items['order'] = self.gtype
        items.sort_values(by='order',inplace=True)
        base['item'] = base.s_.map(lambda x:get_item_list_in_list(items.terms.tolist(),x))
        items.sort_index(inplace=True)
        base['match'] = set_flg(base)
        self.f = fitness_function(base)
#        self.f = np.random.randint(100)
        
    def mutate(self):
        for i in range(GLENGTH):
            if np.random.uniform() < P_MUTATE:
                p1,p2 = np.random.randint(GLENGTH,size=2)
                self.gtype[p1],self.gtype[p2]=self.gtype[p2],self.gtype[p1]
        self.f = 0.0
#==============================================================================
# 
#==============================================================================
# initialize
pop = Pop()

for i in range(GENERATION):
    pop.kill_genes()
    pop.calc_f()
    pop.print_f()
    pop.copy_top_gene()
    pop.generate_population()
    
    elapsed_time = time.time() - start
    print 'elapsed_time:',(elapsed_time/60), "min"
    
    items['order'] = pop.genes[0].gtype
    items.sort_values(by='order',inplace=True)
    hd.out(items,'items_opted_'+str(ospid),True)
    items.sort_index(inplace=True)
    
# main
if __name__ == "__main__":

    print pop.genes[0].f
    








