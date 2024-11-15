# Ecosystem

You'll be making a program to simulate an ecosystem containing two types of creatures, **sharks** and **fish**. The ecosystem consists of a river, which is modelled as a relatively large list. Each element of the list should be a ***Fish object***, a ***Shark object***, or *None*. 

In each generation, based on a random process, each creature either attempts to move into an adjacent list location or stay where it is. 

## Rules for moving

- If the new position is empty (*has None*), the creature should now occupy the new position.
- If the new position has a creature of the same specie (type) and same sexes, the creature with more strength should occupy the new position, and the weaker one should die.
- If the new position has a creature of the same specie (type) but different sexes, a new born baby should be made and occupy any empty space. 
- If the new position has a creature of a different specie, only the fish should die.

## Rules for making babies

- A baby can only be made if two creatures (same specie) of different sexes collide.
- The strength of the new born baby should be the average strength of both parents.
- The new born baby should take the sex of the stronger parent.

## Statistics

Create a way to record data of what happened in a previous generation. The output of these stats should look like this:

```
GENERATION 4

0 fish were killed by other fish.
2 fish were killed by sharks.
0 fish died of old age.

4 shark(s) were killed by other sharks.
27 shark(s) died of old age.

There were 1 newborn fish.
There were 4 newborn shark(s).

CURRENT POPULATION:
Female Fish: 6
Male Fish: 9
Total Fish: 15

Female Shark(s): 7
Male Shark(s): 7
Total Shark(s): 14
```

## Fish and Shark objects

The Fish and the Shark objects are already created for you. Take a peak inside `fish.py` and `shark.py` to see how they work. Feel free to change the code as you see fit (*just ensure tests don't break*).

Both objects have the `same` method that you can use to check if two creatures are of the same specie. You use `same` by passing in another creature as the argument and it returns `True` if they are of the same specie, otherwise `False`.

Example: 

```python
issame = creature1.same(creature2)
```

## Ecosystem and its methods

Ecosystem is expected to have the following methods and should function as mentioned below:

### create_life

The `create_life` method should be responsible for creating all life (fish and sharks). The number of fish and sharks created should be based on the values provided in the `__init__` method.

A new instance of `Ecosystem` will be created by passing in three arguments: `size`, `fish_no`, and `shark_no` (in that order). `size` should be used to determine the size of the river, and `fish_no` should be used to determine the number of fish created, and `shark_no` should determine the number of sharks created.

**Example:**
```python
ecosystem = Ecosystem(50, 20, 10)

# This should create an instance of ecosystem with a river of size 50
# The river should have 20 fish and 10 sharks
```

All life created should exist within a list named `river` and should occupy random empty spaces. All extra spaces should have a value of `None`.

New creature's sex and strength should be based on random values:

- `sex` can only be 0 or 1. 0 for female and 1 for male.
- `strength` can only be values between 0 and 100 inclusively.

### new_generation

When invoked, each life should attempt to move into an adjacent list location or stay where it is. This must be based on a random process. Ensure that each creature **doesn't move more than once in each generation**. 

In each generation, each creature's age must increment by 1. 

- Fish should only live for 14 generations then die.
- Sharks should only live for 10 generations then die.

### make_baby

The `make_baby` method should be responsible for creating new born babies. The method should take in two arguments (*two parents*). A new born baby should be created based on the rules for making babies mentioned above.

This method should create a baby and then return it.

### show_generational_stats

This method should **return** statistics of what happened in the previous generation.

## Running Tests

To test run `python3 .tests.py`.

NOTE: *These tests were not made using any libraries, but they were written from scratch*

---

Feel free to add other functionalities, methods and classes as you see fit.

Goodluck!
