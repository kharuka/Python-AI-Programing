edison='''Everything comes to him
who hustles while he waits.'''

picasso='''I am always doing that which I can not do,
in order that I may learn how to do it.'''

socrates='''he way to gain a good reputation is to endeavor
to be what you desire to appear.'''

while True:
    proverb=input('だれの格言ですか？--->')

    if proverb=='OK':
        print('またねー')
        break
    elif proverb=='エジソン':
        print(edison)
    elif proverb=='ピカソ':
        print(picasso)
    elif proverb=='ソクラテス':
        print(socrates)
    else:
        print('?')
