
# Response messages
WELCOME_MESSAGE = "Hi, welcome to Super Heroes, you can ask me about your favorite Super Heroes!"
HELP_MESSAGE = "You can ask me about a super hero, or, you can say exit... What can I help you with?"
HELP_REPROMPT = "What can I help you with?"
FALLBACK_MESSAGE = "I can't help you with that. It can tell you about super heroes",
FALLBACK_REPROMPT = "What can I help you with"
ERROR_MESSAGE = "Sorry, an error occurred."
STOP_MESSAGE = "Ok Bye"


# Provides hero details
def get_hero_info(hero_name):
    hero = hero_name.lower().replace('-', '').replace(' ', '')
    if hero == 'superman':
        return 'Dude wears underwear on top of his pants'
    elif hero == 'batman':
        return 'Na na na na na na na na Batman! He is a freaking weirdo, eehhh!'
    elif hero == 'spiderman':
        return 'Spider Man isn\'t the only one who gets his hand sticky,. After using the web...'
    elif hero == 'wonderwoman':
        return 'I am Wonder Woman I wonder where I left my keys. I wonder where I left my purse. I wonder where my ' \
               'money went '
    elif hero == 'ironman':
        return 'In fourth grade, Tony\'s, robotics teacher told him to build a little robot for the science fair, ' \
               'he finished it in a few hours and called it Optimus Prime! '
    else:
        return 'No data found'
