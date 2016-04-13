#!/usr/bin/env python
#
# Copyright 2016 BMC Software, Inc.
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
#
import syslog
import random


class OneLiners(object):
    def __init__(self):
        self._one_liners = [
            "I wrote a few children's books... Not on purpose. - Steven Wright",
            "I looked up my family tree and found out I was the sap. - Rodney Dangerfield",
            "Any closet is a walk-in closet if you try hard enough. - Steven Wright",
            "I think it's wrong that only one company makes the game Monopoly. - Steven Wright",
            "I have a lot of growing up to do. I realized that the other day inside my fort. - Zach Galifianakis",
            "I never forget a face, but in your case I'd be glad to make an exception. - Groucho Marx",
            "Two cannibals were eating a clown - one said to the other, 'Does he taste funny to you?' - Tommy Cooper",
            "I like to play chess with old men in the park, although it's hard to find 32 of them. - Emo Phillips",
            "Room service? Send up a larger room. - Groucho Marx",
            "Toughest job I ever had: selling doors, door to door. - Bill Bailey",
            "How do you tell when you're out of invisible ink? - Steven Wright",
            "The quickest way to a man's heart is through his chest. - Roseanne Barr",
            "Men don't care what's on TV. They only care what else is on TV. - Jerry Seinfeld",
            "She said she was approaching forty, and I couldn't help wondering from what direction - Bob Hope",
            "Where there's a will - there's a relative! - Ricky Gervais",
            "Who discovered we could get milk from cows, and what did he think he was doing at the time? - Billy Connolly",
            "Did you hear about the shrimp that went to the prawn's cocktail party? He pulled a mussel. - Ken Dodd",
            "I needed a password eight characters long so I picked Snow White and the Seven Dwarves. - Nick Helm",
            "I'm so ugly. My father carries around the picture of the kid who came with his wallet. - Rodney Dangerfield",
            "Whoever said nothing is impossible obviously hasn't tried nailing jelly to a tree. - John Candy",
            "I have kleptomania. But when it gets bad, I take something for it. - Ken Dodd",
            "Age is an issue of mind over matter. If you don't mind, it doesn't matter. - Mark Twain",
            "Don't sweat the petty things and don't pet the sweaty things. - George Carlin",
            "Well, here's another nice mess you've gotten me into. - Oliver Hardy"
        ]

    def give_me_one(self):
        syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_USER)
        line = self._one_liners[random.randrange(0, len(self._one_liners))]
        print(line)
        syslog.syslog(line)


if __name__ == '__main__':
    one_liner = OneLiners()
    one_liner.give_me_one()
