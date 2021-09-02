#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random, string

from locust import HttpUser, TaskSet, between

def index(l):
    l.client.get("/")

def ownersFind(l):
    l.client.get("/owners/find")

def ownersFindRandomLetter(l):
    l.client.get("/owners?lastName="+generateRandomLetter())

def vets(l):
    l.client.get("/vets.html")

def generateRandomLetter():
    randomLetter = random.choice(string.ascii_letters)
    return randomLetter

class UserBehavior(TaskSet):

    def on_start(self):
        index(self)

    tasks = {
        index: 1,
        ownersFind:1,
        ownersFindRandomLetter: 10,
        vets: 1
    }

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 10)
