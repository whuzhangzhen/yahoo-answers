#coding:utf-8

import numpy
import matplotlib.pylab as plt
import networkx as nx
from random import random

def get_edges(file_name):
    #从主题词矩阵获取权重边元组
    edge_list=[]
    list1=[]
    list2=[]
    with open(file_name,'rb')as file:
        lines =file.readlines()
        for line in lines:
            if '类' in line:
                list1.append(line.split(':')[0])
               # print line
            else:
                #print line.split()
                list2.append(line.split())
    for i in range(16):
        for item in list2[20*i:20*(i+1)]:
            item.insert(0,i)
            edge_list.append(item)
    print edge_list
    return  edge_list

def show():
    edge_list= get_edges('data/topic_model/16.dat')
    G=nx.Graph()
    node_colors = [(random(),random(),random())for _i in range(5)]
    edge_colors=list(range(20*16))
    #for  list1 in edge_list:
    for item in edge_list:
             tuple(item)
    #print edge_list
    G.add_weighted_edges_from(edge_list)
    nx.draw(G, with_labels=True, node_size=400, edge_color=edge_colors,node_color=node_colors,font_size=6)
    plt.savefig('relation3.png',dpi=400)
    plt.show()

def main():

    show()
if __name__ == '__main__':
    main()
