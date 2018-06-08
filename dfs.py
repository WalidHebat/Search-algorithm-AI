
import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    print problem

    visited = dict()
    state = problem.getStartState()
    frontier = util.Stack()

    node = {}
    node["parent"] = None
    node["action"] = None
    node["state"] = state
    frontier.push(node)

    # DFS, non-recursive implementation
    # by non-recurisve, we need to use stack to record
    # which node  to visit when recall
    while not frontier.isEmpty():
        node = frontier.pop()
        state = node["state"]
        if visited.has_key(hash(state)):
            continue
        visited[hash(state)] = True

        if problem.isGoalState(state) == True:
            break

        for child in problem.getSuccessors(state):
            if not visited.has_key(hash(child[0])):
                sub_node = {}
                sub_node["parent"] = node
                sub_node["action"] = child[1]
                sub_node["state"] = child[0]
                frontier.push(sub_node)

    actions = []
    while node["action"] != None:
        actions.insert(0, node["action"])
        node = node["parent"]

    return actions







def depthFirstSearch_recursive(problem):
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  print problem

  visited = dict()
  state = problem.getStartState()
  action = []
  DFS(problem, state, action, visited)
  return action

def DFS(problem, state, action, visited):
  if problem.isGoalState(state):
    return True

  for child in problem.getSuccessors(state):
    state = child[0]
    if not visited.has_key(hash(state)):
      visited[hash(state)] = state
      action.append(child[1])
      if DFS(problem, state, action, visited) == True:
        return True
      action.pop()

  return False



