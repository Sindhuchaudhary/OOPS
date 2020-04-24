

class Animal:
    sound = ''
    Breathe = ''
    increase_in_food = 0
    
    def __init__(self, age_in_months=None, breed=None, required_food_in_kgs=None):
        if age_in_months > 9:
            raise ValueError(f'Invalid value for field age_in_months: {age_in_months}')
        if required_food_in_kgs <= 0:
            raise ValueError(f'Invalid value for field required_food_in_kgs: {required_food_in_kgs}')
        
        self._age_in_months = age_in_months
        self._required_food_in_kgs = required_food_in_kgs
        self._breed = breed
        self.animal_count = 0
        
    @property
    def age_in_months(self):
        return self._age_in_months
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    @property
    def breed(self):
        return self._breed
    
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    @classmethod
    def breathe(cls):
        print(cls.Breathe)
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += type(self).increase_in_food
        
    def hunt(self,zoo):
        if type(self).__name__ in ('Lion', 'Snake'):
            if zoo.animals_in_zoo.count('Deer') > 0:
                zoo.animals_in_zoo.remove('Deer')
            else:
                print('No deers to hunt')
        
        elif type(self).__name__ == 'Shark':
            if zoo.animals_in_zoo.count('GoldFish') > 0:
                zoo.animals_in_zoo.remove('GoldFish')
            else:
                print('No GoldFish to hunt')

class Deer(Animal):
    sound = 'Buck Buck'
    Breathe = 'Breathe in air'
    increase_in_food = 2
    
class Lion(Animal):
    sound = 'Roar Roar'
    Breathe = 'Breathe in air'
    increase_in_food = 4
    
class Shark(Animal):
    sound = 'Shark Sound'
    Breathe = 'Breathe oxygen from water'
    increase_in_food = 8
    
class GoldFish(Animal):
    sound = 'Hum Hum'
    Breathe = 'Breathe oxygen from water'
    increase_in_food = 0.2
    
    
class Snake(Animal):
    sound = 'Hiss Hiss'
    Breathe = 'Breathe in air'
    increase_in_food = 0.5
    
class Zoo(Animal):
    
    all_zoos = []
    
    def __init__(self):
        self._reserved_food_in_kgs =0
        self.animals_in_zoo = []
        type(self).all_zoos.append(self)
    
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    def add_food_to_reserve(self,add_food_to_reserve):
        self._reserved_food_in_kgs += add_food_to_reserve
    
    def count_animals(self):
        return len(self.animals_in_zoo)
    
    def add_animal(self,animal):
        self.animals_in_zoo.append(type(animal).__name__)
        
        
    def feed(self,animal_name):
        
        if self._reserved_food_in_kgs >= animal_name._required_food_in_kgs:
            self._reserved_food_in_kgs -= animal_name._required_food_in_kgs
            animal_name.grow()
    
    @classmethod
    def count_animals_in_all_zoos(cls):
        total_no_of_animals_in_all_zoos = 0
        for zoo in cls.all_zoos:
            total_no_of_animals_in_all_zoos += zoo.count_animals()
        return total_no_of_animals_in_all_zoos
    
    @staticmethod
    def count_animals_in_given_zoos(zoos):
        total_no_of_animals_in_all_zoos = 0
        for zoo in zoos:
            total_no_of_animals_in_all_zoos += zoo.count_animals()
        return total_no_of_animals_in_all_zoos
