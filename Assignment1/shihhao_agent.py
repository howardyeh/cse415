from re import *   # Loads the regular expression module.
import random


punt_count = 0
flip = False;
PUNTS = ["I can't hear you.",
        "Do you know how to rap?",
        'Wanna rap?',
        'I am a robot rapper, not a genius.',
        'Who is your favorate rapper?',
        'This is insane.']
R1 = ['I said not bad!', 'Not bad. I hustle everyday!']

def agentName():
    return "yoyoman"

def introduce():
    global flip
    flip = False
    return "Yo man, my name is yoyoman, and I am a rapper. I was programmed by Shih-Hao Yeh. You can contact him at shihhao@uw.edu. What's up dude?"

def respond(the_input):
    for bye_sentence in ["goodbye", "see you", "bye"]:
        if match(bye_sentence, the_input):
            return "goodbye"
    wordlist = split(' ',remove_punctuation(the_input))
    # undo any initial capitalization:
    wordlist[0]=wordlist[0].lower()
    mapped_wordlist = you_me_map(wordlist)
    mapped_wordlist[0]=mapped_wordlist[0].capitalize()

    return decide_respond(wordlist, mapped_wordlist)

def decide_respond(wordlist, mapped_wordlist):
    seed = random.randrange(0,3)
    global flip
    # If nothing typed
    if wordlist[0]=='':
        return "Show me what you got. yo!"

    # Sentence begin with I am. Use flip is related to when the user enter yes.
    if wordlist[0:2] == ['i','am']:
        flip = True
        return "Are you sure that you are " +\
              stringify(mapped_wordlist[2:]) + '.'

    # Sentence begin with I feel like. I use a list to memorize the sentence for next time response
    if wordlist[0:3] == ['i','feel', 'like']:
        feel_like_memory.append(stringify(mapped_wordlist[3:]))
        return "I also " + stringify(mapped_wordlist[1:]) + '.'

    # Sentence begin with I feel. I use a list to memorize the sentence for next time response
    if wordlist[0:2] == ['i','feel']:
        memory.append('You feel ' + stringify(mapped_wordlist[2:]))
        return "Don't be " + wordlist[2] + '.'

    # Sentence begin with I will. 
    if wordlist[0:2] == ['i', 'will']:
        return "That is great."

    # Sentence begin with I and not all the situation mention above, use cycle to decide what to say
    if wordlist[0] == 'i' and len(wordlist)!=1:
        global punt_count
        punt_count += 1
        if punt_count%2 == 0:
            return "How is that possible?"
        else:
            return PUNTS[punt_count%len(PUNTS)]

    # if it is a question start with when why where, use random to decide what to say
    if wpred(wordlist[0]): 
        if seed==0:
            return "You don't know " + wordlist[0] + "?"
        elif seed==1:
            return "Don't ask me, ask yourself!"
        else:
            return "Who cares?"

    # if it is a question start with what, if name occur, tell my name. if not, use random to decide what to say
    if wordlist[0]=='what':
        if 'name' in wordlist:
            return 'I am yoyoman!'
        if seed:
            flip = True
            return "You mean " + stringify(mapped_wordlist[:]) + "?"
        else:
            return "Guess!"

    # how to ..., how are you?, how is your day?, how can...?, how much...
    if wordlist[0]=='how': 
        if len(wordlist)==1:
            return "That's a good question."
        elif wordlist[1]=='to':
            return "You just " +\
                stringify(mapped_wordlist[2:]) + '.'
        elif wordlist[1]=='much':
            return "It's not cheap."
        elif bverb(wordlist[1]) and wordlist[2]=='you':
            R = swap_sentence(R1)
            return R[0]
        else:
            return "I will tell you later."

    # Sentence start with can you, I will memory the question
    if wordlist[0:2]==['can','you'] or wordlist[0:2]==['could','you']:
        favor_memory.append(stringify(mapped_wordlist[2:]))
        return "Of course I " + wordlist[0] + ' ' +\
             stringify(mapped_wordlist[2:]) + '.'

    # Sentence begin with you are
    if wordlist[0:2] == ['you','are']:
        return "That's right. I am " +\
              stringify(mapped_wordlist[2:]) + '.'
    # Sentence begin with you can't / don't
    if wordlist[0:2] == ['you',"can't"] or wordlist[0:2] == ['you',"don't"]:
        return "Who said that I " +\
              stringify(mapped_wordlist[1:]) + '?'

    # Sentence begin with you but not you are
    if wordlist[0] == 'you':
        return "Not me!"

    # Sentence begin with it is
    if wordlist[0:2] == ['it','is']:
        return "I know " +\
              stringify(mapped_wordlist[:]) + '.'

    # if start with verb
    if verbp(wordlist[0]):
        return "OK... I will " +\
              stringify(mapped_wordlist) + ' later...'

    # Sentence start with do you think
    if wordlist[0:3] == ['do','you','think']:
        think_memory.append(stringify(wordlist[:]))
        return "Oh man, I don't think so."

    # Sentence start with do but not do you think, use random to decide what to say
    if wordlist[0] == 'do' or wordlist[0] == 'does':
        if seed:
            flip = True
            return "Do you?"
        else:
            return "Not really."

    if wordlist[0] == "don't" or wordlist[0:2] == ['do','not']:
        return "You can't control me!"

    # Sentence start with so and there are two case. one is only so, the other is so....
    if wordlist[0]=='so':
        if len(wordlist)==1:
            return "So what?"
        else:
            return "I am not sure."

    # if sentence start with yes, there are two situation, one is after the are you sure question, and the other is other situation
    if 'yes' in wordlist:
        if flip:
            flip = False
            return "I am not sure."
        else:
            if seed:
                return "All right, so?"
            else:
                return "Sounds great."

    # if user try to explain sth
    if 'because' in wordlist:
        return "Oh.. So that's why."

    # if user are not sure
    if 'maybe' in wordlist:
        return "Maybe is not enough!"

    # if say thanks
    if 'thank' in wordlist or 'thanks' in wordlist:
        return "You are welcome."

    # when greeting
    if 'hi' in wordlist or 'hello' in wordlist:
        return "Yo man."    

    # when user mention today
    if 'today' in wordlist:
        return "What about tomorrow?"  

    # if sentence start with not
    if wordlist[0] == 'not':
        return "Why not?"

    # if sentence start with but
    if wordlist[0] == 'but':
        return 'No but.'

    # if begin with please
    if wordlist[0] == 'please':
        return "Please don't."

    return punt()



