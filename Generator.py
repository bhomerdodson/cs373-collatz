#!/usr/bin/env python

import random

def generator () :
    for x in range(0, 1000):
        i = random.randrange(1, 1000000)
        j = random.randrange(1, 1000000)
        print i, j
            
        
        
generator()
