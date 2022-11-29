class TensorflowPlayground:
  def __init__(self):
    self.layer = [torch.tensor([1])] * 6
    self.testLoss = 5000

  def reset(self, layer): #추후 그리드, 랜덤, (베이지안) 중 결정
    pass 
    return self.layer

  def step(self, action):
    for i in range(6):
      if action[i].tolist()[0][0] == 0:
        self.layer[i] -= 1
      elif action[i].tolist()[0][0] == 2:
        self.layer[i] += 1
    self.testLoss = self.getTestLoss()
    return self.layer, 5000/self.testLoss

  def getTestLoss(self):
    pass #준
    return #준
