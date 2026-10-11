class Foodstuff:

    def _init__(id, descripton, serving_size, calories, protein, carbs, fiber, fat):
        self.id = id
        self.descripton = descripton
        self.serving_size = serving_size
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fiber = fiber
        self.fat = fat


    @property
    def descripton(self):
        return self._descripton

    @property
    def serving_size(self):
        return self._serving_size

    @property
    def calories(self):
        return self._calories

    @property
    def protein(self):
        return self._protein

    @property
    def carbs(self):
        return self._carbs

    @property
    def fiber(self):
        return self._fiber

    @property
    def fat(self):
        return self._fat
