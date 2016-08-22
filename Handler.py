from Card import Card

class Handler:

    card = None

    templates = {
        "witch_doctor": "Assets/basic_card_template.png",
    }

    stateMachine = [
        "start",
        "template",
        "title",
        "spellClass",
        "level",
        "target",
        "effectType",
        "actionCost",
        "spellDuration",
        "spellRange",
        "description",
        "area",
        "page",
        "materials",
        "spellType",
        "render",
        "save",
        "end",
    ]

    def run(self):
        self.executeState(0, 'prompt')

    def executeState(self, state, action):
        if (state >= len(self.stateMachine)):
            return self.error(state, action, "State # is OOB")
        elif (state < 0):
            return self.error(state, action, "State # is OOB")

        if ('back' == action):
            newState = int(state) - 1

            if (newState <= 0):
                return self.error(state, action)
            else:
                return self.executeState(newState, 'run')
        elif ('next' == action):
            newState = int(state) + 1

            if (newState >= len(self.stateMachine)):
                return self.error(state, action)
            else:
                return self.executeState(newState, 'run')
        elif ('run' == action):
            option = self.promptOptions(state)
            return self.executeState(state, option)
        elif ('prompt' == action):
            getattr(self, self.stateMachine[state])()

            newState = int(state) + 1

            return self.executeState(newState, 'run')



    def error(self, state, action, message=None):
        print('State [' + str(state) + '] failed for Action [' + str(action) + ']')

        if (None != message):
            print(str(message))

    def start(self):
        if (None == self.card):
            self.card = Card()

        print("Welcome to the Spell Card generator\n\n")

    def template(self):
        print("\n\nAvailable templates:")

        count = 0
        for (templateName, filePath) in self.templates.items():
            print(str(count) + ": " + templateName)
            count += 1

        template = raw_input('Which template? ')
        self.card.setTemplate(self.templates[template])

    def title(self):
        title = raw_input("\n\nWhat is the title? ")
        self.card.setTitle(title)

    def spellClass(self):
        print("\n\nPossible spell classes include (Warlock, Sorcerer, Barbarian)")
        spellClass = raw_input("What is the spell class? ")
        self.card.setSpellClass(spellClass)

    def level(self):
        level = raw_input("\n\nWhat level? ")
        self.card.setLevel(level)

    def target(self):
        print("\n\nPossible targets include (Self, One Living Creature, See Description)")
        target = raw_input("What is the target? ")
        self.card.setTarget(target)

    def effectType(self):
        print("\n\nPossible effect types include (Ray, Burst of Light, One Missile of Acid)")
        effectType = raw_input("What is the effect type? ")
        self.card.setEffectType(effectType)

    def actionCost(self):
        print("\n\nPossible action costs include (1 Standard Action, 1 Round)")
        actionCost = raw_input("What is the action cost? ")
        self.card.setActionCost(actionCost)

    def spellDuration(self):
        print("\n\nPossible spell durations include (Instantaneous, Permanent, 1 Min)")
        spellDuration = raw_input("What is the spell duration? ")
        self.card.setSpellDuration(spellDuration)

    def spellRange(self):
        print("\n\nPossible spell ranges include (10 ft., 100 ft. + 10 ft./2 levels) ")
        spellRange = raw_input("What is the spell range? ")
        self.card.setSpellRange(spellRange)

    def description(self):
        description = raw_input("\n\nWhat is the description? ")
        self.card.setDescription(description)

    def area(self):
        print("\n\nPossible area of effects include (60 ft. cone, 20 ft. radius)")
        area = raw_input("What is the area of effect? ")
        self.card.setArea(area)

    def page(self):
        page = raw_input("What page of the core rulebook is the spell from? ")
        self.card.setPage(page)

    def materials(self):
        materials = []

        print("\n\nPossible materials include (Lizard, Silver, Dung)")
        print("Enter 0 to exit")

        while True:
            material = raw_input("What is a required material? ")

            if ("0" == material):
                break

            materials.append(material)

        self.card.setMaterials(materials)

    def spellType(self):
        spellTypes = []

        print("\n\nPossible spell types include (Verbal, Somatic, Touch, Focus)")
        print("Enter 0 to exit")

        while True:
            spellType = raw_input("What type of spell is this? ")

            if ("0" == spellType):
                break

            spellTypes.append(spellType)

        self.card.setSpellType(spellTypes)

    def render(self):
        print("\n\nRendering the spell card")

        self.card.renderCard()
        self.card.showRenderedCard()

    def save(self):
        print("\n\nSaving the spell card")

        self.card.saveCard()

    def end(self):
        print("\n\nEnding the program")
        exit()

    def promptOptions(self, state):
        print("\n\nYou are currently on state [" + self.stateMachine[state] + "]")
        print("Possible options are: back, next, prompt")

        return raw_input("What would you like to do? ")

handler = Handler()
handler.run()