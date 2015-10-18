#! /usr/bin/env python
sentence = raw_input("Sentence: ")
screen_width = 80
text_width = len(sentence)
print "sentence length: " + `text_width`
box_width = text_width+6
left_margin = (screen_width - box_width) / 2
spc = 3
print
print ' ' * left_margin + '+' + '-' * (box_width) + '+'
print ' ' * left_margin + '|' + ' ' * (box_width)  + '|'
print ' ' * left_margin + '|' + ' ' * spc + sentence  + ' ' * spc + '|'
print ' ' * left_margin + '|' + ' ' * (box_width)  + '|'
print ' ' * left_margin + '+' + '-' * (box_width) + '+'
print
