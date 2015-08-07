
file = 'SCC.txt'
import copy
import sys
sys.setrecursionlimit(500000)
length = 875714

def parse_file(file):
    with open(file) as f:
        dictionary = {}
        
        for i in range(1, length + 1):
            dictionary[i] = set([])
        
       
        for line in f: 
            number = line.strip().split(' ')
            number[0] = int(number[0])
            print number[0]
            number[1] = int(number[1])   
            dictionary[number[0]].update([number[1]])
  
                
    return dictionary            
            
dictionary = parse_file(file)       

print "Dictionary reading completed..."   

def graph_reversal(dictionary):
    dictionary_reversed = {}
    for i in range(1,length + 1):
        dictionary_reversed[i] = set([])
    for key,value in dictionary.items():
        for i in value:
            dictionary_reversed[i].update([key])
 
            
    
        
    return dictionary_reversed 

reversed_dictionary = graph_reversal(dictionary)    

print "Dictionary Reversal Completed..."


visited = set([])
t = 0
finishing_time = {}

def DFS_loop_pass_one(reversed_graph):
    import random
    #print reversed_graph
    remaining_nodes = reversed_graph.keys()
    while len(remaining_nodes) != 0:
        i = random.choice(remaining_nodes)
        visited = DFS_pass_one(reversed_graph,i)
        for i in visited:
            if i in remaining_nodes:
                remaining_nodes.remove(i)
        
def DFS_pass_one(reversed_graph, current_node):
    global visited
    visited.update([current_node])
    #print current_node
    for edge_node in reversed_graph[current_node]:
        if edge_node in visited:
            pass
        else:
            DFS_pass_one(reversed_graph, edge_node)
    global t 
    t = t + 1
    global finishing_time
    finishing_time[current_node] = t
    return visited
    
DFS_loop_pass_one(reversed_dictionary)

print "First PASS COMPLETED...."
#print finishing_time    
def re_reverse_and_modify_graph(dictionary):
    modified_dictionary = {}
    for key,value in dictionary.items():
        new_key = finishing_time[key]
        new_value = set([])
        for i in value:
            j = finishing_time[i]
            new_value.update([j])
            
        modified_dictionary[new_key] = new_value
    
    return modified_dictionary

modified_dictionary = re_reverse_and_modify_graph(dictionary)
#print modified_dictionary

visited_refreshed = set([])
leader = {}
s = None

def DFS_loop_pass_two(modified_graph):
    #print reversed_graph
    remaining_nodes = modified_graph.keys()
    global visited_refreshed
    for i in range(len(remaining_nodes),0,-1):
        if i in visited_refreshed:
            pass
        else:
            global s
            s = i
            DFS_pass_two(modified_graph,i)
                        
def DFS_pass_two(modified_graph, current_node):
    global visited_refreshed
    global leader
    
    try:
        visited_refreshed.update([current_node])
    except KeyError:
        visited_refreshed = set([current_node])
        
    #changed the key and value of reader for computation purposes
    try:
        leader[s].update([current_node])
    except KeyError:
        leader[s] = set([current_node])
    
    
    for edge_node in modified_graph[current_node]:
        if edge_node in visited_refreshed:
            pass
        else:
            DFS_pass_two(modified_graph, edge_node)

DFS_loop_pass_two(modified_dictionary)          

print "SECOND PASS COMPLETED..."
c = []
for i in leader.values():
     c.append(len(i))

print sorted(c, reverse = True)[0:4]     