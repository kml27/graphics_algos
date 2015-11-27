from __future__ import division
import os, sys, math, random
import envelope

env = envelope.envelope()

duration=10
#delay
node = envelope.envelope_node(duration, 0, 0)
env.add_node((duration, 0))
#attack
node = envelope.envelope_node(duration, 10, 0)
env.add_node(node)
#decay
node = envelope.envelope_node(duration, 5, 10)
env.add_node(node)
#sustain
node = envelope.envelope_node(duration, 5, 5)
env.add_node(node)
#attack
node = envelope.envelope_node(duration, 10, 5)
env.add_node(node)
#decay
node = envelope.envelope_node(duration, 0, 10)
env.add_node(node)

print("total duration: " + str(env.get_duration()))

for i in range(-1, 61):
    try:
        time = i
        print("at time " + str(time) + " got interpolated value " + str(env.get_value(time)))
    except Exception as e:
        print(e.message)
    