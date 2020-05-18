class Pokemon:
	attack_value = 0
	sound = ''
	Run = ''
	Swim = ''
	Fly = ''
	def __init__(self,name="",level = 1):
		if name == '':
			raise ValueError('name cannot be empty')
		if level <= 0:
			raise ValueError('level should be > 0')
		self._name = name
		self._level = level
		self._master = None
	
	@property	
	def name(self):
		return self._name
	
	@property	
	def level(self):
		return self._level
	
	@classmethod
	def make_sound(cls):
		print(cls.sound)
	@property
	def master(self):
		if self._master == None:
			print('No Master')
		else:
			return self._master
			
	@classmethod
	def run(cls):
		print(cls.Run)	
		
	@classmethod	
	def swim(cls):
		print(cls.Swim)
		
	@classmethod
	def fly(cls):
		print(cls.Fly)
		
		
	def __str__(self):
		return '{} - Level {}'.format(self.name,self.level)
		
class Pikachu(Pokemon):
	sound = 'Pika Pika'
	Run = 'Pikachu running...'
	attack_value = 10

	def attack(self):
		print('Electric attack with {} damage'.format(self.attack_value*self.level))
	

class Squirtle(Pokemon):
	sound = 'Squirtle...Squirtle'
	attack_value = 9
	Run = 'Squirtle running...'
	Swim = 'Squirtle swimming...'
	
	def attack(self):
		print('Water attack with {} damage'.format(self.attack_value*self.level))
	
class Pidgey(Pokemon):
	sound = 'Pidgey...Pidgey'
	attack_value = 5
	Fly = 'Pidgey flying...'
	
	def attack(self):
		print('Air attack with {} damage'.format(self.attack_value*self.level))
	
class Swanna(Pokemon):
	sound = 'Swanna...Swanna'
	water_attack_value = 9
	air_attack_value = 5
	Fly = 'Swanna flying...'
	Swim = 'Swanna swimming...'
	
	def attack(self):
		print('Water attack with {} damage'.format(self.water_attack_value*self.level))
		print('Air attack with {} damage'.format(self.air_attack_value*self.level))
		
class Zapdos(Pokemon):
	sound = 'Zap...Zap'
	electric_attack_value = 10
	air_attack_value = 5
	
	@classmethod
	def fly(cls):
		print('Zapdos flying...')
		
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
		Island.all_islands.append(self)
		
	
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
			self.add_pokemons.append(self)
			self._pokemon_left_to_catch += 1
		else:
			print('Island at its max pokemon capacity')
	
	@classmethod		
	def get_all_islands(cls):
		return cls.all_islands
		

class Trainer:
	
	def __init__(self,name="none"):
		
		self._name = name
		self._experience = 100
		self._max_food_in_bag = 10 * self._experience
		self._food_in_bag = 0
		self._current_island = None
		self.pokemons_list = []
		
	@property
	def name(self):
		return self._name
	
	@property	
	def experience(self):
		return self._experience
	
	@property	
	def max_food_in_bag(self):
		return self._max_food_in_bag
	
	@property	
	def food_in_bag(self):
		return self._food_in_bag
		
	@property 
	def current_island(self):
		if self._current_island == None:   
			print('You are not on any island')
		else:
			return self._current_island
		

			
		
	def __str__(self):
		return '{}'.format(self._name)
		
	def move_to_island(self,island):
		
		self._current_island = island
				
	def collect_food(self):
		if self._current_island == None:
			print('Move to an island to collect food')
			
		elif self._current_island.total_food_available_in_kgs < self._max_food_in_bag:
			self._food_in_bag = self._current_island._total_food_available_in_kgs
			self._current_island._total_food_available_in_kgs = 0
		elif self._food_in_bag != self._max_food_in_bag:
			self._current_island._total_food_available_in_kgs -= self._max_food_in_bag
			self._food_in_bag = self._max_food_in_bag
	
	def catch(self,pokemon):
		if self._experience >= 100*pokemon.level:
			print('You caught {}'.format(pokemon.name))
			self._experience += pokemon.level*20
			self.pokemons_list.append(pokemon)
			pokemon._master = self
			
		else:
			print('You need more experience to catch {}'.format(pokemon.name))
		
	def get_my_pokemon(self):
		return self.pokemons_list
		

			

