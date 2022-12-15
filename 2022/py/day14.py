import sys
import math
from dataclasses import dataclass
from typing import Callable
import operator
import copy
from collections import defaultdict
from time import time

input="""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

input="""521,154 -> 526,154
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
499,13 -> 499,17 -> 493,17 -> 493,24 -> 507,24 -> 507,17 -> 501,17 -> 501,13
497,80 -> 497,83 -> 489,83 -> 489,87 -> 505,87 -> 505,83 -> 501,83 -> 501,80
471,77 -> 475,77
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
545,157 -> 545,160 -> 544,160 -> 544,167 -> 556,167 -> 556,160 -> 549,160 -> 549,157
477,73 -> 481,73
532,137 -> 537,137
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
513,142 -> 513,143 -> 528,143
497,80 -> 497,83 -> 489,83 -> 489,87 -> 505,87 -> 505,83 -> 501,83 -> 501,80
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
512,128 -> 526,128 -> 526,127
480,71 -> 484,71
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
497,80 -> 497,83 -> 489,83 -> 489,87 -> 505,87 -> 505,83 -> 501,83 -> 501,80
507,95 -> 507,96 -> 515,96 -> 515,95
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
514,154 -> 519,154
478,60 -> 478,62 -> 472,62 -> 472,66 -> 484,66 -> 484,62 -> 482,62 -> 482,60
528,134 -> 533,134
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
535,154 -> 540,154
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
515,140 -> 520,140
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
478,60 -> 478,62 -> 472,62 -> 472,66 -> 484,66 -> 484,62 -> 482,62 -> 482,60
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
497,80 -> 497,83 -> 489,83 -> 489,87 -> 505,87 -> 505,83 -> 501,83 -> 501,80
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
518,137 -> 523,137
490,31 -> 494,31
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
526,146 -> 531,146
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
487,29 -> 491,29
499,13 -> 499,17 -> 493,17 -> 493,24 -> 507,24 -> 507,17 -> 501,17 -> 501,13
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
478,60 -> 478,62 -> 472,62 -> 472,66 -> 484,66 -> 484,62 -> 482,62 -> 482,60
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
534,150 -> 539,150
536,140 -> 541,140
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
478,60 -> 478,62 -> 472,62 -> 472,66 -> 484,66 -> 484,62 -> 482,62 -> 482,60
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
528,154 -> 533,154
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
484,31 -> 488,31
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
507,95 -> 507,96 -> 515,96 -> 515,95
545,157 -> 545,160 -> 544,160 -> 544,167 -> 556,167 -> 556,160 -> 549,160 -> 549,157
512,128 -> 526,128 -> 526,127
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
545,157 -> 545,160 -> 544,160 -> 544,167 -> 556,167 -> 556,160 -> 549,160 -> 549,157
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
499,13 -> 499,17 -> 493,17 -> 493,24 -> 507,24 -> 507,17 -> 501,17 -> 501,13
525,137 -> 530,137
478,60 -> 478,62 -> 472,62 -> 472,66 -> 484,66 -> 484,62 -> 482,62 -> 482,60
497,80 -> 497,83 -> 489,83 -> 489,87 -> 505,87 -> 505,83 -> 501,83 -> 501,80
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
520,150 -> 525,150
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
486,71 -> 490,71
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
517,152 -> 522,152
489,73 -> 493,73
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
530,148 -> 535,148
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
538,152 -> 543,152
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
499,13 -> 499,17 -> 493,17 -> 493,24 -> 507,24 -> 507,17 -> 501,17 -> 501,13
513,142 -> 513,143 -> 528,143
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
524,131 -> 529,131
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
483,69 -> 487,69
474,75 -> 478,75
493,29 -> 497,29
527,150 -> 532,150
545,157 -> 545,160 -> 544,160 -> 544,167 -> 556,167 -> 556,160 -> 549,160 -> 549,157
499,13 -> 499,17 -> 493,17 -> 493,24 -> 507,24 -> 507,17 -> 501,17 -> 501,13
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
499,13 -> 499,17 -> 493,17 -> 493,24 -> 507,24 -> 507,17 -> 501,17 -> 501,13
489,77 -> 493,77
524,152 -> 529,152
496,89 -> 496,90 -> 509,90
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
521,134 -> 526,134
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
496,31 -> 500,31
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
490,27 -> 494,27
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
478,60 -> 478,62 -> 472,62 -> 472,66 -> 484,66 -> 484,62 -> 482,62 -> 482,60
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
545,157 -> 545,160 -> 544,160 -> 544,167 -> 556,167 -> 556,160 -> 549,160 -> 549,157
529,140 -> 534,140
545,157 -> 545,160 -> 544,160 -> 544,167 -> 556,167 -> 556,160 -> 549,160 -> 549,157
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
483,73 -> 487,73
523,148 -> 528,148
542,154 -> 547,154
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
480,75 -> 484,75
495,77 -> 499,77
478,60 -> 478,62 -> 472,62 -> 472,66 -> 484,66 -> 484,62 -> 482,62 -> 482,60
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
522,140 -> 527,140
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
496,89 -> 496,90 -> 509,90
492,75 -> 496,75
499,13 -> 499,17 -> 493,17 -> 493,24 -> 507,24 -> 507,17 -> 501,17 -> 501,13
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
507,95 -> 507,96 -> 515,96 -> 515,95
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
497,80 -> 497,83 -> 489,83 -> 489,87 -> 505,87 -> 505,83 -> 501,83 -> 501,80
477,77 -> 481,77
497,80 -> 497,83 -> 489,83 -> 489,87 -> 505,87 -> 505,83 -> 501,83 -> 501,80
486,75 -> 490,75
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
502,122 -> 502,115 -> 502,122 -> 504,122 -> 504,114 -> 504,122 -> 506,122 -> 506,115 -> 506,122 -> 508,122 -> 508,119 -> 508,122 -> 510,122 -> 510,113 -> 510,122 -> 512,122 -> 512,116 -> 512,122 -> 514,122 -> 514,115 -> 514,122 -> 516,122 -> 516,113 -> 516,122 -> 518,122 -> 518,117 -> 518,122
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
531,152 -> 536,152
545,157 -> 545,160 -> 544,160 -> 544,167 -> 556,167 -> 556,160 -> 549,160 -> 549,157
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109
483,77 -> 487,77
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
474,44 -> 474,38 -> 474,44 -> 476,44 -> 476,39 -> 476,44 -> 478,44 -> 478,34 -> 478,44 -> 480,44 -> 480,40 -> 480,44 -> 482,44 -> 482,36 -> 482,44 -> 484,44 -> 484,34 -> 484,44 -> 486,44 -> 486,38 -> 486,44 -> 488,44 -> 488,36 -> 488,44 -> 490,44 -> 490,36 -> 490,44
464,57 -> 464,49 -> 464,57 -> 466,57 -> 466,53 -> 466,57 -> 468,57 -> 468,54 -> 468,57 -> 470,57 -> 470,56 -> 470,57 -> 472,57 -> 472,47 -> 472,57 -> 474,57 -> 474,53 -> 474,57 -> 476,57 -> 476,51 -> 476,57 -> 478,57 -> 478,50 -> 478,57 -> 480,57 -> 480,55 -> 480,57
500,109 -> 500,100 -> 500,109 -> 502,109 -> 502,103 -> 502,109 -> 504,109 -> 504,106 -> 504,109 -> 506,109 -> 506,108 -> 506,109 -> 508,109 -> 508,108 -> 508,109 -> 510,109 -> 510,105 -> 510,109"""

@dataclass
class vec2:
    __slots__ = 'x', 'y'
    x: int
    y: int
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y

lines=input.split('\n')
lines=input.split('\n')
rocks_dict_y=defaultdict(set)
max_y=0
for line in lines:
    keys=[tuple(map(int, entry.split(','))) for entry in line.replace(' ','').split('->')]
    for ki in range(len(keys)):
        if (ki+1) < len(keys):
            if keys[ki][0]==keys[ki+1][0]:
                start,end=min(keys[ki][1], keys[ki+1][1]),max(keys[ki][1], keys[ki+1][1])
                for y in range(start, end+1):
                    rocks_dict_y[y].add(keys[ki][0])
                    max_y=y if y >max_y else max_y
            elif keys[ki][1]==keys[ki+1][1]:
                y=keys[ki][1]
                max_y=y if y>max_y else max_y
                start,end=min(keys[ki][0], keys[ki+1][0]),max(keys[ki][0], keys[ki+1][0])
                for x in range(start, end+1):
                    rocks_dict_y[y].add(x)

start_time=time()
start=vec2(500,0)
current=copy.deepcopy(start)
sands_dict_y=defaultdict(set)
while True:
    rested=True
    for dir in [(0,1),(-1,1),(1,1)]:
        newx=current.x+dir[0]
        newy=current.y+dir[1]
        if newx not in rocks_dict_y[newy] and newx not in sands_dict_y[newy]:
            current.x=newx
            current.y=newy
            rested=False
            break
    
    if rested:
        sands_dict_y[current.y].add(current.x)
        current=copy.deepcopy(start)# start again
    else:
        if newy > max_y:
            print(sum(len(v) for v in sands_dict_y.values()))
            break
print('elapsed',(time()-start_time))

#b
start_time=time()
max_y=max_y+1
start=vec2(500,0)
current=copy.deepcopy(start)
sands_dict_y=defaultdict(set)
while True:
    rested=True
    for dir in [(0,1),(-1,1),(1,1)]:
        newx=current.x+dir[0]
        newy=current.y+dir[1]
        if newx not in rocks_dict_y[newy] and newx not in sands_dict_y[newy]:
            current.x=newx
            current.y=newy
            rested=True if newy==max_y else False
            break
    
    if rested:
        if current==start:
            # end
            print(sum(len(v) for v in sands_dict_y.values()) + 1)
            break
        else:
            sands_dict_y[current.y].add(current.x)
            current=copy.deepcopy(start)# start again
print('elapsed',(time()-start_time))