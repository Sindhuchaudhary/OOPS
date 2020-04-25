class Pokemon:
	attack_value = 0
	sound = ''
	def __init__(self,name="",level = 1):
		if name == '':
			raise ValueError('name cannot be empty')
		if level <= 0:
			raise ValueError('level should be > 0')
		self._name = name
		self._level = level
	
	@property	
	def name(self):
		return self._name
	
	@property	
	def level(self):
		return self._level
		
	def run(self):
		print('{} running...'.format(type(self).__name__))
		
	def swim(self):
		print('{} swimming...'.format(type(self).__name__))
		
	def fly(self):
		print('{} flying...'.format(type(self).__name__))
		
	
	
	@classmethod
	def make_sound(cls):
		print(cls.sound)
		
	def __str__(self):
		return '{} - Level {}'.format(self.name,self.level)
		
class Pikachu(Pokemon):
	sound = 'Pika Pika'
	attack_value = 10
	
	
	def attack(self):
		print('Electric attack with {} damage'.format(self.attack_value*self.level))
	

class Squirtle(Pokemon):
	sound = 'Squirtle...Squirtle'
	attack_value = 9
	
	def attack(self):
		print('Water attack with {} damage'.format(self.attack_value*self.level))
	
class Pidgey(Pokemon):
	sound = 'Pidgey...Pidgey'
	attack_value = 5
	
	
	def attack(self):
		print('Air attack with {} damage'.format(self.attack_value*self.level))
	
	

class Swanna(Pokemon):
	sound = 'Swanna...Swanna'
	water_attack_value = 9
	air_attack_value = 5
	
	
	def attack(self):
		print('Water attack with {} damage'.format(self.water_attack_value*self.level))
		print('Air attack with {} damage'.format(self.air_attack_value*self.level))
		
class Zapdos(Pokemon):
	sound = 'Zap...Zap'
	electric_attack_value = 10
	air_attack_value = 5
	
	
	def attack(self):
		print('Electric attack with {} damage'.format(self.electric_attack_value*self.level))
		print('Air attack with {} damage'.format(self.air_attack_value*self.level))
	
	
class Island:
	all_islands = []
	
	def __init__(self,name, max_no_of_pokemon=0, total_food_available_in_kgs=0):
		self._name = name
		self._max_no_of_pokemon = max_no_of_pokemon
		self._total_food_available_in_kgs = total_food_available_in_kgs
		self._pokemon_left_to_catch = 0
		self.add_pokemons = []
		Island.all_islands.append('{} - {} pokemon - {} food'.format(self.name,self._pokemon_left_to_catch,self._total_food_available_in_kgs))
		
	
	@property	
	def name(self):
		return self._name
	
	@property	
	def max_no_of_pokemon(self):
		return self._max_no_of_pokemon
	
	@property	
	def total_food_available_in_kgs(self):
		return self._total_food_available_in_kgs
	
	@property	
	def pokemon_left_to_catch(self):
		return self._pokemon_left_to_catch
		
	def __str__(self):
		return '{} - {} pokemon - {} food'.format(self.name,self._pokemon_left_to_catch,self._total_food_available_in_kgs)
			
	def add_pokemon(self,pokemon):
		if self._pokemon_left_to_catch < self._max_no_of_pokemon:
			self.add_pokemons.append(type(self).__name__)
			self._pokemon_left_to_catch += 1
		else:
			print('Island at its max pokemon capacity')
	
	@classmethod		
	def get_all_islands(cls):
		print('\n'.join(map(str,cls.all_islands)))

class Trainer:
	caught_pokemons = []
	def __init__(self,name):
		self._name = name
		self._experience = 100
		self._max_food_in_bag = 10 * self.experience
		self._food_in_bag = 0
		self._current_island = ''
	
	@property
	def name(self):
		return self._name
	
	@property	
	def experience(self):
		return self._experience
	
	@property	
	def max_food_in_bag(self):
		self._max_food_in_bag
	
	@property	
	def food_in_bag(self):
		return self._food_in_bag
		
	@property 
	def current_island(self):
		return self._current_island
		
	def __str__(self):
		return '{}'.format(self.name)
		
	def move_to_island(self,island):
		
		if self._current_island not in Island.all_islands:
			print('You are not on any island')
			
		else:
			self._current_island = island
			if self._current_island == island:
				print('True')
				
	def collect_food(self):
		if self._current_island not in Island.all_islands:
			print('Move to an island to collect food')
		self._food_in_bag += self._experience	
			
	def catch(self,pokemon):
		if self._experience >= 100*pokemon.level:
			print('You caught {}'.format(pokemon.name))
			self._experience += pokemon.level*20
			Trainer.caught_pokemons.append('[{} - Level 1]'.format(pokemon.name))
		else:
			print('You need more experience to catch {}'.format(pokemon.name))
			
	@classmethod		
	def get_my_pokemon(cls):
		print('\n'.join(map(str,cls.caught_pokemons)))		
		
		
		
		
		
		
