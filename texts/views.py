from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import loader
from .forms import DeedForm
import random
from random import choice

def hello(request):
    return HttpResponse ("Hello world")

def diarydate(request):
    template = loader.get_template('texts/diarydate.html')
    year1 = random.randint(1570, 1590)
    month1 = random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    if month1 == "February":
        day1 = random.randint(1,29)
    elif month1 == "April" or month1 == "June" or month1 == "September" or month1 == "November":
        day1 = random.randint(1,30)
    else:
        day1 = random.randint(1,31)

    s1_emotions = {'a nightmare': 'awful', 'full of woe': 'forlorn', 'wonderful': 'content', 'lovely': 'restored'} # this generates the variables for the first sentence
    s1_emotions_var1 = random.choice(list(s1_emotions.keys()))

    ledger_mer = {'saved a person\'s life': '100',
            'ensured the fidelity of a woman': '100',
            'prevented someone from drowning a child or aborting a baby': '100',
            'maintained the family lineage': '50',
            'adopted an orphan': '50',
            'buried a corpse no one cared for': '50',
            'prevented a person from abandoning a village': '50',
            'remonstrated with an evildoer to change his way': '30',
            'rectified an justice': '30',
            'recommended a virtuous person for office': '10',
            'eliminated something harmful to the people': '10',
            'remonstrated with a litigant to withdraw a lawsuit': '5',
            'saved the life of a domestic animal': '5',
            'praised someone\'s good deed': '1',
            'did not join in someone\'s bad deed': '1',
            'remonstrated with someone from doing evil': '1',
            'cured someone\'s illness': '1',
            'provided a meal to a hungry person': '1',
            'buried a dead domestic animal': '1',
            'saved the life of an insect or watery creature': '1',
            'spent 100 coins on constructing a road': '1',
            'spent 100 coins on constructing a bridge': '1',
            'spent 100 coins on digging a waterway to benefit the people': '1',
            'spent 100 coins on repairing a sacred image': '1',
            'spent 100 coins giving assistance to the poor': '1',
            'donated tea worth 100 coins': '1',
            'donated medicine worth 100 coins': '1',
            'donated clothes worth 100 coins': '1',
            'donated coffins worth 100 coins': '1'}

    s2p1 = ('As I was strolling through my fields, I ', 'After meeting an old friend, I', 'After having argued with my concubine, I','As I was walking in the town square, I ', 'During my visit to the teahouse, I ', 'While meandering through the countryside, I')
    s2_var1 = random.choice(s2p1) #sets the initial setting
    mer_var1 = random.choice(list(ledger_mer.keys())) #selects the first meritorious act
    done_deeds = (mer_var1) #saves the done meritorious acts to a list
    print(s2_var1, mer_var1 + '.')
    s3_var1 = random.choice(list(ledger_mer.keys()))
    if s3_var1 in done_deeds:
        done_deeds.append(s3_var1)
        print('In addition I', random.choice(list(ledger_mer.keys())))
    else:
        print('I also', s3_var1 + '.')

    if s1_emotions_var1 == 'a nightmare':
        print ('And alas, I did so many bad deeds!')

    html = "This is the week of %s %s, %s. My days were %s and I feel %s. %s %s. In addition I %s." % (month1, day1, year1, s1_emotions_var1, s1_emotions[s1_emotions_var1], s2_var1, mer_var1, random.choice(list(ledger_mer.keys())))
    return render_to_response('texts/diarydate.html', {'html': html})

def FormCalculate(): #this function should add them all up, doesn't work
    response = input('Enter the deed: ')
    d1 = ledger_mer[response]
    if d1 in ledger_mer.keys():
        return int(d1)
    print("This action's merit is  " + x)
