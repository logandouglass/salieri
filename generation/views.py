### imports
## For acquiring and using music theoretical data
# import mingus.core.progressions as progressions
# import mingus.core.chords as chords
# import mingus.core.scales as scales
# import mingus.core.intervals as intervals
# import mingus.core.notes as notes

## For writing notes, chords bars, tracks, comps
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Composition as Mcomposition
from mingus.containers import Track as Mtrack

## for writing MIDI
from mingus.midi import midi_file_out

## django stuff
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from userinput.models import Composition, Track
from userinput.forms import ProgressionForm, TrackForm

## For improvisation and random generation (coming...eventually)
# import random

## For data check readability
# import pprint

### my music-writing functions
from salieri.Lfunctions import *
###===============================================================

#### views
def magic(request, id):
    """
    ==MASTER FUNCTION==
    Writes music as MIDI based on the user's commands

    """
    ### summon the comp and harvest the data from the django forms 
    comp_obj = Composition.objects.get(id=id)
    comp_data_dict_list = list(Composition.objects.filter(id=id).values())
    comp_data_dict = comp_data_dict_list[0] 

    name_harvest = comp_obj.name

    chord1_tonic_harvest = comp_obj.chord1_tonic
    chord1_quality_harvest = comp_obj.chord1_quality
    chord1_bars_harvest = comp_obj.chord1_bars

    chord2_tonic_harvest = comp_obj.chord2_tonic
    chord2_quality_harvest = comp_obj.chord2_quality
    chord2_bars_harvest = comp_obj.chord2_bars

    chord3_tonic_harvest = comp_obj.chord3_tonic
    chord3_quality_harvest = comp_obj.chord3_quality
    chord3_bars_harvest = comp_obj.chord3_bars

    chord4_tonic_harvest = comp_obj.chord4_tonic
    chord4_quality_harvest = comp_obj.chord4_quality
    chord4_bars_harvest = comp_obj.chord4_bars

    chord5_tonic_harvest = comp_obj.chord5_tonic
    chord5_quality_harvest = comp_obj.chord5_quality
    chord5_bars_harvest = comp_obj.chord5_bars

    ### Turn the tonic and quality data into chords as lists of unclassed notes
    chord1 = chordbuild(comp_data_dict['chord1_tonic'], comp_data_dict['chord1_quality'])
    chord2 = chordbuild(comp_data_dict['chord2_tonic'], comp_data_dict['chord2_quality'])
    chord3 = chordbuild(comp_data_dict['chord3_tonic'], comp_data_dict['chord3_quality'])
    chord4 = chordbuild(comp_data_dict['chord4_tonic'], comp_data_dict['chord4_quality'])
    chord5 = chordbuild(comp_data_dict['chord5_tonic'], comp_data_dict['chord5_quality'])



    # progression_seed = [
    #     (chord1_tonic_harvest)
    
    # ]
    ###=======================================================

    ### summon the comp tracks, the len of their set, and the track model param list 
    all_tracks = Track.objects.all()
    track_objs = all_tracks.filter(comp=comp_obj)
    track_obj_length = len(track_objs)
    track_params = list(Track.objects.values()[0].keys()) # investigate rube goldbergy way?

    
    ###=======================================================
    
    ### make the master dict list of track data
    track_dict_list = []
    for i in range(len(track_objs)):
        new_dict = {}
        for ii in range (len(track_params)):
            new_dict.update({track_params[ii]:list(list(all_tracks.filter(comp=comp_obj).values_list())[i])[ii]}) # I can't belive this works
        track_dict_list.append(new_dict)

    # for i in track_obj_length:
    #     new_dict = {}
    #     for

    ### debugging
    test_track = track_objs[0]
    type_test = f"{type(chord5_tonic_harvest)} + {chord5_tonic_harvest}"
    data_test = chord1
    data_test_2 = list(list(all_tracks.filter(comp=comp_obj).values_list())[0])
    data_test_3 = track_dict_list
    ###=========================================================


    context={

        ### debugging
        "test_track":test_track,
        "type_test":type_test,
        "data_test":data_test,
        "data_test_2":data_test_2,
        "data_test_3":data_test_3,
        ###====================

        "name_harvest":name_harvest,

        "chord1_tonic_harvest":chord1_tonic_harvest,
        "chord1_quality_harvest":chord1_quality_harvest,
        "chord1_bars_harvest":chord1_bars_harvest,

        "chord2_tonic_harvest":chord2_tonic_harvest,
        "chord2_quality_harvest":chord2_quality_harvest,
        "chord2_bars_harvest":chord2_bars_harvest,

        "chord3_tonic_harvest":chord3_tonic_harvest,
        "chord3_quality_harvest":chord3_quality_harvest,
        "chord3_bars_harvest":chord3_bars_harvest,

        "chord4_tonic_harvest":chord4_tonic_harvest,
        "chord4_quality_harvest":chord4_quality_harvest,
        "chord4_bars_harvest":chord4_bars_harvest,

        "chord5_tonic_harvest":chord5_tonic_harvest,
        "chord5_quality_harvest":chord5_quality_harvest,
        "chord5_bars_harvest":chord5_bars_harvest,

        "track_objs":track_objs,
        "track_obj_length":track_obj_length,

        }

    ###########################


    ###########################

    return render(request, "generation/datatest.html", context)
    ###=================================================================================


    #########################################
    # notes (ld)
    #
    #
    #
    #
    #
    #
    #
    ##

    ###############################################
    # scrap
    # Track._meta.get_fields() ## for non-rg retrieval of track model parameters

        # for track in track_objs:
    #     new_dict = {}
    #     for i in range (len(track_params)):
    #         new_dict.update({track_params[i]:track.objects.values[i]})
    #     track_dict_list.append(new_dict)

        # comp_params = list(list(Composition.objects.filter(id=id).values())[0].keys())
    # comp_values =