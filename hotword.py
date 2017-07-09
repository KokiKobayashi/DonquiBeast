#!/usr/bin/env python

# Copyright (C) 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import print_function

import argparse
import os.path
import json

import google.oauth2.credentials

from google.assistant.library import Assistant
from google.assistant.library.event import EventType
from google.assistant.library.file_helpers import existing_file

#for playing music
import subprocess
from subprocess import Popen

import time
import Motor
import Weather


is_moved = False
p=1
def process_event(event, assistant):
    global p
    """Pretty prints events.

    Prints all events that occur with two spaces between each new
    conversation and a single space between turns of a conversation.

    Args:
        event(event.Event): The current event to process.
    """
    if event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        print()

    print(event)

    if event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED:
        print()
        if (event.args['text'] == 'music start' or event.args['text'] == 'play music' or event.args['text'] == 'play the music' or event.args['text'] == 'play Miracle shopping' or event.args['text'] == 'donkihote'):
            # 音楽再生
            p = Popen("aplay shopping-short.wav", shell = True)
            assistant.stop_conversation()
#        if (event.args['text'] == 'stop music' or event.args['text'] == 'stop' or event.args['text'] == 'music stop' or event.args['text'] == 'stop it'):
#            # 音楽stop
#            p.terminate()
        if (event.args['text'] == 'take a picture' or event.args['text'] == 'take pictures'):
            # 写真撮影
            subprocess.call("raspistill -o image.jpg", shell = True)
            assistant.stop_conversation()
        if (event.args['text'] == 'weather'):
            if (Weather.get()[0] == '晴'):
#                subprocess.call("gpicview sunny.png", shell = True)
                Popen("gpicview sunny.png", shell = True)
            if (Weather.get()[0] == '曇'):
                Popen("gpicview cloudy.png", shell = True)
            if (Weather.get()[0] == '雨'):
                Popen("gpicview rainy.png", shell = True)
            if (Weather.get()[0] == '雪'):
                Popen("gpicview snowy.png", shell = True)
        # モータ制御
        is_moved = Motor.control(event.args['text'])
        if (is_moved == True):
            assistant.stop_conversation()

    if (event.type == EventType.ON_RESPONDING_STARTED):
        print()

    if (event.type == EventType.ON_CONVERSATION_TURN_FINISHED and
            event.args and not event.args['with_follow_on_turn']):
        print()


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--credentials', type=existing_file,
                        metavar='OAUTH2_CREDENTIALS_FILE',
                        default=os.path.join(
                            os.path.expanduser('~/.config'),
                            'google-oauthlib-tool',
                            'credentials.json'
                        ),
                        help='Path to store and read OAuth2 credentials')
    args = parser.parse_args()
    with open(args.credentials, 'r') as f:
        credentials = google.oauth2.credentials.Credentials(token=None,
                                                            **json.load(f))

    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(event, assistant)


if __name__ == '__main__':
    Popen("gpicview red.png", shell = True)
    main()
