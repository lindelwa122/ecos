class Shark:
  def __init__(self, sex, strength):
    self.sex = sex
    self.strength = strength
    self.age = 0
    
  def __setattr__(self, name, value):
    if name == 'sex' and (not isinstance(value, int) or value < 0 or value > 1):
      raise ValueError(f'The attribute sex can only be 0 or 1, {value} received')
      
    if name == 'strength' and (not isinstance(value, int) or value < 0 or value > 100):
      raise ValueError(f'The attribute strength can only be between 0 and 100 inclusively, {value} received')
      
    if name == 'age' and (not isinstance(value, int) or value < 0 or value >= 9):
      raise ValueError(f'The attribute age can only be between 0 and 9 inclusively, {value} received')
      
    if not (name == 'sex' or name == 'strength' or name == 'age'):
      raise ValueError(f'Only sex, strength, and age are allowed to be set, attempted to set {name}')
      
    self.__dict__[name] = value
    
  def __str__(self):
    return f'{"Male" if self.sex else "Female"} Shark (str: {self.strength}, age: {self.age})'
    
  def __repr__(self):
    return str(self)
    
  def same(self, other):
    return isinstance(other, Shark)

