from shark import Shark
from fish import Fish
from random import random
from math import floor

class Ecosystem:
  class GenerationalStats:
    generation = -1

    fish_died_fish = 0
    fish_died_shark = 0
    fish_died_age = 0
    fish_newborn = 0

    shark_died = 0
    shark_died_age = 0
    shark_newborn = 0

    @classmethod
    def update_death_stats(cls, died, killer):
      if isinstance(died, Fish) and isinstance(killer, Fish):
        cls.fish_died_fish += 1

      elif isinstance(died, Fish) and isinstance(killer, Shark):
        cls.fish_died_shark += 1

      elif isinstance(died, Fish):
        cls.fish_died_age += 1

      elif isinstance(killer, Shark):
        cls.shark_died += 1

      else:
        cls.shark_died_age += 1

    @classmethod
    def update_newborn_stats(cls, newborn):
      if isinstance(newborn, Fish):
        cls.fish_newborn += 1
      else:
        cls.shark_newborn += 1

    @classmethod
    def reset(cls):
      cls.generation += 1

      cls.fish_died_fish = 0
      cls.fish_died_shark = 0
      cls.fish_newborn = 0

      cls.shark_died = 0
      cls.shark_died_age = 0
      cls.shark_newborn = 0

    @classmethod
    def show(cls, river):
      return f'''\
        GENERATION {cls.generation}

        {cls.fish_died_fish} fish were killed by other fish.
        {cls.fish_died_shark} fish were killed by sharks.
        {cls.fish_died_age} fish died of old age.
        
        {cls.shark_died} shark(s) were killed by other sharks.
        {cls.shark_died_age} shark(s) died of old age.

        There were {cls.fish_newborn} newborn fish.
        There were {cls.shark_newborn} newborn shark(s).

        CURRENT POPULATION:
        Female Fish: {len([c for c in river if isinstance(c, Fish) and not c.sex])}
        Male Fish: {len([c for c in river if isinstance(c, Fish) and c.sex])}
        Total: {len([c for c in river if isinstance(c, Fish)])}

        Female Shark(s): {len([c for c in river if isinstance(c, Shark) and not c.sex])}
        Male Shark(s): {len([c for c in river if isinstance(c, Shark) and c.sex])}
        Total: {len([c for c in river if isinstance(c, Shark)])}
      '''

  def __init__(self, size, fish_no, shark_no):
    self.size = size
    self.fish_no = fish_no
    self.shark_no = shark_no
    self.river = [None] * size

  def __len__(self):
    return len(self.river)

  def __getitem__(self, index):
    return self.river[index]

  def __setitem__(self, index, value):
    self.river[index] = value

  def __contains__(self, value):
    return value in self.river

  def __str__(self):
    return str(self.river)

  def __repr__(self):
    return str(self)

  def _next_move(self, index):
    if index == 0:
      move = floor(random() * 2) + 1
    elif index == len(self) - 1:
      move = floor(random() * 2)
    else:
      move = floor(random() * 3)

    if move == 0: return index - 1
    elif move == 2: return index + 1
    else: return None

  def make_baby(self, creature1, creature2):
    strength = (creature1.strength + creature2.strength) // 2
    if creature1.strength >= creature2.strength:
      sex = creature1.sex
    else:
      sex = creature2.sex
    return creature1.__class__(sex, strength)

  def create_life(self):
    if self.fish_no + self.shark_no > self.size:
      raise ValueError('The number of sharks and fish cannot be bigger than the size of the ecosystem')

    def main(specie, n):
      for _ in range(n):
        sex = floor(random() * 2)
        strength = floor(random() * 101)
        s = specie(sex, strength)

        while True:
          pos = floor(random() * self.size)
          if not self.river[pos]: break

        self.river[pos] = s

    main(Fish, self.fish_no)
    main(Shark, self.shark_no)

  def new_generation(self):
    self.GenerationalStats.reset()

    creatures = [(i, c) for i, c in enumerate(self) if c]

    for i, creature in creatures:
      if isinstance(creature, Shark) and creature.age >= 4:
        self.GenerationalStats.update_death_stats(creature, None)
        self[i] = None
        continue
      elif isinstance(creature, Fish) and creature.age >= 9:
        self.GenerationalStats.update_death_stats(creature, None)
        self[i] = None
        continue

      creature.age += 1

      pos = self._next_move(i)
      if not pos: continue

      other = self[pos]
      if not other:
        self[pos] = creature
        self[i] = None
        continue

      if creature.same(other) and creature.sex == other.sex:
        if creature.strength > other.strength:
          self.GenerationalStats.update_death_stats(other, creature)
          self[pos] = creature
          self[i] = None

        elif creature.strength < other.strength:
          self.GenerationalStats.update_death_stats(creature, other)
          self[pos] = None

        else:
          self.GenerationalStats.update_death_stats(creature, other)
          self.GenerationalStats.update_death_stats(other, creature)
          self[pos] = None
          self[i] = None

      elif creature.same(other):
        try:
          baby = self.make_baby(creature, other)
          index = self.river.index(None)
          self.river[index] = baby
          self.GenerationalStats.update_newborn_stats(baby)
        except ValueError:
          pass

      else:
        if isinstance(creature, Shark):
          self.GenerationalStats.update_death_stats(other, creature)
          self[pos] = creature
          self[i] = None
        else:
          self.GenerationalStats.update_death_stats(creature, other)
          self[i] = None

  def show_generational_stats(self):
    return self.GenerationalStats.show(self)
