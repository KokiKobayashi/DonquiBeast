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

import time



def process_event(event):
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
        if (event.args['text'] == 'play music' or event.args['text'] == 'play the music' or event.args['text'] == 'play Miracle shopping'):
            # 音楽再生
            subprocess.call("aplay shopping-short.wav", shell = True)
        if (event.args['text'] == 'take a picture' or event.args['text'] == 'take pictures'):
            # 写真撮影
            subprocess.call("raspistill -o image.jpg", shell = True)
        if (event.args['text'] == 'stop'):
            # モータ停止
            subprocess.call("./motor 0", shell = True)
        if (event.args['text'] == 'go forward' or event.args['text'] == 'forward' or event.args['text'] == 'front' ):
            # 前進
            subprocess.call("./motor 1", shell = True)
#            time.sleep(5)
#            subprocess.call("./motor 0", shell = True)
        if (event.args['text'] == 'go backward' or event.args['text'] == 'backward' or event.args['text'] == 'back'):
            # 後退
            subprocess.call("./motor 2", shell = True)
#            time.sleep(5)
#            subprocess.call("./motor 0", shell = True)
        if (event.args['text'] == 'turn left'):
            # 方向転換：左
            subprocess.call("./motor 3", shell = True)
            time.sleep(1)
            subprocess.call("./motor 0", shell = True)
        if (event.args['text'] == 'turn right'):
            # 方向転換：右
            subprocess.call("./motor 4", shell = True)
            time.sleep(1)
            subprocess.call("./motor 0", shell = True)

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
            process_event(event)


if __name__ == '__main__':
    main()
