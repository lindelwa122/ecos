import os
import importlib

from random import random
from math import floor

# DON'T BE TEMPTED TO CHANGE ANYTHING HERE :)

def output_error_msg(msg):
  print(f'\033[31m\u00D7 {msg}\033[0m')
  exit(1)

def output_success_msg(msg):
  print(f'\033[32m\u2713 {msg}\033[0m')

# Test if the 'fish.py' file exists
if os.path.isfile('fish.py'):
  output_success_msg('fish.py exists')
else:
  output_error_msg('fish.py doesn\'t exist')

# Test if 'fish.py' has a Fish object
fish_module = importlib.import_module('fish')
if hasattr(fish_module, 'Fish'):
  output_success_msg('Fish object exists')
else:
  output_error_msg('Fish object doesn\'t exist')

Fish = fish_module.Fish

# Test if fish has all the expected attributes
try:
  for name in ['age', 'sex', 'strength']:
    if not hasattr(Fish(0, 0), name):
      output_error_msg('Fish is missing expected attributes. It must have sex, age, and strength as attributes')
except TypeError:
  output_error_msg('Fish must take in two arguments')

output_success_msg('Fish has all the expected attributes')

# Test if sex is handled accurately by the Fish object
fish = Fish(0, 0)
try:
  fish.sex = 0
  fish.sex = 1
except Exception:
  output_error_msg('Fish doesn\'t handle the sex attribute accurately. Remember sex can only be 0 or 1')

try:
  fish.sex = 5
  output_error_msg('Fish doesn\'t handle the sex attribute accurately. Remember sex can only be 0 or 1')

except Exception: 
  pass

try:
  fish.sex = -1
  output_error_msg('Fish doesn\'t handle the sex attribute accurately. Remember sex can only be 0 or 1')
except Exception: 
  pass

try: 
  fish.sex = 'female'
  output_error_msg('Fish doesn\'t handle the sex attribute accurately. Remember sex can only be 0 or 1')
except Exception:
  pass

# Test if strength is handled accurately by the Fish object
strengths = []
while len(strengths) != 10:
  strengths.append(floor(random() * 101))

try:
  for stngth in strengths:
    fish.strength = stngth
except Exception:
  output_error_msg('Fish doesn\'t handle the strength attribute accurately. Remember strength can only be between 0 and 100 inclusively')

try:
  fish.strength = 101
  output_error_msg('Fish doesn\'t handle the strength attribute accurately. Remember strength can only be between 0 and 100 inclusively')
except Exception:
  pass

try:
  fish.strength = -1
  output_error_msg('Fish doesn\'t handle the strength attribute accurately. Remember strength can only be between 0 and 100 inclusively')
except Exception:
  pass

try:
  fish.strength = 'strong'
except Exception:
  pass

try:
  age = [*range(1, 13)]
  for a in age: fish.age = a
except Exception:
  output_error_msg('Fish doesn\'t handle the age attribute accurately. Remember age can only be between 0 and 13 inclusively')

try:
  fish.age = 14
  output_error_msg('Fish doesn\'t handle the age attribute accurately. Remember age can only be between 0 and 13 inclusively')
except Exception:
  pass

output_success_msg('Fish handles sex, age, and strength attributes correctly')

# Test if the 'shark.py' file exists
if os.path.isfile('shark.py'):
  output_success_msg('shark.py exists')
else:
  output_error_msg('shark.py doesn\'t exist')

# Test if 'shark.py' has a Shark object
shark_module = importlib.import_module('shark')
if hasattr(shark_module, 'Shark'):
  output_success_msg('Shark object exists')
else:
  output_error_msg('Shark object doesn\'t exist')

Shark = shark_module.Shark

# Test if shark has all the expected attributes
try:
  for name in ['age', 'sex', 'strength']:
    if not hasattr(Shark(0, 0), name):
      output_error_msg('Shark is missing expected attributes. It must have sex, age, and strength as attributes')
except TypeError:
  output_error_msg('Shark must take in two arguments')

output_success_msg('Shark has all the expected attributes')

# Test if sex is handled accurately by the Shark object
shark = Shark(0, 0)
try:
  shark.sex = 0
  shark.sex = 1
except Exception:
  output_error_msg('Shark doesn\'t handle the sex attribute accurately. Remember sex can only be 0 or 1')

try:
  shark.sex = 5
  output_error_msg('Shark doesn\'t handle the sex attribute accurately. Remember sex can only be 0 or 1')

except Exception: 
  pass

try:
  shark.sex = -1
  output_error_msg('Shark doesn\'t handle the sex attribute accurately. Remember sex can only be 0 or 1')
except Exception: 
  pass

try: 
  shark.sex = 'female'
  output_error_msg('Shark doesn\'t handle the sex attribute accurately. Remember sex can only be 0 or 1')
except Exception:
  pass

# Test if strength is handled accurately by the Shark object
strengths = []
while len(strengths) != 10:
  strengths.append(floor(random() * 101))

try:
  for stngth in strengths:
    shark.strength = stngth
