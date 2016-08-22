from PIL import Image

class Card:

    renderedCard = None

    template = None

    """Name of the spell"""
    title = None

    """What class this spell is for"""
    spellClass = None

    """What spell level this is for"""
    level = None

    """Who is targeted by this"""
    target = None

    """What type of spell this is (Ray, Burst of Light, One Missile of Acid)"""
    effectType = None

    """How long it takes to generate the spell (ie. 1 Standard Action, 1 Round)"""
    actionCost = None

    """How long is the effect for (ie. Instantaneous, Permanent, 1 Min)"""
    spellDuration = None

    """What is the range of the spell"""
    spellRange = None

    """Description of the spell"""
    description = None

    """What area of effect this spell has"""
    area = None

    """What page of the core rulebook the spell is from"""
    page = None

    """What materials are needed to cast this"""
    materials = None

    """How is this spell cast (ie. Verbal, Somatic, Touch, Focus)"""
    spellType = None


    def __init__(self):
        pass

    def setTemplate(self, template):
        self.template = template

    def getTemplate(self):
        return self.template

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setSpellClass(self, spellClass):
        self.spellClass = spellClass

    def getSpellClass(self):
        return self.spellClass

    def setLevel(self, level):
        self.level = level

    def getLevel(self):
        return self.level

    def setTarget(self, target):
        self.target = target

    def getTarget(self):
        return self.target

    def setEffectType(self, effectType):
        self.effectType = effectType

    def getEffectType(self):
        return self.effectType

    def setActionCost(self, actionCost):
        self.actionCost = actionCost

    def getActionCost(self):
        return self.actionCost

    def setSpellDuration(self, spellDuration):
        self.spellDuration = spellDuration

    def getSpellDuration(self):
        return self.spellDuration

    def setSpellRange(self, spellRange):
        self.spellRange = spellRange

    def getSpellRange(self):
        return self.spellRange

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
        self.spellType = spellType

    def getSpellType(self):
        return self.spellType

    def setRenderedCard(self, renderedCard):
        self.renderedCard = renderedCard

    def getRenderedCard(self):
        return self.renderedCard

    def renderCard(self):
        """Render the card here"""

    def showRenderedCard(self):
        print("template:", self.getTemplate())
        print("title:", self.getTitle())
        print("spellClass:", self.getSpellClass())
        print("level:", self.getLevel())
        print("target:", self.getTarget())
        print("effectType:", self.getEffectType())
        print("actionCost:", self.getActionCost())
        print("spellDuration:", self.getSpellDuration())
        print("spellRange:", self.getSpellRange())
        print("description:", self.getDescription())
        print("area:", self.getArea())
        print("page", self.getPage())
        print("materials:")
        print(self.getMaterials())
        print("spellType:")
        print(self.getSpellType())
        #self.renderedCard.show()

    def saveCard(self):
        """Save the card to filesystem"""
