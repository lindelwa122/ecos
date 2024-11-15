from ecosystem import Ecosystem

ecos = Ecosystem(100, 48, 48)
ecos.create_life()

for i in range(5):
  ecos.new_generation()

stats = ecos.show_generational_stats()
print(stats)