except Exception:
  output_error_msg('Shark doesn\'t handle the strength attribute accurately. Remember strength can only be between 0 and 100 inclusively')

try:
  shark.strength = 101
  output_error_msg('Shark doesn\'t handle the strength attribute accurately. Remember strength can only be between 0 and 100 inclusively')
except Exception:
  pass

try:
  shark.strength = -1
  output_error_msg('Shark doesn\'t handle the strength attribute accurately. Remember strength can only be between 0 and 100 inclusively')
except Exception:
  pass

try:
  shark.strength = 'strong'
except Exception:
  pass

try:
  age = [*range(1, 9)]
  for a in age: shark.age = a
except Exception:
  output_error_msg('Shark doesn\'t handle the age attribute accurately. Remember age can only be between 0 and 9 inclusively')

try:
  shark.age = 10
  output_error_msg('Shark doesn\'t handle the age attribute accurately. Remember age can only be between 0 and 9 inclusively')
except Exception:
  pass

output_success_msg('Shark handles sex, age, and strength attributes correctly')

# Test if 'ecosystem.py' exists
if os.path.isfile('ecosystem.py'):
  output_success_msg('ecosystem.py exists')
else:
  output_error_msg('ecosystem.py doesn\'t exist')

ecosystem_module = importlib.import_module('ecosystem')

# Test if the Ecosystem object exists
if hasattr(ecosystem_module, 'Ecosystem'):
  output_success_msg('Ecosystem object exists')
else:
  output_error_msg('Ecosystem object doesn\'t exist')

Ecosystem = ecosystem_module.Ecosystem

try:
  ecosystem = Ecosystem(50, 20, 10)
except Exception:
  output_error_msg('Ecosystem must take in 3 attributes (size, fish_no, shark_no)')

# Test if the 'create_life' method exists
if hasattr(ecosystem, 'create_life'):
  output_success_msg('the method create_life exists')
else:
  output_error_msg('the method create_life doesn\'t exist')

# Test if river exists
if hasattr(ecosystem, 'river'):
  output_success_msg('river exists')
else:
  output_error_msg('river doesn\'t exist')

# Test if river's capacity is equal to the size specified
river_sizes = []
while len(river_sizes) != 10:
  river_sizes.append(floor(random() * 100) + 10)

for size in river_sizes:
  ecos = Ecosystem(size, int(size * (40/100)), int(size * (20/100)))
  if len(ecos.river) != size:
    output_error_msg(f'''
      the length of river should always be the same as the specified size
      specified size: {size}
      the length of river: {len(ecos.river)}
    ''')
  
output_success_msg('the length of the river is the same as the size specified')

# Test if create_life creates the specified number of Fish objects
fish_nos = []
while len(fish_nos) != 10:
  fish_nos.append(floor(random() * 100) + 1)

for no in fish_nos:
  ecos = Ecosystem(int(no * (160/100)), no, int(no * (50/100)))
  ecos.create_life()
  
  fish_life = 0
  for item in ecos.river:
    if isinstance(item, Fish): fish_life += 1

  if fish_life != no:
    output_error_msg(f'''
      the number of fish in the river should equal to the specified fish_no at instance creation
      specified fish number: {no}
      the number of fish in the river: {fish_life}
    ''')

output_success_msg('the number of fish in the river matches the specified number')

# Test if create_life creates the specified number of Shark objects
shark_nos = []
while len(shark_nos) != 10:
  shark_nos.append(floor(random() * 100) + 1)

