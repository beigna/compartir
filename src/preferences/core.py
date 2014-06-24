#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xdg import BaseDirectory
import os
import json


class Data(object):
    def __init__(self, data):
        self.__dict__.update(data)


class Preferences(object):
    def __init__(self):
        self._app_path = BaseDirectory.save_config_path('compartir')
        self._file = os.path.join(self._app_path, 'preferences.json')

        self.compartir = None
        self.profile = None

        self._load()

    def _load(self):
        if not os.path.isfile(self._file):
            data = {
                'profile': {
                    'name': 'Alumno',
                    'description': '',
                },
                'compartir': {
                    'auto_start': True
                }
            }
            with open(self._file, 'w') as fd:
                fd.write(json.dumps(data))

        with open(self._file, 'r') as fd:
            _ = json.loads(fd.read())
            self.compartir = Data(_['compartir'])
            self.profile = Data(_['profile'])

    def save(self):
        data = {
            'compartir': self.compartir.__dict__,
            'profile': self.profile.__dict__
        }

        with open(self._file, 'w') as fd:
            fd.write(json.dumps(data))