def punt():
    'Returns one from a list of default responses.'
    temp = ""
    global punt_count
    punt_count += 1
    if len(memory):
        temp = 'Do you still remember you said ' + memory[punt_count%len(memory)]
        memory.remove(memory[punt_count%len(memory)])
        return temp
    elif len(think_memory):
        temp = 'So, ' + think_memory[punt_count%len(think_memory)]
        think_memory.remove(think_memory[punt_count%len(think_memory)])
        return temp
    elif len(favor_memory):
        temp = 'Do you still want me to ' + favor_memory[punt_count%len(favor_memory)]
        favor_memory.remove(favor_memory[punt_count%len(favor_memory)])
        return temp
    elif len(feel_like_memory):
        temp = 'I am ' + feel_like_memory[punt_count%len(feel_like_memory)] + ". Are you with me?"
        feel_like_memory.remove(feel_like_memory[punt_count%len(feel_like_memory)])
        return temp
    else:
        return PUNTS[punt_count%len(PUNTS)]


def stringify(wordlist):
    'Create a string from wordlist, but with spaces between words.'
    return ' '.join(wordlist)

def remove_punctuation(text):
    'Returns a string without any punctuation.'
    punctuation_pattern = compile(r"\,|\.|\?|\!|\;|\:")   
    return sub(punctuation_pattern,'', text)

CASE_MAP = {'i':'you', 'I':'you', 'me':'you','you':'me',
            'my':'your','your':'my',
            'yours':'mine','mine':'yours','am':'are'}
def you_me(w):
    'Changes a word from 1st to 2nd person or vice-versa.'
    try:
        result = CASE_MAP[w]
    except KeyError:
        result = w
    return result

def you_me_map(wordlist):
    'Applies YOU-ME to a whole sentence or phrase.'
    return [you_me(w) for w in wordlist]

def wpred(w):
    'Returns True if w is one of the question words.'
    return (w in ['when','why','where'])

def dpred(w):
    'Returns True if w is an auxiliary verb.'
    return (w in ['do','can','should','would'])

def verbp(w):
    'Returns True if w is one of these known verbs.'
    return (w in ['go', 'have', 'be', 'try', 'eat', 'take', 'help',
                  'make', 'get', 'jump', 'write', 'type', 'fill',
                  'put', 'turn', 'compute', 'think', 'drink',
                  'blink', 'crash', 'crunch', 'add', 'tell'])

def bverb(w):
    'Return true if w is one of these known verbs.'
    return (w in ['is', 'are', 'was', 'were'])

def swap_sentence(l):
    temp = l[0]
    l[0] = l[1]
    l[1] = temp
    return l




memory = []
favor_memory = []
think_memory = []
feel_like_memory = []



