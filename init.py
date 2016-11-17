#!/usr/bin/python


class Bird(object):
    have_feather = True
    fuck = 'nimabi'

class haappy(Bird):
    def __init__(self,more_words):
        print 'we are haapy' , more_words


summer = haappy('haapy')

print summer.have_feather
print summer.fuck
