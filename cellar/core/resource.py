# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from cellar import Model


class Resource(Model):
    def __init__(self, uuid=None, type=None, attributes=None,
                 foreign_tracking=None, relations=None):
        self.uuid = uuid
        self.type = type
        self.attributes = attributes or {}
        self.foreign_tracking = foreign_tracking or {}
        self.relations = relations or {}