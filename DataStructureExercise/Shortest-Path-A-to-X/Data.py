from collections import deque
class HashTownData:
    def __init__(self,name):
        self.name = name
        self.connections = []
        self.connections_names = []
        
    def add_connection(self,node):
        self.connections.append(node)
        self.connections_names.append(node.name)
    
    def __str__(self):
        return f"{self.name} connects to: {self.connections_names}"
