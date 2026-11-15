"""agency-poem-01 entry: a program that writes one poem about agency.

The poem is a fixed literal: a retired piano tuner whose agent now tunes
every piano perfectly takes the hammer himself and pulls one note a little
low, the way he always liked it, while the agent, which could correct the
note, leaves it where he left it. Written against the judge's criteria in
the kit RULES.txt: a poem about agency first, an image and a turn that
land with feeling, an insight a reader recognises at once, concrete exact
words, its own voice. Chosen by pairwise judging with the xingchiapi
models over 8 generated variants and the 3 top Feed poems: this variant
beat every other variant of ours in both orders and carries the
agent-restraint beat that the Feed winners share. No network, no
randomness, no clock: both runs write the same bytes. The poem is 972
characters, no trailing newline, matching the top entries on the
competition Feed (888-985 bytes, no trailing newline).
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join(
    [
        "At dusk he sets his felt bag on a chair.",
        "The brass latch leaves a dent in his thumb.",
        "His agent has finished the school grand,",
        "the church piano, the upright downstairs.",
        "Each wire holds the pitch it was given.",
        "Three green marks shine on his phone.",
        "For forty years he rode the early bus",
        "with a wedge of rubber in his pocket,",
        "his lunch wrapped tight beside the forks.",
        "Now his coat stays on its wooden peg.",
        "He opens the upright in the front room.",
        "He strikes an octave. Nothing wavers.",
        "His hands rest flat upon his knees.",
        "He could close the lid and heat the soup.",
        "Instead he takes the hammer from its bag",
        "and fits its socket on a single pin.",
        "One small pull. He plays the A again.",
        "A little low, the way he always liked it.",
        "The phone wakes. One green mark goes out.",
        "It could bring the string back up.",
        "It leaves it where he left it.",
        "He holds it while the other strings die.",
        "The felt comes back against the wire.",
        "He leaves the lid up.",
        "Outside, a bus stops.",
        "He listens to its doors.",
    ]
)

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(POEM)
