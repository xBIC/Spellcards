from PIL import Image
import yaml

class SpellCard:
    image = None

    template = None

    """Name of the spell"""
    title = None

    """What class this spell is for"""
    spell_class = None

    """What spell level this is for"""
    level = None

    """Who is targeted by this"""
    target = None

    """What type of spell this is (Ray, Burst of Light, One Missile of Acid)"""
    effect_type = None

    """How long it takes to generate the spell (ie. 1 Standard Action, 1 Round)"""
    action_cost = None

    """How long is the effect for (ie. Instantaneous, Permanent, 1 Min)"""
    spell_duration = None

    """What is the range of the spell"""
    spell_range = None

    """Description of the spell"""
    description = None

    """What area of effect this spell has"""
    area = None

    """Image path for the area of effect graphic"""
    area_image = None

    """What page of the core rulebook the spell is from"""
    page = None

    """What materials are needed to cast this"""
    materials = None

    """How is this spell cast (ie. Verbal, Somatic, Touch, Focus)"""
    spell_type = None

    def __init__(self, data=None):
        if (None != data):
            self.setSpellCardFromData(data)

    def setTemplate(self, template):
        self.template = template

    def getTemplate(self):
        return self.template

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setSpellClass(self, spellClass):
        self.spell_class = spellClass

    def getSpellClass(self):
        return self.spell_class

    def setLevel(self, level):
        self.level = level

    def getLevel(self):
        return self.level

    def setTarget(self, target):
        self.target = target

    def getTarget(self):
        return self.target

    def setEffectType(self, effectType):
        self.effect_type = effectType

    def getEffectType(self):
        return self.effect_type

    def setActionCost(self, actionCost):
        self.action_cost = actionCost

    def getActionCost(self):
        return self.action_cost

    def setSpellDuration(self, spellDuration):
        self.spell_duration = spellDuration

    def getSpellDuration(self):
        return self.spell_duration

    def setSpellRange(self, spellRange):
        self.spell_range = spellRange

    def getSpellRange(self):
        return self.spell_range

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def setArea(self, area):
        self.area = area

    def getArea(self):
        return self.area

    def setPage(self, page):
        self.page = page

    def getPage(self):
        return self.page

    def setMaterials(self, materials):
        self.materials = materials

    def getMaterials(self):
        return self.materials

    def setSpellType(self, spellType):
        self.spell_type = spellType

    def getSpellType(self):
        return self.spell_type

    def setImage(self, image):
        self.image = image

    def getImage(self):
        return self.image

    def setAreaImage(self, area_image):
        self.area_image = area_image

    def getAreaImage(self):
        return self.area_image

    def renderCard(self):
        """Render the card here"""
        pass

    def saveCardToFile(self):
        cardDict = self.convertCardToDictionary()
        title = self.getTitle()
        title = title.replace(' ', '_')
        with open('Card_Files/' + title + '.yaml', 'w') as outfile:
            yaml.dump(cardDict, outfile, default_flow_style=False)

    def saveCardImage(self):
        pass

    def showCard(self):
        image = self.getImage()
        if (None != image):
            image.show()

    def setSpellCardFromData(self, data):
        if ('template' in data):
            self.setTemplate(data['template'])
        if ('title' in data):
            self.setTitle(data['title'])
        if ('spell_class' in data):
            self.setSpellClass(data['spell_class'])
        if ('level' in data):
            self.setLevel(data['level'])
        if ('target' in data):
            self.setTarget(data['target'])
        if ('effect_type' in data):
            self.setEffectType(data['effect_type'])
        if ('action_cost' in data):
            self.setActionCost(data['action_cost'])
        if ('spell_duration' in data):
            self.setSpellDuration(data['spell_duration'])
        if ('spell_range' in data):
            self.setSpellRange(data['spell_range'])
        if ('description' in data):
            self.setDescription(data['description'])
        if ('area' in data):
            self.setArea(data['area'])
        if ('area_image' in data):
            self.setAreaImage(data['area_image'])
        if ('page' in data):
            self.setPage(data['page'])
        if ('materials' in data):
            self.setMaterials(data['materials'])
        if ('spell_type' in data):
            self.setSpellType(data['spell_type'])

    def convertCardToDictionary(self):
        card = {
            'template' : self.getTemplate(),
            'title' : self.getTitle(),
            'spell_class' : self.getSpellClass(),
            'level' : self.getLevel(),
            'target' : self.getTarget(),
            'effect_type' : self.getEffectType(),
            'action_cost' : self.getActionCost(),
            'spell_duration' : self.getSpellDuration(),
            'spell_range' : self.getSpellRange(),
            'description' : self.getDescription(),
            'area' : self.getArea(),
            'area_image' : self.getAreaImage(),
            'page' : self.getPage(),
            'materials' : self.getMaterials(),
            'spell_type' : self.getSpellType(),
        }

        return card