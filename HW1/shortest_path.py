"""
CS 5112 - Homework 1
Steffen Baumgarten (stb92)
Rory Connolly (rlc367)

Implementation of the shortest_path function which will determine the shortest
path between a source and target node and return the distance of the path 
along with a list of the nodes that are visited in between.

Args:
  graph:   Set of connected nodes to work on when searching for shortest path
  source:  Beginning node for path
  target:  Destination node for path
  
Returns:
  A tuple containing:
    - list of nodes visited along the path from source to target
    - distance covered along the path
"""
import Queue as Q

def shortest_path(graph, source, target):
  # `graph` is an object that provides a get_neighbors(node) method that returns
  # a list of (node, weight) edges. both of your graph implementations should be
  # valid inputs. you may assume that the input graph is connected, and that all
  # edges in the graph have positive edge weights.
  # 
  # `source` and `target` are both nodes in the input graph. you may assume that
  # at least one path exists from the source node to the target node.
  #
  # this method should return a tuple that looks like
  # ([`source`, ..., `target`], `length`), where the first element is a list of
  # nodes representing the shortest path from the source to the target (in
  # order) and the second element is the length of that path
  #
  # NOTE: Please see instructions.txt for additional information about the
  # return value of this method.
  
  # Unexplored will be a priority queue with 
  #  (distance, node, previousNode)
  unexplored = Q.PriorityQueue()
  discoveredDist = dict()
  discoveredMap = dict()
  shortestPath = []
  
  unexplored.put((0, source, None))
  
  # Check if source is equal to target, in which case return
  # immediately with ([source, source], 0)
  if source == target:
    return([source, source], 0)
  
  # Execute this loop while there are still unexplored nodes in the 
  # PriorityQueue and the target has not yet been discovered
  while not unexplored.empty() and target not in discoveredDist:
    temp = unexplored.get()
    # Set local variables for use within loop
    localNode = temp[1]
    localDistance = temp[0]
    localPrev = temp[2]
    # Add entries to discovered maps if node is not already discovered
    if localNode not in discoveredMap:
      discoveredDist[localNode] = localDistance
      discoveredMap[localNode] = localPrev
      # Add neighbors of localNode to the unexplored PriorityQueue
      for fringeElement in graph.get_neighbors(localNode):
        fringeNode = fringeElement[0]
        fringeDistance = fringeElement[1]
        unexplored.put((localDistance+fringeDistance, fringeNode, localNode))
          
  # Calculate shortestPath; work backwards from target to source node
  # inserting previous node from discoveredMap to index zero of the list
  # until we reach the source node (where previous == None)
  tempNode = target
  while tempNode is not None:
    shortestPath.insert(0, tempNode)
    tempNode = discoveredMap[tempNode]

  return(shortestPath, discoveredDist[target])