for no in shark_nos:
  ecos = Ecosystem(int(no * (250/100)), no // 2, no)
  ecos.create_life()

  shark_life = 0
  for item in ecos.river:
    if isinstance(item, Shark): shark_life += 1

  if shark_life != no:
    output_error_msg(f'''
      the number of sharks in the river should equal to the specified shark_no at instance creation
      specified shark number: {no}
      the number of sharks in the river: {shark_life}
    ''')

output_success_msg('the number of sharks in the river matches the specified number')
  
# Test if all objects in river are either Fish, Shark, or None
ecos = Ecosystem(100, 40, 40)
for item in ecos.river:
  if not (isinstance(item, (Fish, Shark)) or item is None):
    output_error_msg(f'all objects in the river must either be a Fish, Shark, or NoneType, {type(item)} found')

# Test if life is distributed randomly
if ecos.river[:40].count(None) < 3:
  output_error_msg('life when created should be placed in random empty positions.')
  
output_success_msg('create_life creates life correctly')

if not hasattr(ecos, 'make_baby'):
  output_error_msg('the ecosystem has no make_baby method')
else:
  output_success_msg('the ecosystem has make_baby method')

# Test if make_baby works as expected
for _ in range(10):
  fish1_sex, fish2_sex = floor(random() * 2), floor(random() * 2)
  fish1_str, fish2_str = floor(random() * 101), floor(random() * 101)

  fish1 = Fish(fish1_sex, fish1_str)
  fish2 = Fish(fish2_sex, fish2_str)
  baby = ecos.make_baby(fish1, fish2)

  if fish1_str >= fish2_str:
    if baby.sex != fish1_sex:
      output_error_msg('the baby should inherit the sex of the stronger parent')

    if baby.strength != (fish1_str + fish2_str) // 2:
      output_error_msg('the baby\'s strength should be the average strength of both parents')

# Test if make_baby works as expected
for _ in range(10):
  shark1_sex, shark2_sex = floor(random() * 2), floor(random() * 2)
  shark1_str, shark2_str = floor(random() * 101), floor(random() * 101)

  shark1 = Shark(shark1_sex, shark1_str)
  shark2 = Shark(shark2_sex, shark2_str)
  baby = ecos.make_baby(shark1, shark2)
  
  if shark1_str >= shark2_str:
    if baby.sex != shark1_sex:
      output_error_msg('the baby should inherit the sex of the stronger parent')

    if baby.strength != (shark1_str + shark2_str) // 2:
      output_error_msg('the baby\'s strength should be the average strength of both parents')

output_success_msg('the babies are created correctly')

if not hasattr(ecos, 'new_generation'):
  output_error_msg('ecosystem has no new_generation method')
else:
  output_success_msg('ecosystem has a new_generation method')

# Test if each life increase per generation
ecosystem = Ecosystem(100, 40, 30)
for i in range(5):
  creatures = [item for item in ecosystem.river if isinstance(item, (Fish, Shark))]
  for creature in creatures:
    if creature.age > i:
      output_error_msg(f'age is handled incorrectly, it\'s generation {i} and there\'s a creature that has an age of {creature.age}')

    if len([c for c in creatures if c.age == i]) == 0:
      output_error_msg(f'something may be wrong, it\'s generation {i} and no creature has and age of {i}')

    ecosystem.new_generation()

output_success_msg('age increase correctly in each generation')

# Test if fish live their expected lifespan
ecosystem = Ecosystem(100, 80, 10)

for i in range(14):
  ecosystem.new_generation()

fish = [item for item in ecosystem.river if isinstance(item, Fish)]
for f in fish:
  if f.age >= 14:
    output_error_msg('there\'s a fish that lived longer than it was supposed to live')

# Test if sharks live their expected lifespan
ecosystem = Ecosystem(100, 80, 10)

for i in range(10):
  sharks = [item for item in ecosystem.river if isinstance(item, Shark)]
  for shark in sharks:
    if shark.age >= 10:
      output_error_msg('there\'s a shark that lived longer than it was supposed to live')

output_success_msg('both fish and sharks live their expected lifespans')

ecosystem = Ecosystem(100, 40, 20)
index = ecosystem.river.index(None)
fish = Fish(0, 85)
ecosystem.river[index] = fish
for _ in range(10):
  ecosystem.new_generation()
  
if ecosystem.river[index] == fish:
  output_error_msg('''
    one fish hasn\'t moved in 10 generations, this is highly unlikely.
    double check your code or rerun the tests.
  ''')
    
output_success_msg('the new_generation method works correctly')

ecosystem = Ecosystem(500, 250, 150)
for _ in range(5): ecosystem.new_generation()

num_of_newborn_fish = len([item for item in ecosystem.river if isinstance(item, Fish) and item.age == 0])

if not hasattr(ecos, 'show_generational_stats'):
  output_error_msg('ecosystem has no show_generational_stats')
else:
  output_success_msg('ecosystem has show_generational_stats')

stats = ecosystem.show_generational_stats()

if f'There were {num_of_newborn_fish} newborn fish.' not in stats:
  output_error_msg('stats incorrectly handles newborn fish')

num_of_newborn_sharks = len([item for item in ecosystem.river if isinstance(item, Shark) and item.age == 0])

stats = ecosystem.show_generational_stats()

if f'There were {num_of_newborn_sharks} newborn shark(s).' not in stats:
  output_error_msg('stats incorrectly handles newborn sharks')

female_fish = len([item for item in ecosystem.river if isinstance(item, Fish) and item.sex == 0])
male_fish = len([item for item in ecosystem.river if isinstance(item, Fish) and item.sex == 1])
female_sharks = len([item for item in ecosystem.river if isinstance(item, Fish) and item.sex == 0])
male_sharks = len([item for item in ecosystem.river if isinstance(item, Fish) and item.sex == 1])

if f'Female Fish: {female_fish}' not in stats:
  output_error_msg('stats incorrectly handles the stats of female fish')

if f'Male Fish: {male_fish}' not in stats:
  output_error_msg('stats incorrectly handles the stats of male fish')

if f'Total Fish: {male_fish + female_fish}' not in stats:
  output_error_msg('stats incorrectly handles the stats of fish')

if f'Female Shark(s): {female_sharks}' not in stats:
  output_error_msg('stats incorrectly handles the stats of female sharks')

if f'Male Shark(s): {male_sharks}' not in stats:
  output_error_msg('stats incorrectly handles the stats of male sharks')

if f'Total Shark(s): {male_sharks + female_sharks}' not in stats:
    output_error_msg('stats incorrectly handles the stats of sharks')

output_success_msg('stats work accurately')
output_success_msg('Congratulations 🎉, Tariro Mashanda. You did it :)')
