#!/usr/bin/env python
# coding: utf-8

# In[5]:


graph = {
  'A' : ['B','E','C'],
  'B' : ['D', 'E','A'],
  'C' : ['F','G','A'],
  'D' : ['E','B'],
  'E' : ['B','D','A'],
  'F' : ['C'],
   'G': ['C'],
}
visited = [] 
queue = []   
def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
bfs(visited, graph, 'A')


# In[6]:


graph = {
  'A' : ['B','E','C'],
  'B' : ['D', 'E','A'],
  'C' : ['F','G','A'],
  'D' : ['E','B'],
  'E' : ['B','D','A'],
  'F' : ['C'],
   'G': ['C'],
}
visited = [] 
queue = []   
def bfs(visited, graph, node,end):
  visited.append(node)
  queue.append(node)
  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 
    if s==end:
        break
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
bfs(visited, graph, 'A','F')


# In[11]:


graph={
    '1':['2'],
    '2':['1','3'],
    '3':['4','2'],
    '4':['3','5','6'],
    '6':['4','7'],
    '7':['6','9','8'],
    '8':['7','10'],
    '9':['7','10'],
    '10':['11','8','9'],
    '11':['10','12'],
    '12':['11','13','14'],
    '13':['12'],
    '14':['12','15'],
    '15':['16','14'],
    '16':['25','15'],
    '25':['24','16'],
    '24':['23','25'],
    '23':['24','22'],
    '22':['21','23'],
    '21':['20','22'],
    '20':['19','21'],
    '19':['18','20'],
    '18':['17','19'],
    '17':['18','5'],
    '5':['4','17'],
}
visited = [] 
queue = []   
def bfs(visited, graph, node,end):
  visited.append(node)
  queue.append(node)
  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 
    if s==end:
        break
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
bfs(visited, graph, '1','16')


# In[12]:


graph={
    'Arab':['Zernid','Timisoara','Sibiu'],
    'Zernid':['Arab','Oradea'],
    'Timisoara':['Arab','Lugoj'],
    'Sibiu':['Rimnico vilcea','Arab','Oradea','Fagaras'],
    'Oradea':['Zernid','Sibiu'],
    'Lugoj':['Mehadia'],
    'Mehadia':['Drobeta'],
    'Craiova':['Drobeta','Pitesti','Rimnico vilcea'],
    'Drobeta':['Mehadia','Craiova'],
    'Pitesti':['Craiova','Rimnico vilcea','Bucharest'],
    'Rimnico vilcea':['Pitesti','Sibiu'],
    'Fagaras':['Sibiu','Bucharest'],
    'Bucharest':['Giurgiu','Urziceni','Pitesti','Fagaras'],
    'Giurgiu':['Bucharrest'],
    'Urziceni':['Hirsova','Valsui'],
    'Hirsova':['Eforie','Urziceni'],
    'Eforie':['Hirsova'],
    'Valsui':['Iasi','Urziceni'],
    'Iasi':['Valsui','Neamt'],
    'Neamt':['Iasi'],
}
visited = [] 
queue = []   
def bfs(visited, graph, node,end):
  visited.append(node)
  queue.append(node)
  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 
    if s==end:
        break
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
bfs(visited, graph, 'Arab','Bucharest')


# In[ ]:




