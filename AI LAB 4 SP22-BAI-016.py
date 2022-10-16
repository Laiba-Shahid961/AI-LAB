#!/usr/bin/env python
# coding: utf-8

# In[17]:


class dfss:
    def __init__(self,visited,graph):
        self.visited=visited
        self.graph=graph
    def dfs(self,node):
        if node not in self.visited:
            print (node)
            self.visited.add(node)
            for self.neighbour in self.graph[node]:
                self.dfs(self.neighbour)
obj=dfss(visited, graph)

graph = {
  'A' : ['B','E','C'],
  'B' : ['D', 'E','A'],
  'C' : ['F','G','A'],
  'D' : ['E','B'],
  'E' : ['B','D','A'],
  'F' : ['C'],
   'G': ['C'],
}

visited = set() 
obj.dfs('A')


# In[21]:


class dfss:
    def __init__(self,visited,graph,end):
        self.visited=visited
        self.graph=graph
        self.end=end
    def dfs(self,node):
        if node not in self.visited:
            print (node)
            self.visited.add(node)
            if node!=self.end:
                for self.neighbour in self.graph[node]:
                    self.dfs(self.neighbour)
visited = set() 
obj=dfss(visited, graph,'C')
graph = {
  'A' : ['B','E','C'],
  'B' : ['D', 'A','E'],
  'C' : ['F','G','A'],
  'D' : ['B','E'],
  'E' : ['B','D','A'],
  'F' : ['C'],
   'G': ['C'],
}


obj.dfs('D')


# In[25]:


class dfss:
    def __init__(self,visited,graph,end):
        self.visited=visited
        self.graph=graph
        self.end=end
    def dfs(self,node):
        if node not in self.visited:
            print (node)
            self.visited.add(node)
            if node!=self.end:
                for self.neighbour in self.graph[node]:
                    self.dfs(self.neighbour)
visited = set() 
obj=dfss(visited, graph,'Bucharest')
graph={
    'Arab':['Zernid','Timisoara','Sibiu'],
    'Zernid':['Arab','Oradea'],
    'Timisoara':['Arab','Lugoj'],
    'Sibiu':['Rimnico vilcea','Arab','Oradea'],
    'Oradea':['Zernid','Sibiu'],
    'Lugoj':['Mehadia','Timisoara'],
    'Mehadia':['Drobeta','Lugoj'],
    'Craiova':['Drobeta','Pitesti','Rimnico vilcea'],
    'Drobeta':['Mehadia','Craiova'],
    'Pitesti':['Craiova','Rimnico vilcea','Bucharest'],
    'Rimnico vilcea':['Pitesti','Sibiu','Craiova'],
    'Fagaras':['Sibiu','Bucharest'],
    'Bucharest':['Giurgiu','Urziceni','Pitesti','Fagaras'],
    'Giurgiu':['Bucharrest'],
    'Urziceni':['Hirsova','Valsui','Bucharest'],
    'Hirsova':['Eforie','Urziceni'],
    'Eforie':['Hirsova'],
    'Valsui':['Iasi','Urziceni'],
    'Iasi':['Valsui','Neamt'],
    'Neamt':['Iasi'],
}
obj.dfs('Arab')


# In[6]:



dictionary = ["START", "NOTE", "SAND", "STONED"]
n = len(dictionary)
M = 4
N = 4
def isWord(Str):
    for i in range(n):
        if (Str == dictionary[i]):
            return True
    return False
def findWordsUtil(boggle, visited, i, j, Str):
    visited[i][j] = True
    Str = Str + boggle[i][j]
    if (isWord(Str)):
        print(Str)
    row = i - 1
    while row <= i + 1 and row < M:
        col = j - 1
        while col <= j + 1 and col < N:
            if (row >= 0 and col >= 0 and not visited[row][col]):
                findWordsUtil(boggle, visited, row, col, Str)
            col+=1
        row+=1
    Str = "" + Str[-1]
    visited[i][j] = False
def findWords(boggle):
    visited = [[False for i in range(N)] for j in range(M)]
    Str = ""
    for i in range(M):
     for j in range(N):
        findWordsUtil(boggle, visited, i, j, Str)
boggle = [["M", "S", "E","F"], ["R", "A", "T", "D"], ["L", "O", "N", "E"],["K" , "A", "F", "B"]]

print("Following words of", "dictionary are present")
findWords(boggle)


# In[ ]:




