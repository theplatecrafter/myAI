import math as m
import random as r

class network():
  def __init__(self,NumberOfInput,NumberOfOutput,NumberOfNodes,NumberOfConnections,RestrictionType = "DEFAULT"):
    self.noi = NumberOfInput
    self.noo = NumberOfOutput
    self.non = NumberOfNodes
    self.noc = NumberOfConnections
    self.rType = RestrictionType