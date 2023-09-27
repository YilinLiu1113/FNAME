#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Thu Dec 10 17:24:03 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'FNAME Recognition Practice'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/koeunlim/uatmslab Dropbox/FaceName Task/Psychopy/FNAME V2/V2_0 aMCI/Set_201206/Session1/FaceName_V2_0_Session1_CI.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DATA)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Directions_Encode"
Directions_EncodeClock = core.Clock()
Img_EncodInstr = visual.ImageStim(
    win=win,
    name='Img_EncodInstr', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.4, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Start_Encod = keyboard.Keyboard()
Voice_Encod = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Voice_Encod')
Voice_Encod.setVolume(1)

# Initialize components for Routine "Encoding"
EncodingClock = core.Clock()
encode_names = visual.TextStim(win=win, name='encode_names',
    text='default text',
    font='Arial',
    pos=(0, -.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
encode_faces = visual.ImageStim(
    win=win,
    name='encode_faces', 
    image='sin', mask=None,
    ori=0, pos=(0,.1), size=(0.7, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
encode_resp = keyboard.Keyboard()
label1 = visual.TextStim(win=win, name='label1',
    text='1',
    font='Arial',
    pos=(-0.38, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
label2 = visual.TextStim(win=win, name='label2',
    text='2',
    font='Arial',
    pos=(-0.13, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
label3 = visual.TextStim(win=win, name='label3',
    text='3',
    font='Arial',
    pos=(0.13, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
label4 = visual.TextStim(win=win, name='label4',
    text='4',
    font='Arial',
    pos=(0.38, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
label1_str = visual.TextStim(win=win, name='label1_str',
    text='Poor Match',
    font='Arial',
    pos=(-0.38, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color=[0.5,0.5,0.5], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
label4_str = visual.TextStim(win=win, name='label4_str',
    text='Good Match',
    font='Arial',
    pos=(0.38, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color=[0.5,0.5,0.5], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "Transition"
TransitionClock = core.Clock()
encode_fixation = visual.TextStim(win=win, name='encode_fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Directions_Retrieval"
Directions_RetrievalClock = core.Clock()
Img_RetrvInstr = visual.ImageStim(
    win=win,
    name='Img_RetrvInstr', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.4, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Start_Retrv = keyboard.Keyboard()
Voice_RetrvInstr = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='Voice_RetrvInstr')
Voice_RetrvInstr.setVolume(1)

# Initialize components for Routine "Retrieval"
RetrievalClock = core.Clock()
retrieve_faces = visual.ImageStim(
    win=win,
    name='retrieve_faces', 
    image='sin', mask=None,
    ori=0, pos=(-0.3, 0.2), size=(0.7, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
retrieve_names = visual.TextStim(win=win, name='retrieve_names',
    text='default text',
    font='Arial',
    pos=(0.3, 0.2), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
retrieve_resp = keyboard.Keyboard()
box1 = visual.Rect(
    win=win, name='box1',
    width=(0.4, 0.2)[0], height=(0.4, 0.2)[1],
    ori=0, pos=(-0.42, -0.22),
    lineWidth=2, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.5,0.5,0.5], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
box2 = visual.Rect(
    win=win, name='box2',
    width=(0.4, 0.2)[0], height=(0.4, 0.2)[1],
    ori=0, pos=(0, -0.22),
    lineWidth=2, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.5,0.5,0.5], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
box3 = visual.Rect(
    win=win, name='box3',
    width=(0.4, 0.2)[0], height=(0.4, 0.2)[1],
    ori=0, pos=(0.42, -0.22),
    lineWidth=2, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.5,0.5,0.5], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
num1_r = visual.TextStim(win=win, name='num1_r',
    text='Correct',
    font='Arial',
    pos=(-0.42, -0.2), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
num2_r = visual.TextStim(win=win, name='num2_r',
    text='Incorrect',
    font='Arial',
    pos=(0, -0.2), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
num3_r = visual.TextStim(win=win, name='num3_r',
    text='New',
    font='Arial',
    pos=(0.42, -0.2), height=0.07, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
label1_r = visual.TextStim(win=win, name='label1_r',
    text='default text',
    font='Arial',
    pos=(-0.42, -0.27), height=0.05, wrapWidth=None, ori=0, 
    color=[-0.5,-0.5,-0.5], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
label2_r = visual.TextStim(win=win, name='label2_r',
    text='2',
    font='Arial',
    pos=(0, -0.27), height=0.05, wrapWidth=None, ori=0, 
    color=[-0.5,-0.5,-0.5], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
label3_r = visual.TextStim(win=win, name='label3_r',
    text='3',
    font='Arial',
    pos=(0.42, -0.27), height=0.05, wrapWidth=None, ori=0, 
    color=[-0.5,-0.5,-0.5], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "Confirm_Response"
Confirm_ResponseClock = core.Clock()
text_instruction = visual.TextStim(win=win, name='text_instruction',
    text='Click on a box to confirm your response.',
    font='Arial',
    pos=(0, 0.25), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
confirm = visual.Rect(
    win=win, name='confirm',
    width=(0.3, 0.2)[0], height=(0.3, 0.2)[1],
    ori=0, pos=(-0.42, -0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
change = visual.Rect(
    win=win, name='change',
    width=(0.3, 0.2)[0], height=(0.3, 0.2)[1],
    ori=0, pos=(0, -0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
missed = visual.Rect(
    win=win, name='missed',
    width=(0.3, 0.2)[0], height=(0.3, 0.2)[1],
    ori=0, pos=(0.42, -0.1),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
text_confirm = visual.TextStim(win=win, name='text_confirm',
    text='Confirm',
    font='Arial',
    pos=(-0.42, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_change = visual.TextStim(win=win, name='text_change',
    text='Change\nof\nMind',
    font='Arial',
    pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_missed = visual.TextStim(win=win, name='text_missed',
    text='Missed',
    font='Arial',
    pos=(0.42, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
mouse_confirm = event.Mouse(win=win)
x, y = [None, None]
mouse_confirm.mouseClock = core.Clock()

# Initialize components for Routine "Transition"
TransitionClock = core.Clock()
encode_fixation = visual.TextStim(win=win, name='encode_fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Finish"
FinishClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Thank you for your time!',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
encodinstrloop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Condition_Instruction_Encod.csv'),
    seed=None, name='encodinstrloop')
thisExp.addLoop(encodinstrloop)  # add the loop to the experiment
thisEncodinstrloop = encodinstrloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEncodinstrloop.rgb)
if thisEncodinstrloop != None:
    for paramName in thisEncodinstrloop:
        exec('{} = thisEncodinstrloop[paramName]'.format(paramName))

for thisEncodinstrloop in encodinstrloop:
    currentLoop = encodinstrloop
    # abbreviate parameter names if possible (e.g. rgb = thisEncodinstrloop.rgb)
    if thisEncodinstrloop != None:
        for paramName in thisEncodinstrloop:
            exec('{} = thisEncodinstrloop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Directions_Encode"-------
    continueRoutine = True
    # update component parameters for each repeat
    Img_EncodInstr.setImage(encinstimage)
    Start_Encod.keys = []
    Start_Encod.rt = []
    _Start_Encod_allKeys = []
    Voice_Encod.setSound(encinstvoice, hamming=True)
    Voice_Encod.setVolume(1, log=False)
    # keep track of which components have finished
    Directions_EncodeComponents = [Img_EncodInstr, Start_Encod, Voice_Encod]
    for thisComponent in Directions_EncodeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Directions_EncodeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Directions_Encode"-------
    while continueRoutine:
        # get current time
        t = Directions_EncodeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Directions_EncodeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Img_EncodInstr* updates
        if Img_EncodInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Img_EncodInstr.frameNStart = frameN  # exact frame index
            Img_EncodInstr.tStart = t  # local t and not account for scr refresh
            Img_EncodInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Img_EncodInstr, 'tStartRefresh')  # time at next scr refresh
            Img_EncodInstr.setAutoDraw(True)
        
        # *Start_Encod* updates
        waitOnFlip = False
        if Start_Encod.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Start_Encod.frameNStart = frameN  # exact frame index
            Start_Encod.tStart = t  # local t and not account for scr refresh
            Start_Encod.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Start_Encod, 'tStartRefresh')  # time at next scr refresh
            Start_Encod.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Start_Encod.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Start_Encod.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Start_Encod.status == STARTED and not waitOnFlip:
            theseKeys = Start_Encod.getKeys(keyList=None, waitRelease=False)
            _Start_Encod_allKeys.extend(theseKeys)
            if len(_Start_Encod_allKeys):
                Start_Encod.keys = _Start_Encod_allKeys[-1].name  # just the last key pressed
                Start_Encod.rt = _Start_Encod_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop Voice_Encod
        if Voice_Encod.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Voice_Encod.frameNStart = frameN  # exact frame index
            Voice_Encod.tStart = t  # local t and not account for scr refresh
            Voice_Encod.tStartRefresh = tThisFlipGlobal  # on global time
            Voice_Encod.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Directions_EncodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Directions_Encode"-------
    for thisComponent in Directions_EncodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    encodinstrloop.addData('Img_EncodInstr.started', Img_EncodInstr.tStartRefresh)
    encodinstrloop.addData('Img_EncodInstr.stopped', Img_EncodInstr.tStopRefresh)
    # check responses
    if Start_Encod.keys in ['', [], None]:  # No response was made
        Start_Encod.keys = None
    encodinstrloop.addData('Start_Encod.keys',Start_Encod.keys)
    if Start_Encod.keys != None:  # we had a response
        encodinstrloop.addData('Start_Encod.rt', Start_Encod.rt)
    encodinstrloop.addData('Start_Encod.started', Start_Encod.tStartRefresh)
    encodinstrloop.addData('Start_Encod.stopped', Start_Encod.tStopRefresh)
    Voice_Encod.stop()  # ensure sound has stopped at end of routine
    encodinstrloop.addData('Voice_Encod.started', Voice_Encod.tStartRefresh)
    encodinstrloop.addData('Voice_Encod.stopped', Voice_Encod.tStopRefresh)
    # the Routine "Directions_Encode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'encodinstrloop'


# set up handler to look after randomisation of conditions etc
encodeloop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Condition_Encod.csv'),
    seed=None, name='encodeloop')
thisExp.addLoop(encodeloop)  # add the loop to the experiment
thisEncodeloop = encodeloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisEncodeloop.rgb)
if thisEncodeloop != None:
    for paramName in thisEncodeloop:
        exec('{} = thisEncodeloop[paramName]'.format(paramName))

for thisEncodeloop in encodeloop:
    currentLoop = encodeloop
    # abbreviate parameter names if possible (e.g. rgb = thisEncodeloop.rgb)
    if thisEncodeloop != None:
        for paramName in thisEncodeloop:
            exec('{} = thisEncodeloop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Encoding"-------
    continueRoutine = True
    # update component parameters for each repeat
    encode_names.setText(encodename)
    encode_faces.setImage(encodeimage)
    encode_resp.keys = []
    encode_resp.rt = []
    _encode_resp_allKeys = []
    # keep track of which components have finished
    EncodingComponents = [encode_names, encode_faces, encode_resp, label1, label2, label3, label4, label1_str, label4_str]
    for thisComponent in EncodingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    EncodingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Encoding"-------
    while continueRoutine:
        # get current time
        t = EncodingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=EncodingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *encode_names* updates
        if encode_names.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encode_names.frameNStart = frameN  # exact frame index
            encode_names.tStart = t  # local t and not account for scr refresh
            encode_names.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encode_names, 'tStartRefresh')  # time at next scr refresh
            encode_names.setAutoDraw(True)
        if encode_names.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encode_names.tStartRefresh + 5.5-frameTolerance:
                # keep track of stop time/frame for later
                encode_names.tStop = t  # not accounting for scr refresh
                encode_names.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encode_names, 'tStopRefresh')  # time at next scr refresh
                encode_names.setAutoDraw(False)
        
        # *encode_faces* updates
        if encode_faces.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encode_faces.frameNStart = frameN  # exact frame index
            encode_faces.tStart = t  # local t and not account for scr refresh
            encode_faces.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encode_faces, 'tStartRefresh')  # time at next scr refresh
            encode_faces.setAutoDraw(True)
        if encode_faces.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encode_faces.tStartRefresh + 5.5-frameTolerance:
                # keep track of stop time/frame for later
                encode_faces.tStop = t  # not accounting for scr refresh
                encode_faces.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encode_faces, 'tStopRefresh')  # time at next scr refresh
                encode_faces.setAutoDraw(False)
        
        # *encode_resp* updates
        waitOnFlip = False
        if encode_resp.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            encode_resp.frameNStart = frameN  # exact frame index
            encode_resp.tStart = t  # local t and not account for scr refresh
            encode_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encode_resp, 'tStartRefresh')  # time at next scr refresh
            encode_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(encode_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(encode_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if encode_resp.status == STARTED and not waitOnFlip:
            theseKeys = encode_resp.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
            _encode_resp_allKeys.extend(theseKeys)
            if len(_encode_resp_allKeys):
                encode_resp.keys = _encode_resp_allKeys[-1].name  # just the last key pressed
                encode_resp.rt = _encode_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *label1* updates
        if label1.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            label1.frameNStart = frameN  # exact frame index
            label1.tStart = t  # local t and not account for scr refresh
            label1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label1, 'tStartRefresh')  # time at next scr refresh
            label1.setAutoDraw(True)
        
        # *label2* updates
        if label2.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            label2.frameNStart = frameN  # exact frame index
            label2.tStart = t  # local t and not account for scr refresh
            label2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label2, 'tStartRefresh')  # time at next scr refresh
            label2.setAutoDraw(True)
        
        # *label3* updates
        if label3.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            label3.frameNStart = frameN  # exact frame index
            label3.tStart = t  # local t and not account for scr refresh
            label3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label3, 'tStartRefresh')  # time at next scr refresh
            label3.setAutoDraw(True)
        
        # *label4* updates
        if label4.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            label4.frameNStart = frameN  # exact frame index
            label4.tStart = t  # local t and not account for scr refresh
            label4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label4, 'tStartRefresh')  # time at next scr refresh
            label4.setAutoDraw(True)
        
        # *label1_str* updates
        if label1_str.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            label1_str.frameNStart = frameN  # exact frame index
            label1_str.tStart = t  # local t and not account for scr refresh
            label1_str.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label1_str, 'tStartRefresh')  # time at next scr refresh
            label1_str.setAutoDraw(True)
        
        # *label4_str* updates
        if label4_str.status == NOT_STARTED and tThisFlip >= 5.5-frameTolerance:
            # keep track of start time/frame for later
            label4_str.frameNStart = frameN  # exact frame index
            label4_str.tStart = t  # local t and not account for scr refresh
            label4_str.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label4_str, 'tStartRefresh')  # time at next scr refresh
            label4_str.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EncodingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Encoding"-------
    for thisComponent in EncodingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    encodeloop.addData('encode_names.started', encode_names.tStartRefresh)
    encodeloop.addData('encode_names.stopped', encode_names.tStopRefresh)
    encodeloop.addData('encode_faces.started', encode_faces.tStartRefresh)
    encodeloop.addData('encode_faces.stopped', encode_faces.tStopRefresh)
    # check responses
    if encode_resp.keys in ['', [], None]:  # No response was made
        encode_resp.keys = None
    encodeloop.addData('encode_resp.keys',encode_resp.keys)
    if encode_resp.keys != None:  # we had a response
        encodeloop.addData('encode_resp.rt', encode_resp.rt)
    encodeloop.addData('encode_resp.started', encode_resp.tStartRefresh)
    encodeloop.addData('encode_resp.stopped', encode_resp.tStopRefresh)
    encodeloop.addData('label1.started', label1.tStartRefresh)
    encodeloop.addData('label1.stopped', label1.tStopRefresh)
    encodeloop.addData('label2.started', label2.tStartRefresh)
    encodeloop.addData('label2.stopped', label2.tStopRefresh)
    encodeloop.addData('label3.started', label3.tStartRefresh)
    encodeloop.addData('label3.stopped', label3.tStopRefresh)
    encodeloop.addData('label4.started', label4.tStartRefresh)
    encodeloop.addData('label4.stopped', label4.tStopRefresh)
    encodeloop.addData('label1_str.started', label1_str.tStartRefresh)
    encodeloop.addData('label1_str.stopped', label1_str.tStopRefresh)
    encodeloop.addData('label4_str.started', label4_str.tStartRefresh)
    encodeloop.addData('label4_str.stopped', label4_str.tStopRefresh)
    # the Routine "Encoding" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Transition"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    TransitionComponents = [encode_fixation]
    for thisComponent in TransitionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TransitionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Transition"-------
    while continueRoutine:
        # get current time
        t = TransitionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TransitionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *encode_fixation* updates
        if encode_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encode_fixation.frameNStart = frameN  # exact frame index
            encode_fixation.tStart = t  # local t and not account for scr refresh
            encode_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encode_fixation, 'tStartRefresh')  # time at next scr refresh
            encode_fixation.setAutoDraw(True)
        if encode_fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encode_fixation.tStartRefresh + fixation-frameTolerance:
                # keep track of stop time/frame for later
                encode_fixation.tStop = t  # not accounting for scr refresh
                encode_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encode_fixation, 'tStopRefresh')  # time at next scr refresh
                encode_fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TransitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Transition"-------
    for thisComponent in TransitionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    encodeloop.addData('encode_fixation.started', encode_fixation.tStartRefresh)
    encodeloop.addData('encode_fixation.stopped', encode_fixation.tStopRefresh)
    # the Routine "Transition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'encodeloop'

# get names of stimulus parameters
if encodeloop.trialList in ([], [None], None):
    params = []
else:
    params = encodeloop.trialList[0].keys()
# save data for this loop
encodeloop.saveAsExcel(filename + '.xlsx', sheetName='encodeloop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
encodeloop.saveAsText(filename + 'encodeloop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
retrievinstrloop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Condition_Instruction_Retriev.csv'),
    seed=None, name='retrievinstrloop')
thisExp.addLoop(retrievinstrloop)  # add the loop to the experiment
thisRetrievinstrloop = retrievinstrloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRetrievinstrloop.rgb)
if thisRetrievinstrloop != None:
    for paramName in thisRetrievinstrloop:
        exec('{} = thisRetrievinstrloop[paramName]'.format(paramName))

for thisRetrievinstrloop in retrievinstrloop:
    currentLoop = retrievinstrloop
    # abbreviate parameter names if possible (e.g. rgb = thisRetrievinstrloop.rgb)
    if thisRetrievinstrloop != None:
        for paramName in thisRetrievinstrloop:
            exec('{} = thisRetrievinstrloop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Directions_Retrieval"-------
    continueRoutine = True
    # update component parameters for each repeat
    Img_RetrvInstr.setImage(retinstimage)
    Start_Retrv.keys = []
    Start_Retrv.rt = []
    _Start_Retrv_allKeys = []
    Voice_RetrvInstr.setSound(retinstvoice, hamming=True)
    Voice_RetrvInstr.setVolume(1, log=False)
    # keep track of which components have finished
    Directions_RetrievalComponents = [Img_RetrvInstr, Start_Retrv, Voice_RetrvInstr]
    for thisComponent in Directions_RetrievalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Directions_RetrievalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Directions_Retrieval"-------
    while continueRoutine:
        # get current time
        t = Directions_RetrievalClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Directions_RetrievalClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Img_RetrvInstr* updates
        if Img_RetrvInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Img_RetrvInstr.frameNStart = frameN  # exact frame index
            Img_RetrvInstr.tStart = t  # local t and not account for scr refresh
            Img_RetrvInstr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Img_RetrvInstr, 'tStartRefresh')  # time at next scr refresh
            Img_RetrvInstr.setAutoDraw(True)
        
        # *Start_Retrv* updates
        waitOnFlip = False
        if Start_Retrv.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Start_Retrv.frameNStart = frameN  # exact frame index
            Start_Retrv.tStart = t  # local t and not account for scr refresh
            Start_Retrv.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Start_Retrv, 'tStartRefresh')  # time at next scr refresh
            Start_Retrv.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Start_Retrv.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Start_Retrv.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Start_Retrv.status == STARTED and not waitOnFlip:
            theseKeys = Start_Retrv.getKeys(keyList=None, waitRelease=False)
            _Start_Retrv_allKeys.extend(theseKeys)
            if len(_Start_Retrv_allKeys):
                Start_Retrv.keys = _Start_Retrv_allKeys[-1].name  # just the last key pressed
                Start_Retrv.rt = _Start_Retrv_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop Voice_RetrvInstr
        if Voice_RetrvInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Voice_RetrvInstr.frameNStart = frameN  # exact frame index
            Voice_RetrvInstr.tStart = t  # local t and not account for scr refresh
            Voice_RetrvInstr.tStartRefresh = tThisFlipGlobal  # on global time
            Voice_RetrvInstr.play(when=win)  # sync with win flip
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Directions_RetrievalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Directions_Retrieval"-------
    for thisComponent in Directions_RetrievalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    retrievinstrloop.addData('Img_RetrvInstr.started', Img_RetrvInstr.tStartRefresh)
    retrievinstrloop.addData('Img_RetrvInstr.stopped', Img_RetrvInstr.tStopRefresh)
    # check responses
    if Start_Retrv.keys in ['', [], None]:  # No response was made
        Start_Retrv.keys = None
    retrievinstrloop.addData('Start_Retrv.keys',Start_Retrv.keys)
    if Start_Retrv.keys != None:  # we had a response
        retrievinstrloop.addData('Start_Retrv.rt', Start_Retrv.rt)
    retrievinstrloop.addData('Start_Retrv.started', Start_Retrv.tStartRefresh)
    retrievinstrloop.addData('Start_Retrv.stopped', Start_Retrv.tStopRefresh)
    Voice_RetrvInstr.stop()  # ensure sound has stopped at end of routine
    retrievinstrloop.addData('Voice_RetrvInstr.started', Voice_RetrvInstr.tStartRefresh)
    retrievinstrloop.addData('Voice_RetrvInstr.stopped', Voice_RetrvInstr.tStopRefresh)
    # the Routine "Directions_Retrieval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'retrievinstrloop'


# set up handler to look after randomisation of conditions etc
retrieval_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Condition_Retriev.csv'),
    seed=None, name='retrieval_loop')
thisExp.addLoop(retrieval_loop)  # add the loop to the experiment
thisRetrieval_loop = retrieval_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRetrieval_loop.rgb)
if thisRetrieval_loop != None:
    for paramName in thisRetrieval_loop:
        exec('{} = thisRetrieval_loop[paramName]'.format(paramName))

for thisRetrieval_loop in retrieval_loop:
    currentLoop = retrieval_loop
    # abbreviate parameter names if possible (e.g. rgb = thisRetrieval_loop.rgb)
    if thisRetrieval_loop != None:
        for paramName in thisRetrieval_loop:
            exec('{} = thisRetrieval_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Retrieval"-------
    continueRoutine = True
    # update component parameters for each repeat
    retrieve_faces.setImage(retrieveimage)
    retrieve_names.setText(retrievename)
    retrieve_resp.keys = []
    retrieve_resp.rt = []
    _retrieve_resp_allKeys = []
    label1_r.setText('1')
    # keep track of which components have finished
    RetrievalComponents = [retrieve_faces, retrieve_names, retrieve_resp, box1, box2, box3, num1_r, num2_r, num3_r, label1_r, label2_r, label3_r]
    for thisComponent in RetrievalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RetrievalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Retrieval"-------
    while continueRoutine:
        # get current time
        t = RetrievalClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RetrievalClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *retrieve_faces* updates
        if retrieve_faces.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            retrieve_faces.frameNStart = frameN  # exact frame index
            retrieve_faces.tStart = t  # local t and not account for scr refresh
            retrieve_faces.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(retrieve_faces, 'tStartRefresh')  # time at next scr refresh
            retrieve_faces.setAutoDraw(True)
        if retrieve_faces.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > retrieve_faces.tStartRefresh + 5.5-frameTolerance:
                # keep track of stop time/frame for later
                retrieve_faces.tStop = t  # not accounting for scr refresh
                retrieve_faces.frameNStop = frameN  # exact frame index
                win.timeOnFlip(retrieve_faces, 'tStopRefresh')  # time at next scr refresh
                retrieve_faces.setAutoDraw(False)
        
        # *retrieve_names* updates
        if retrieve_names.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            retrieve_names.frameNStart = frameN  # exact frame index
            retrieve_names.tStart = t  # local t and not account for scr refresh
            retrieve_names.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(retrieve_names, 'tStartRefresh')  # time at next scr refresh
            retrieve_names.setAutoDraw(True)
        if retrieve_names.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > retrieve_names.tStartRefresh + 5.5-frameTolerance:
                # keep track of stop time/frame for later
                retrieve_names.tStop = t  # not accounting for scr refresh
                retrieve_names.frameNStop = frameN  # exact frame index
                win.timeOnFlip(retrieve_names, 'tStopRefresh')  # time at next scr refresh
                retrieve_names.setAutoDraw(False)
        
        # *retrieve_resp* updates
        waitOnFlip = False
        if retrieve_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            retrieve_resp.frameNStart = frameN  # exact frame index
            retrieve_resp.tStart = t  # local t and not account for scr refresh
            retrieve_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(retrieve_resp, 'tStartRefresh')  # time at next scr refresh
            retrieve_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(retrieve_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(retrieve_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if retrieve_resp.status == STARTED and not waitOnFlip:
            theseKeys = retrieve_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _retrieve_resp_allKeys.extend(theseKeys)
            if len(_retrieve_resp_allKeys):
                retrieve_resp.keys = _retrieve_resp_allKeys[-1].name  # just the last key pressed
                retrieve_resp.rt = _retrieve_resp_allKeys[-1].rt
                # was this correct?
                if (retrieve_resp.keys == str(retrievecode)) or (retrieve_resp.keys == retrievecode):
                    retrieve_resp.corr = 1
                else:
                    retrieve_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *box1* updates
        if box1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box1.frameNStart = frameN  # exact frame index
            box1.tStart = t  # local t and not account for scr refresh
            box1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box1, 'tStartRefresh')  # time at next scr refresh
            box1.setAutoDraw(True)
        
        # *box2* updates
        if box2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box2.frameNStart = frameN  # exact frame index
            box2.tStart = t  # local t and not account for scr refresh
            box2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box2, 'tStartRefresh')  # time at next scr refresh
            box2.setAutoDraw(True)
        
        # *box3* updates
        if box3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            box3.frameNStart = frameN  # exact frame index
            box3.tStart = t  # local t and not account for scr refresh
            box3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(box3, 'tStartRefresh')  # time at next scr refresh
            box3.setAutoDraw(True)
        
        # *num1_r* updates
        if num1_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            num1_r.frameNStart = frameN  # exact frame index
            num1_r.tStart = t  # local t and not account for scr refresh
            num1_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(num1_r, 'tStartRefresh')  # time at next scr refresh
            num1_r.setAutoDraw(True)
        
        # *num2_r* updates
        if num2_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            num2_r.frameNStart = frameN  # exact frame index
            num2_r.tStart = t  # local t and not account for scr refresh
            num2_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(num2_r, 'tStartRefresh')  # time at next scr refresh
            num2_r.setAutoDraw(True)
        
        # *num3_r* updates
        if num3_r.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            num3_r.frameNStart = frameN  # exact frame index
            num3_r.tStart = t  # local t and not account for scr refresh
            num3_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(num3_r, 'tStartRefresh')  # time at next scr refresh
            num3_r.setAutoDraw(True)
        
        # *label1_r* updates
        if label1_r.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            label1_r.frameNStart = frameN  # exact frame index
            label1_r.tStart = t  # local t and not account for scr refresh
            label1_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label1_r, 'tStartRefresh')  # time at next scr refresh
            label1_r.setAutoDraw(True)
        
        # *label2_r* updates
        if label2_r.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            label2_r.frameNStart = frameN  # exact frame index
            label2_r.tStart = t  # local t and not account for scr refresh
            label2_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label2_r, 'tStartRefresh')  # time at next scr refresh
            label2_r.setAutoDraw(True)
        
        # *label3_r* updates
        if label3_r.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            label3_r.frameNStart = frameN  # exact frame index
            label3_r.tStart = t  # local t and not account for scr refresh
            label3_r.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(label3_r, 'tStartRefresh')  # time at next scr refresh
            label3_r.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RetrievalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Retrieval"-------
    for thisComponent in RetrievalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    retrieval_loop.addData('retrieve_faces.started', retrieve_faces.tStartRefresh)
    retrieval_loop.addData('retrieve_faces.stopped', retrieve_faces.tStopRefresh)
    retrieval_loop.addData('retrieve_names.started', retrieve_names.tStartRefresh)
    retrieval_loop.addData('retrieve_names.stopped', retrieve_names.tStopRefresh)
    # check responses
    if retrieve_resp.keys in ['', [], None]:  # No response was made
        retrieve_resp.keys = None
        # was no response the correct answer?!
        if str(retrievecode).lower() == 'none':
           retrieve_resp.corr = 1;  # correct non-response
        else:
           retrieve_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for retrieval_loop (TrialHandler)
    retrieval_loop.addData('retrieve_resp.keys',retrieve_resp.keys)
    retrieval_loop.addData('retrieve_resp.corr', retrieve_resp.corr)
    if retrieve_resp.keys != None:  # we had a response
        retrieval_loop.addData('retrieve_resp.rt', retrieve_resp.rt)
    retrieval_loop.addData('retrieve_resp.started', retrieve_resp.tStartRefresh)
    retrieval_loop.addData('retrieve_resp.stopped', retrieve_resp.tStopRefresh)
    retrieval_loop.addData('box1.started', box1.tStartRefresh)
    retrieval_loop.addData('box1.stopped', box1.tStopRefresh)
    retrieval_loop.addData('box2.started', box2.tStartRefresh)
    retrieval_loop.addData('box2.stopped', box2.tStopRefresh)
    retrieval_loop.addData('box3.started', box3.tStartRefresh)
    retrieval_loop.addData('box3.stopped', box3.tStopRefresh)
    retrieval_loop.addData('num1_r.started', num1_r.tStartRefresh)
    retrieval_loop.addData('num1_r.stopped', num1_r.tStopRefresh)
    retrieval_loop.addData('num2_r.started', num2_r.tStartRefresh)
    retrieval_loop.addData('num2_r.stopped', num2_r.tStopRefresh)
    retrieval_loop.addData('num3_r.started', num3_r.tStartRefresh)
    retrieval_loop.addData('num3_r.stopped', num3_r.tStopRefresh)
    retrieval_loop.addData('label1_r.started', label1_r.tStartRefresh)
    retrieval_loop.addData('label1_r.stopped', label1_r.tStopRefresh)
    retrieval_loop.addData('label2_r.started', label2_r.tStartRefresh)
    retrieval_loop.addData('label2_r.stopped', label2_r.tStopRefresh)
    retrieval_loop.addData('label3_r.started', label3_r.tStartRefresh)
    retrieval_loop.addData('label3_r.stopped', label3_r.tStopRefresh)
    # the Routine "Retrieval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Confirm_Response"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouse_confirm
    mouse_confirm.x = []
    mouse_confirm.y = []
    mouse_confirm.leftButton = []
    mouse_confirm.midButton = []
    mouse_confirm.rightButton = []
    mouse_confirm.time = []
    mouse_confirm.clicked_name = []
    gotValidClick = False  # until a click is received
    mouse_confirm.mouseClock.reset()
    # keep track of which components have finished
    Confirm_ResponseComponents = [text_instruction, confirm, change, missed, text_confirm, text_change, text_missed, mouse_confirm]
    for thisComponent in Confirm_ResponseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Confirm_ResponseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Confirm_Response"-------
    while continueRoutine:
        # get current time
        t = Confirm_ResponseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Confirm_ResponseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_instruction* updates
        if text_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_instruction.frameNStart = frameN  # exact frame index
            text_instruction.tStart = t  # local t and not account for scr refresh
            text_instruction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_instruction, 'tStartRefresh')  # time at next scr refresh
            text_instruction.setAutoDraw(True)
        
        # *confirm* updates
        if confirm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confirm.frameNStart = frameN  # exact frame index
            confirm.tStart = t  # local t and not account for scr refresh
            confirm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirm, 'tStartRefresh')  # time at next scr refresh
            confirm.setAutoDraw(True)
        
        # *change* updates
        if change.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            change.frameNStart = frameN  # exact frame index
            change.tStart = t  # local t and not account for scr refresh
            change.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(change, 'tStartRefresh')  # time at next scr refresh
            change.setAutoDraw(True)
        
        # *missed* updates
        if missed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            missed.frameNStart = frameN  # exact frame index
            missed.tStart = t  # local t and not account for scr refresh
            missed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(missed, 'tStartRefresh')  # time at next scr refresh
            missed.setAutoDraw(True)
        
        # *text_confirm* updates
        if text_confirm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_confirm.frameNStart = frameN  # exact frame index
            text_confirm.tStart = t  # local t and not account for scr refresh
            text_confirm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_confirm, 'tStartRefresh')  # time at next scr refresh
            text_confirm.setAutoDraw(True)
        
        # *text_change* updates
        if text_change.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_change.frameNStart = frameN  # exact frame index
            text_change.tStart = t  # local t and not account for scr refresh
            text_change.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_change, 'tStartRefresh')  # time at next scr refresh
            text_change.setAutoDraw(True)
        
        # *text_missed* updates
        if text_missed.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_missed.frameNStart = frameN  # exact frame index
            text_missed.tStart = t  # local t and not account for scr refresh
            text_missed.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_missed, 'tStartRefresh')  # time at next scr refresh
            text_missed.setAutoDraw(True)
        # *mouse_confirm* updates
        if mouse_confirm.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_confirm.frameNStart = frameN  # exact frame index
            mouse_confirm.tStart = t  # local t and not account for scr refresh
            mouse_confirm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_confirm, 'tStartRefresh')  # time at next scr refresh
            mouse_confirm.status = STARTED
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if mouse_confirm.status == STARTED:  # only update if started and not finished!
            buttons = mouse_confirm.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [confirm, change, missed]:
                        if obj.contains(mouse_confirm):
                            gotValidClick = True
                            mouse_confirm.clicked_name.append(obj.name)
                    x, y = mouse_confirm.getPos()
                    mouse_confirm.x.append(x)
                    mouse_confirm.y.append(y)
                    buttons = mouse_confirm.getPressed()
                    mouse_confirm.leftButton.append(buttons[0])
                    mouse_confirm.midButton.append(buttons[1])
                    mouse_confirm.rightButton.append(buttons[2])
                    mouse_confirm.time.append(mouse_confirm.mouseClock.getTime())
                    # abort routine on response
                    continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Confirm_ResponseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Confirm_Response"-------
    for thisComponent in Confirm_ResponseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    retrieval_loop.addData('text_instruction.started', text_instruction.tStartRefresh)
    retrieval_loop.addData('text_instruction.stopped', text_instruction.tStopRefresh)
    retrieval_loop.addData('confirm.started', confirm.tStartRefresh)
    retrieval_loop.addData('confirm.stopped', confirm.tStopRefresh)
    retrieval_loop.addData('change.started', change.tStartRefresh)
    retrieval_loop.addData('change.stopped', change.tStopRefresh)
    retrieval_loop.addData('missed.started', missed.tStartRefresh)
    retrieval_loop.addData('missed.stopped', missed.tStopRefresh)
    retrieval_loop.addData('text_confirm.started', text_confirm.tStartRefresh)
    retrieval_loop.addData('text_confirm.stopped', text_confirm.tStopRefresh)
    retrieval_loop.addData('text_change.started', text_change.tStartRefresh)
    retrieval_loop.addData('text_change.stopped', text_change.tStopRefresh)
    retrieval_loop.addData('text_missed.started', text_missed.tStartRefresh)
    retrieval_loop.addData('text_missed.stopped', text_missed.tStopRefresh)
    # store data for retrieval_loop (TrialHandler)
    if len(mouse_confirm.x): retrieval_loop.addData('mouse_confirm.x', mouse_confirm.x[0])
    if len(mouse_confirm.y): retrieval_loop.addData('mouse_confirm.y', mouse_confirm.y[0])
    if len(mouse_confirm.leftButton): retrieval_loop.addData('mouse_confirm.leftButton', mouse_confirm.leftButton[0])
    if len(mouse_confirm.midButton): retrieval_loop.addData('mouse_confirm.midButton', mouse_confirm.midButton[0])
    if len(mouse_confirm.rightButton): retrieval_loop.addData('mouse_confirm.rightButton', mouse_confirm.rightButton[0])
    if len(mouse_confirm.time): retrieval_loop.addData('mouse_confirm.time', mouse_confirm.time[0])
    if len(mouse_confirm.clicked_name): retrieval_loop.addData('mouse_confirm.clicked_name', mouse_confirm.clicked_name[0])
    retrieval_loop.addData('mouse_confirm.started', mouse_confirm.tStart)
    retrieval_loop.addData('mouse_confirm.stopped', mouse_confirm.tStop)
    # the Routine "Confirm_Response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Transition"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    TransitionComponents = [encode_fixation]
    for thisComponent in TransitionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TransitionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Transition"-------
    while continueRoutine:
        # get current time
        t = TransitionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TransitionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *encode_fixation* updates
        if encode_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            encode_fixation.frameNStart = frameN  # exact frame index
            encode_fixation.tStart = t  # local t and not account for scr refresh
            encode_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(encode_fixation, 'tStartRefresh')  # time at next scr refresh
            encode_fixation.setAutoDraw(True)
        if encode_fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > encode_fixation.tStartRefresh + fixation-frameTolerance:
                # keep track of stop time/frame for later
                encode_fixation.tStop = t  # not accounting for scr refresh
                encode_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(encode_fixation, 'tStopRefresh')  # time at next scr refresh
                encode_fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TransitionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Transition"-------
    for thisComponent in TransitionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    retrieval_loop.addData('encode_fixation.started', encode_fixation.tStartRefresh)
    retrieval_loop.addData('encode_fixation.stopped', encode_fixation.tStopRefresh)
    # the Routine "Transition" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'retrieval_loop'

# get names of stimulus parameters
if retrieval_loop.trialList in ([], [None], None):
    params = []
else:
    params = retrieval_loop.trialList[0].keys()
# save data for this loop
retrieval_loop.saveAsExcel(filename + '.xlsx', sheetName='retrieval_loop',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
retrieval_loop.saveAsText(filename + 'retrieval_loop.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Finish"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
FinishComponents = [text_2]
for thisComponent in FinishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinishClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Finish"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FinishClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinishClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Finish"-------
for thisComponent in FinishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
