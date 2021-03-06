#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Demo: Running the Autism Quotient with scoring
    :Authors:
            - 2018: Anthony Haffey
"""

from __future__ import absolute_import, division, print_function
import os
# Import key parts of the PsychoPy library:

from psychopy import visual, event, data, core
from psychopy.visual import surveys,button
surveys.initialize()

# Create a visual window:
win = visual.Window(units='height', allowStencil=True)
title = visual.TextStim(win, "My test survey", units='height', pos=[0,0.45])

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

#experiment handler
expInfo = {'participant': '', 'session': '001'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expName = "AQForm"
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:/Users/antho/psychopy/psychopy/demos/surveys/aq_form.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

proceedConfirmed = False
proceedButton = visual.Button(win, buttonText="Proceed", buttonPos=(.3, -0.45),survey="AutismQuotient",thisExp =thisExp)

surveys.thisSurvey = visual.Form(   win,
                        excelFile='C:/Users/antho/psychopy/psychopy/demos/coder/surveys/AQ.xlsx',
                        size=(1, 1),
                        pos=(0.0, 0.0),
                        name="AutismQuotient")

currentSurvey = sum(surveys.completed) #i.e. 0

while surveys.completed[currentSurvey] == False:
    win.color = [255, 255, 255]  # clear blue in rgb255
    #survey.draw()
    surveys.thisSurvey.draw()
    proceedButton.draw()
    win.flip()

# The contents of this file are in the public domain.
