import yaml
import glob
import sys
import time
from SpellCard import SpellCard

class Handler:

    cards = []

    def run(self):
        print '\n\n\nWelcome to the Spell Card generator!'
        time.sleep(1)
        self.stateMachine('list')

    def loadCardsFromFolder(self, cardFolder):
        path = cardFolder + "/*.yaml"
        data = map(lambda x: yaml.load_all(open(x)), glob.glob(path))

        for file in data:
            for card in file:
                newCard = SpellCard(card)
                self.cards.append(newCard)

    def stateMachine(self, action, card=None):
        if (len(self.cards) <= card):
            print str(card) + ' is not a valid selection'
            time.sleep(1.5)
            return self.stateMachine('list')

        if ('save' == action):
            self.cards[card].saveCardToFile()
            print '\nSaved to file: ' + self.cards[card].getTitle()
            time.sleep(1.5)
            return self.stateMachine('options', card)
        elif ('save_image' == action):
            self.cards[card].renderCard()
            self.cards[card].saveCardImage()
            self.cards[card].showCard()
            print '\nSaved as image: ' + self.cards[card].getTitle()
            time.sleep(1.5)
            return self.stateMachine('options', card)
        elif ('preview' == action):
            self.cards[card].renderCard()
            self.cards[card].showCard()
            print '\nShowing card: ' + self.cards[card].getTitle()
            time.sleep(1.5)
            return self.stateMachine('options', card)
        elif ('list' == action):
            print '\n\n\n-- List of cards --'
            for index, aCard in enumerate(self.cards):
                print str(index) + ':\t' + aCard.getTitle()
            cardNum = self.getInput('Please select a card: ')

            try:
                return self.stateMachine('options', int(cardNum))
            except ValueError:
                print str(cardNum) + ' is not a valid selection'
                time.sleep(1.5)
                return self.stateMachine('list')

        elif ('options' == action):
            print '\n\n\n-- Card options --'
            print '0:\tback'
            print '1:\tpreview card'
            print '2:\tsave file'
            print '3:\tsave image'

            response = self.getInput('Please select option: ')
            if ('0' == response):
                return self.stateMachine('list')
            elif ('1' == response):
                return self.stateMachine('preview', card)
            elif ('2' == response):
                return self.stateMachine('save', card)
            elif ('3' == response):
                return self.stateMachine('save_image', card)
            else:
                print str(response) + ' is not a valid selection'
                time.sleep(2)
                return self.stateMachine('options', card)

    def getInput(self, message):
        response = raw_input(message)

        if 'exit' == response:
            print 'Good bye'
            exit()

        return response

handler = Handler()

if len(sys.argv) > 1 and None != sys.argv[1]:
    handler.loadCardsFromFolder(sys.argv[1])
else:
    handler.loadCardsFromFolder('Card_Files')
handler.run()