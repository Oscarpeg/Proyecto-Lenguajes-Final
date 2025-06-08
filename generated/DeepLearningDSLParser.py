# Generated from grammar/DeepLearningDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,61,474,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,3,1,84,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,3,2,98,8,2,1,3,1,3,3,3,102,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,120,8,6,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,138,8,8,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,3,10,148,8,10,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,161,8,11,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,3,12,170,8,12,1,13,1,13,1,14,1,14,1,14,1,14,1,
        14,3,14,179,8,14,1,15,1,15,1,15,1,15,3,15,185,8,15,1,16,1,16,1,16,
        1,16,1,16,3,16,192,8,16,1,17,1,17,1,17,1,17,1,17,3,17,199,8,17,1,
        18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,3,19,209,8,19,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,3,20,242,8,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,3,22,259,8,22,1,23,1,23,1,
        23,1,23,1,23,3,23,266,8,23,1,24,1,24,1,25,1,25,3,25,272,8,25,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,1,28,1,29,1,29,1,29,3,29,307,8,29,1,30,1,30,1,30,1,30,
        3,30,313,8,30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,3,32,327,8,32,1,33,1,33,1,33,1,33,3,33,333,8,33,1,34,1,
        34,1,34,1,34,1,34,3,34,340,8,34,1,35,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,435,8,35,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,
        36,1,36,3,36,453,8,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,
        37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,3,37,472,8,37,1,37,0,
        0,38,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,0,2,1,0,31,34,1,
        0,42,47,491,0,76,1,0,0,0,2,83,1,0,0,0,4,97,1,0,0,0,6,101,1,0,0,0,
        8,103,1,0,0,0,10,107,1,0,0,0,12,119,1,0,0,0,14,121,1,0,0,0,16,137,
        1,0,0,0,18,139,1,0,0,0,20,147,1,0,0,0,22,160,1,0,0,0,24,169,1,0,
        0,0,26,171,1,0,0,0,28,178,1,0,0,0,30,184,1,0,0,0,32,191,1,0,0,0,
        34,198,1,0,0,0,36,200,1,0,0,0,38,208,1,0,0,0,40,241,1,0,0,0,42,243,
        1,0,0,0,44,258,1,0,0,0,46,265,1,0,0,0,48,267,1,0,0,0,50,271,1,0,
        0,0,52,273,1,0,0,0,54,285,1,0,0,0,56,293,1,0,0,0,58,306,1,0,0,0,
        60,312,1,0,0,0,62,314,1,0,0,0,64,326,1,0,0,0,66,332,1,0,0,0,68,339,
        1,0,0,0,70,434,1,0,0,0,72,452,1,0,0,0,74,471,1,0,0,0,76,77,3,2,1,
        0,77,78,5,0,0,1,78,1,1,0,0,0,79,80,3,4,2,0,80,81,3,2,1,0,81,84,1,
        0,0,0,82,84,1,0,0,0,83,79,1,0,0,0,83,82,1,0,0,0,84,3,1,0,0,0,85,
        86,3,8,4,0,86,87,3,6,3,0,87,98,1,0,0,0,88,98,3,42,21,0,89,98,3,50,
        25,0,90,98,3,56,28,0,91,92,3,64,32,0,92,93,3,6,3,0,93,98,1,0,0,0,
        94,95,3,10,5,0,95,96,3,6,3,0,96,98,1,0,0,0,97,85,1,0,0,0,97,88,1,
        0,0,0,97,89,1,0,0,0,97,90,1,0,0,0,97,91,1,0,0,0,97,94,1,0,0,0,98,
        5,1,0,0,0,99,102,5,55,0,0,100,102,1,0,0,0,101,99,1,0,0,0,101,100,
        1,0,0,0,102,7,1,0,0,0,103,104,5,59,0,0,104,105,5,35,0,0,105,106,
        3,10,5,0,106,9,1,0,0,0,107,108,3,14,7,0,108,109,3,12,6,0,109,11,
        1,0,0,0,110,111,5,36,0,0,111,112,3,14,7,0,112,113,3,12,6,0,113,120,
        1,0,0,0,114,115,5,37,0,0,115,116,3,14,7,0,116,117,3,12,6,0,117,120,
        1,0,0,0,118,120,1,0,0,0,119,110,1,0,0,0,119,114,1,0,0,0,119,118,
        1,0,0,0,120,13,1,0,0,0,121,122,3,18,9,0,122,123,3,16,8,0,123,15,
        1,0,0,0,124,125,5,38,0,0,125,126,3,18,9,0,126,127,3,16,8,0,127,138,
        1,0,0,0,128,129,5,39,0,0,129,130,3,18,9,0,130,131,3,16,8,0,131,138,
        1,0,0,0,132,133,5,40,0,0,133,134,3,18,9,0,134,135,3,16,8,0,135,138,
        1,0,0,0,136,138,1,0,0,0,137,124,1,0,0,0,137,128,1,0,0,0,137,132,
        1,0,0,0,137,136,1,0,0,0,138,17,1,0,0,0,139,140,3,22,11,0,140,141,
        3,20,10,0,141,19,1,0,0,0,142,143,5,41,0,0,143,144,3,22,11,0,144,
        145,3,20,10,0,145,148,1,0,0,0,146,148,1,0,0,0,147,142,1,0,0,0,147,
        146,1,0,0,0,148,21,1,0,0,0,149,161,3,64,32,0,150,161,5,59,0,0,151,
        161,5,56,0,0,152,161,5,57,0,0,153,161,5,58,0,0,154,155,5,48,0,0,
        155,156,3,10,5,0,156,157,5,49,0,0,157,161,1,0,0,0,158,161,3,28,14,
        0,159,161,3,24,12,0,160,149,1,0,0,0,160,150,1,0,0,0,160,151,1,0,
        0,0,160,152,1,0,0,0,160,153,1,0,0,0,160,154,1,0,0,0,160,158,1,0,
        0,0,160,159,1,0,0,0,161,23,1,0,0,0,162,163,5,37,0,0,163,170,3,22,
        11,0,164,165,3,26,13,0,165,166,5,48,0,0,166,167,3,10,5,0,167,168,
        5,49,0,0,168,170,1,0,0,0,169,162,1,0,0,0,169,164,1,0,0,0,170,25,
        1,0,0,0,171,172,7,0,0,0,172,27,1,0,0,0,173,174,5,52,0,0,174,175,
        3,30,15,0,175,176,5,53,0,0,176,179,1,0,0,0,177,179,3,40,20,0,178,
        173,1,0,0,0,178,177,1,0,0,0,179,29,1,0,0,0,180,181,3,34,17,0,181,
        182,3,32,16,0,182,185,1,0,0,0,183,185,1,0,0,0,184,180,1,0,0,0,184,
        183,1,0,0,0,185,31,1,0,0,0,186,187,5,54,0,0,187,188,3,34,17,0,188,
        189,3,32,16,0,189,192,1,0,0,0,190,192,1,0,0,0,191,186,1,0,0,0,191,
        190,1,0,0,0,192,33,1,0,0,0,193,194,5,52,0,0,194,195,3,36,18,0,195,
        196,5,53,0,0,196,199,1,0,0,0,197,199,3,10,5,0,198,193,1,0,0,0,198,
        197,1,0,0,0,199,35,1,0,0,0,200,201,3,10,5,0,201,202,3,38,19,0,202,
        37,1,0,0,0,203,204,5,54,0,0,204,205,3,10,5,0,205,206,3,38,19,0,206,
        209,1,0,0,0,207,209,1,0,0,0,208,203,1,0,0,0,208,207,1,0,0,0,209,
        39,1,0,0,0,210,211,5,20,0,0,211,212,5,48,0,0,212,213,3,10,5,0,213,
        214,5,49,0,0,214,242,1,0,0,0,215,216,5,21,0,0,216,217,5,48,0,0,217,
        218,3,10,5,0,218,219,5,49,0,0,219,242,1,0,0,0,220,221,5,22,0,0,221,
        222,5,48,0,0,222,223,3,10,5,0,223,224,5,54,0,0,224,225,3,10,5,0,
        225,226,5,49,0,0,226,242,1,0,0,0,227,228,5,23,0,0,228,229,5,48,0,
        0,229,230,3,10,5,0,230,231,5,54,0,0,231,232,3,10,5,0,232,233,5,49,
        0,0,233,242,1,0,0,0,234,235,5,24,0,0,235,236,5,48,0,0,236,237,3,
        10,5,0,237,238,5,54,0,0,238,239,3,10,5,0,239,240,5,49,0,0,240,242,
        1,0,0,0,241,210,1,0,0,0,241,215,1,0,0,0,241,220,1,0,0,0,241,227,
        1,0,0,0,241,234,1,0,0,0,242,41,1,0,0,0,243,244,5,1,0,0,244,245,5,
        48,0,0,245,246,3,46,23,0,246,247,5,49,0,0,247,248,5,50,0,0,248,249,
        3,2,1,0,249,250,5,51,0,0,250,251,3,44,22,0,251,43,1,0,0,0,252,253,
        5,2,0,0,253,254,5,50,0,0,254,255,3,2,1,0,255,256,5,51,0,0,256,259,
        1,0,0,0,257,259,1,0,0,0,258,252,1,0,0,0,258,257,1,0,0,0,259,45,1,
        0,0,0,260,261,3,10,5,0,261,262,3,48,24,0,262,263,3,10,5,0,263,266,
        1,0,0,0,264,266,3,10,5,0,265,260,1,0,0,0,265,264,1,0,0,0,266,47,
        1,0,0,0,267,268,7,1,0,0,268,49,1,0,0,0,269,272,3,52,26,0,270,272,
        3,54,27,0,271,269,1,0,0,0,271,270,1,0,0,0,272,51,1,0,0,0,273,274,
        5,3,0,0,274,275,5,48,0,0,275,276,3,8,4,0,276,277,3,6,3,0,277,278,
        3,46,23,0,278,279,3,6,3,0,279,280,3,8,4,0,280,281,5,49,0,0,281,282,
        5,50,0,0,282,283,3,2,1,0,283,284,5,51,0,0,284,53,1,0,0,0,285,286,
        5,4,0,0,286,287,5,48,0,0,287,288,3,46,23,0,288,289,5,49,0,0,289,
        290,5,50,0,0,290,291,3,2,1,0,291,292,5,51,0,0,292,55,1,0,0,0,293,
        294,5,5,0,0,294,295,5,59,0,0,295,296,5,48,0,0,296,297,3,58,29,0,
        297,298,5,49,0,0,298,299,5,50,0,0,299,300,3,2,1,0,300,301,3,62,31,
        0,301,302,5,51,0,0,302,57,1,0,0,0,303,304,5,59,0,0,304,307,3,60,
        30,0,305,307,1,0,0,0,306,303,1,0,0,0,306,305,1,0,0,0,307,59,1,0,
        0,0,308,309,5,54,0,0,309,310,5,59,0,0,310,313,3,60,30,0,311,313,
        1,0,0,0,312,308,1,0,0,0,312,311,1,0,0,0,313,61,1,0,0,0,314,315,5,
        6,0,0,315,316,3,10,5,0,316,317,3,6,3,0,317,63,1,0,0,0,318,319,5,
        59,0,0,319,320,5,48,0,0,320,321,3,66,33,0,321,322,5,49,0,0,322,327,
        1,0,0,0,323,327,3,70,35,0,324,327,3,72,36,0,325,327,3,74,37,0,326,
        318,1,0,0,0,326,323,1,0,0,0,326,324,1,0,0,0,326,325,1,0,0,0,327,
        65,1,0,0,0,328,329,3,10,5,0,329,330,3,68,34,0,330,333,1,0,0,0,331,
        333,1,0,0,0,332,328,1,0,0,0,332,331,1,0,0,0,333,67,1,0,0,0,334,335,
        5,54,0,0,335,336,3,10,5,0,336,337,3,68,34,0,337,340,1,0,0,0,338,
        340,1,0,0,0,339,334,1,0,0,0,339,338,1,0,0,0,340,69,1,0,0,0,341,342,
        5,7,0,0,342,343,5,48,0,0,343,344,3,10,5,0,344,345,5,54,0,0,345,346,
        3,10,5,0,346,347,5,49,0,0,347,435,1,0,0,0,348,349,5,8,0,0,349,350,
        5,48,0,0,350,351,3,10,5,0,351,352,5,54,0,0,352,353,3,10,5,0,353,
        354,5,54,0,0,354,355,3,10,5,0,355,356,5,49,0,0,356,435,1,0,0,0,357,
        358,5,9,0,0,358,359,5,48,0,0,359,360,3,10,5,0,360,361,5,54,0,0,361,
        362,3,10,5,0,362,363,5,54,0,0,363,364,3,10,5,0,364,365,5,49,0,0,
        365,435,1,0,0,0,366,367,5,10,0,0,367,368,5,48,0,0,368,369,3,10,5,
        0,369,370,5,54,0,0,370,371,3,10,5,0,371,372,5,49,0,0,372,435,1,0,
        0,0,373,374,5,11,0,0,374,375,5,48,0,0,375,376,3,10,5,0,376,377,5,
        54,0,0,377,378,3,10,5,0,378,379,5,49,0,0,379,435,1,0,0,0,380,381,
        5,12,0,0,381,382,5,48,0,0,382,383,3,10,5,0,383,384,5,54,0,0,384,
        385,3,10,5,0,385,386,5,49,0,0,386,435,1,0,0,0,387,388,5,13,0,0,388,
        389,5,48,0,0,389,390,3,10,5,0,390,391,5,54,0,0,391,392,3,10,5,0,
        392,393,5,49,0,0,393,435,1,0,0,0,394,395,5,14,0,0,395,396,5,48,0,
        0,396,397,3,10,5,0,397,398,5,49,0,0,398,435,1,0,0,0,399,400,5,15,
        0,0,400,401,5,48,0,0,401,402,3,10,5,0,402,403,5,54,0,0,403,404,3,
        10,5,0,404,405,5,49,0,0,405,435,1,0,0,0,406,407,5,16,0,0,407,408,
        5,48,0,0,408,409,3,10,5,0,409,410,5,54,0,0,410,411,3,10,5,0,411,
        412,5,49,0,0,412,435,1,0,0,0,413,414,5,17,0,0,414,415,5,48,0,0,415,
        416,3,10,5,0,416,417,5,54,0,0,417,418,3,10,5,0,418,419,5,49,0,0,
        419,435,1,0,0,0,420,421,5,18,0,0,421,422,5,48,0,0,422,423,3,10,5,
        0,423,424,5,54,0,0,424,425,3,10,5,0,425,426,5,49,0,0,426,435,1,0,
        0,0,427,428,5,19,0,0,428,429,5,48,0,0,429,430,3,10,5,0,430,431,5,
        54,0,0,431,432,3,10,5,0,432,433,5,49,0,0,433,435,1,0,0,0,434,341,
        1,0,0,0,434,348,1,0,0,0,434,357,1,0,0,0,434,366,1,0,0,0,434,373,
        1,0,0,0,434,380,1,0,0,0,434,387,1,0,0,0,434,394,1,0,0,0,434,399,
        1,0,0,0,434,406,1,0,0,0,434,413,1,0,0,0,434,420,1,0,0,0,434,427,
        1,0,0,0,435,71,1,0,0,0,436,437,5,25,0,0,437,438,5,48,0,0,438,439,
        5,58,0,0,439,453,5,49,0,0,440,441,5,26,0,0,441,442,5,48,0,0,442,
        443,5,58,0,0,443,444,5,54,0,0,444,445,3,10,5,0,445,446,5,49,0,0,
        446,453,1,0,0,0,447,448,5,27,0,0,448,449,5,48,0,0,449,450,3,10,5,
        0,450,451,5,49,0,0,451,453,1,0,0,0,452,436,1,0,0,0,452,440,1,0,0,
        0,452,447,1,0,0,0,453,73,1,0,0,0,454,455,5,28,0,0,455,456,5,48,0,
        0,456,457,3,10,5,0,457,458,5,49,0,0,458,472,1,0,0,0,459,460,5,29,
        0,0,460,461,5,48,0,0,461,462,3,10,5,0,462,463,5,54,0,0,463,464,3,
        10,5,0,464,465,5,49,0,0,465,472,1,0,0,0,466,467,5,30,0,0,467,468,
        5,48,0,0,468,469,3,10,5,0,469,470,5,49,0,0,470,472,1,0,0,0,471,454,
        1,0,0,0,471,459,1,0,0,0,471,466,1,0,0,0,472,75,1,0,0,0,25,83,97,
        101,119,137,147,160,169,178,184,191,198,208,241,258,265,271,306,
        312,326,332,339,434,452,471
    ]

class DeepLearningDSLParser ( Parser ):

    grammarFileName = "DeepLearningDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'while'", 
                     "'def'", "'return'", "'linear_regression'", "'mlp_classifier'", 
                     "'neural_network'", "'predict'", "'train'", "'kmeans'", 
                     "'fit_predict'", "'get_centroids'", "'autoencoder'", 
                     "'encode'", "'decode'", "'reconstruct'", "'reconstruction_error'", 
                     "'transpose'", "'inverse'", "'matmult'", "'matadd'", 
                     "'matsub'", "'read_file'", "'write_file'", "'print'", 
                     "'plot'", "'scatter'", "'histogram'", "'sin'", "'cos'", 
                     "'tan'", "'sqrt'", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'^'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "WHILE", "DEF", 
                      "RETURN", "LINEAR_REGRESSION", "MLP_CLASSIFIER", "NEURAL_NETWORK", 
                      "PREDICT", "TRAIN", "KMEANS", "FIT_PREDICT", "GET_CENTROIDS", 
                      "AUTOENCODER", "ENCODE", "DECODE", "RECONSTRUCT", 
                      "RECONSTRUCTION_ERROR", "TRANSPOSE", "INVERSE", "MATMULT", 
                      "MATADD", "MATSUB", "READ_FILE", "WRITE_FILE", "PRINT", 
                      "PLOT", "SCATTER", "HISTOGRAM", "SIN", "COS", "TAN", 
                      "SQRT", "ASSIGN", "PLUS", "MINUS", "MULT", "DIV", 
                      "MOD", "POWER", "EQ", "NE", "LT", "LE", "GT", "GE", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACKET", 
                      "RBRACKET", "COMMA", "SEMICOLON", "NUMBER", "FLOAT", 
                      "STRING", "ID", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement_list = 1
    RULE_statement = 2
    RULE_semicolon_opt = 3
    RULE_assignment = 4
    RULE_expression = 5
    RULE_expr_rest = 6
    RULE_term = 7
    RULE_term_rest = 8
    RULE_factor = 9
    RULE_factor_rest = 10
    RULE_base = 11
    RULE_unary_expr = 12
    RULE_trig_func = 13
    RULE_list_or_matrix_expr = 14
    RULE_list_or_matrix_content = 15
    RULE_list_or_matrix_content_rest = 16
    RULE_list_or_matrix_row = 17
    RULE_expression_list = 18
    RULE_expression_list_rest = 19
    RULE_matrix_operation = 20
    RULE_conditional = 21
    RULE_else_part = 22
    RULE_condition = 23
    RULE_rel_op = 24
    RULE_loop = 25
    RULE_for_loop = 26
    RULE_while_loop = 27
    RULE_function_def = 28
    RULE_param_list = 29
    RULE_param_list_rest = 30
    RULE_return_stmt = 31
    RULE_function_call = 32
    RULE_arg_list = 33
    RULE_arg_list_rest = 34
    RULE_ml_function = 35
    RULE_io_function = 36
    RULE_plot_function = 37

    ruleNames =  [ "program", "statement_list", "statement", "semicolon_opt", 
                   "assignment", "expression", "expr_rest", "term", "term_rest", 
                   "factor", "factor_rest", "base", "unary_expr", "trig_func", 
                   "list_or_matrix_expr", "list_or_matrix_content", "list_or_matrix_content_rest", 
                   "list_or_matrix_row", "expression_list", "expression_list_rest", 
                   "matrix_operation", "conditional", "else_part", "condition", 
                   "rel_op", "loop", "for_loop", "while_loop", "function_def", 
                   "param_list", "param_list_rest", "return_stmt", "function_call", 
                   "arg_list", "arg_list_rest", "ml_function", "io_function", 
                   "plot_function" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    WHILE=4
    DEF=5
    RETURN=6
    LINEAR_REGRESSION=7
    MLP_CLASSIFIER=8
    NEURAL_NETWORK=9
    PREDICT=10
    TRAIN=11
    KMEANS=12
    FIT_PREDICT=13
    GET_CENTROIDS=14
    AUTOENCODER=15
    ENCODE=16
    DECODE=17
    RECONSTRUCT=18
    RECONSTRUCTION_ERROR=19
    TRANSPOSE=20
    INVERSE=21
    MATMULT=22
    MATADD=23
    MATSUB=24
    READ_FILE=25
    WRITE_FILE=26
    PRINT=27
    PLOT=28
    SCATTER=29
    HISTOGRAM=30
    SIN=31
    COS=32
    TAN=33
    SQRT=34
    ASSIGN=35
    PLUS=36
    MINUS=37
    MULT=38
    DIV=39
    MOD=40
    POWER=41
    EQ=42
    NE=43
    LT=44
    LE=45
    GT=46
    GE=47
    LPAREN=48
    RPAREN=49
    LBRACE=50
    RBRACE=51
    LBRACKET=52
    RBRACKET=53
    COMMA=54
    SEMICOLON=55
    NUMBER=56
    FLOAT=57
    STRING=58
    ID=59
    WS=60
    COMMENT=61

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def EOF(self):
            return self.getToken(DeepLearningDSLParser.EOF, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = DeepLearningDSLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.statement_list()
            self.state = 77
            self.match(DeepLearningDSLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.StatementContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_statement_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement_list" ):
                listener.enterStatement_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement_list" ):
                listener.exitStatement_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = DeepLearningDSLParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement_list)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 48, 52, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.statement()
                self.state = 80
                self.statement_list()
                pass
            elif token in [-1, 6, 51]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.AssignmentContext,0)


        def semicolon_opt(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Semicolon_optContext,0)


        def conditional(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ConditionalContext,0)


        def loop(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.LoopContext,0)


        def function_def(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Function_defContext,0)


        def function_call(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Function_callContext,0)


        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = DeepLearningDSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.assignment()
                self.state = 86
                self.semicolon_opt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.conditional()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.loop()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.function_def()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.function_call()
                self.state = 92
                self.semicolon_opt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 94
                self.expression()
                self.state = 95
                self.semicolon_opt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Semicolon_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(DeepLearningDSLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_semicolon_opt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSemicolon_opt" ):
                listener.enterSemicolon_opt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSemicolon_opt" ):
                listener.exitSemicolon_opt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSemicolon_opt" ):
                return visitor.visitSemicolon_opt(self)
            else:
                return visitor.visitChildren(self)




    def semicolon_opt(self):

        localctx = DeepLearningDSLParser.Semicolon_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_semicolon_opt)
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.match(DeepLearningDSLParser.SEMICOLON)
                pass
            elif token in [-1, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 48, 51, 52, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLearningDSLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(DeepLearningDSLParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = DeepLearningDSLParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(DeepLearningDSLParser.ID)
            self.state = 104
            self.match(DeepLearningDSLParser.ASSIGN)
            self.state = 105
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.TermContext,0)


        def expr_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Expr_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = DeepLearningDSLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.term()
            self.state = 108
            self.expr_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(DeepLearningDSLParser.PLUS, 0)

        def term(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.TermContext,0)


        def expr_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Expr_restContext,0)


        def MINUS(self):
            return self.getToken(DeepLearningDSLParser.MINUS, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_expr_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_rest" ):
                listener.enterExpr_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_rest" ):
                listener.exitExpr_rest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_rest" ):
                return visitor.visitExpr_rest(self)
            else:
                return visitor.visitChildren(self)




    def expr_rest(self):

        localctx = DeepLearningDSLParser.Expr_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr_rest)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(DeepLearningDSLParser.PLUS)
                self.state = 111
                self.term()
                self.state = 112
                self.expr_rest()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.match(DeepLearningDSLParser.MINUS)
                self.state = 115
                self.term()
                self.state = 116
                self.expr_rest()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.FactorContext,0)


        def term_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Term_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = DeepLearningDSLParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.factor()
            self.state = 122
            self.term_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Term_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(DeepLearningDSLParser.MULT, 0)

        def factor(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.FactorContext,0)


        def term_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Term_restContext,0)


        def DIV(self):
            return self.getToken(DeepLearningDSLParser.DIV, 0)

        def MOD(self):
            return self.getToken(DeepLearningDSLParser.MOD, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_term_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_rest" ):
                listener.enterTerm_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_rest" ):
                listener.exitTerm_rest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_rest" ):
                return visitor.visitTerm_rest(self)
            else:
                return visitor.visitChildren(self)




    def term_rest(self):

        localctx = DeepLearningDSLParser.Term_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_term_rest)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(DeepLearningDSLParser.MULT)
                self.state = 125
                self.factor()
                self.state = 126
                self.term_rest()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.match(DeepLearningDSLParser.DIV)
                self.state = 129
                self.factor()
                self.state = 130
                self.term_rest()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.match(DeepLearningDSLParser.MOD)
                self.state = 133
                self.factor()
                self.state = 134
                self.term_rest()
                pass
            elif token in [-1, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 4)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def base(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.BaseContext,0)


        def factor_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Factor_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = DeepLearningDSLParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.base()
            self.state = 140
            self.factor_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Factor_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POWER(self):
            return self.getToken(DeepLearningDSLParser.POWER, 0)

        def base(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.BaseContext,0)


        def factor_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Factor_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_factor_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_rest" ):
                listener.enterFactor_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_rest" ):
                listener.exitFactor_rest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_rest" ):
                return visitor.visitFactor_rest(self)
            else:
                return visitor.visitChildren(self)




    def factor_rest(self):

        localctx = DeepLearningDSLParser.Factor_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_factor_rest)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(DeepLearningDSLParser.POWER)
                self.state = 143
                self.base()
                self.state = 144
                self.factor_rest()
                pass
            elif token in [-1, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Function_callContext,0)


        def ID(self):
            return self.getToken(DeepLearningDSLParser.ID, 0)

        def NUMBER(self):
            return self.getToken(DeepLearningDSLParser.NUMBER, 0)

        def FLOAT(self):
            return self.getToken(DeepLearningDSLParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(DeepLearningDSLParser.STRING, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def list_or_matrix_expr(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.List_or_matrix_exprContext,0)


        def unary_expr(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Unary_exprContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBase" ):
                listener.enterBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBase" ):
                listener.exitBase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBase" ):
                return visitor.visitBase(self)
            else:
                return visitor.visitChildren(self)




    def base(self):

        localctx = DeepLearningDSLParser.BaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_base)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(DeepLearningDSLParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.match(DeepLearningDSLParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 152
                self.match(DeepLearningDSLParser.FLOAT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 153
                self.match(DeepLearningDSLParser.STRING)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 154
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 155
                self.expression()
                self.state = 156
                self.match(DeepLearningDSLParser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 158
                self.list_or_matrix_expr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 159
                self.unary_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(DeepLearningDSLParser.MINUS, 0)

        def base(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.BaseContext,0)


        def trig_func(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Trig_funcContext,0)


        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_unary_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_expr" ):
                listener.enterUnary_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_expr" ):
                listener.exitUnary_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expr" ):
                return visitor.visitUnary_expr(self)
            else:
                return visitor.visitChildren(self)




    def unary_expr(self):

        localctx = DeepLearningDSLParser.Unary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_unary_expr)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(DeepLearningDSLParser.MINUS)
                self.state = 163
                self.base()
                pass
            elif token in [31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.trig_func()
                self.state = 165
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 166
                self.expression()
                self.state = 167
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Trig_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIN(self):
            return self.getToken(DeepLearningDSLParser.SIN, 0)

        def COS(self):
            return self.getToken(DeepLearningDSLParser.COS, 0)

        def TAN(self):
            return self.getToken(DeepLearningDSLParser.TAN, 0)

        def SQRT(self):
            return self.getToken(DeepLearningDSLParser.SQRT, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_trig_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrig_func" ):
                listener.enterTrig_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrig_func" ):
                listener.exitTrig_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrig_func" ):
                return visitor.visitTrig_func(self)
            else:
                return visitor.visitChildren(self)




    def trig_func(self):

        localctx = DeepLearningDSLParser.Trig_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_trig_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_or_matrix_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(DeepLearningDSLParser.LBRACKET, 0)

        def list_or_matrix_content(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.List_or_matrix_contentContext,0)


        def RBRACKET(self):
            return self.getToken(DeepLearningDSLParser.RBRACKET, 0)

        def matrix_operation(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Matrix_operationContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_list_or_matrix_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_or_matrix_expr" ):
                listener.enterList_or_matrix_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_or_matrix_expr" ):
                listener.exitList_or_matrix_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_or_matrix_expr" ):
                return visitor.visitList_or_matrix_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_or_matrix_expr(self):

        localctx = DeepLearningDSLParser.List_or_matrix_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_or_matrix_expr)
        try:
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.match(DeepLearningDSLParser.LBRACKET)
                self.state = 174
                self.list_or_matrix_content()
                self.state = 175
                self.match(DeepLearningDSLParser.RBRACKET)
                pass
            elif token in [20, 21, 22, 23, 24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.matrix_operation()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_or_matrix_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_or_matrix_row(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.List_or_matrix_rowContext,0)


        def list_or_matrix_content_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.List_or_matrix_content_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_list_or_matrix_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_or_matrix_content" ):
                listener.enterList_or_matrix_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_or_matrix_content" ):
                listener.exitList_or_matrix_content(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_or_matrix_content" ):
                return visitor.visitList_or_matrix_content(self)
            else:
                return visitor.visitChildren(self)




    def list_or_matrix_content(self):

        localctx = DeepLearningDSLParser.List_or_matrix_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_or_matrix_content)
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 48, 52, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.list_or_matrix_row()
                self.state = 181
                self.list_or_matrix_content_rest()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_or_matrix_content_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def list_or_matrix_row(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.List_or_matrix_rowContext,0)


        def list_or_matrix_content_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.List_or_matrix_content_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_list_or_matrix_content_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_or_matrix_content_rest" ):
                listener.enterList_or_matrix_content_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_or_matrix_content_rest" ):
                listener.exitList_or_matrix_content_rest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_or_matrix_content_rest" ):
                return visitor.visitList_or_matrix_content_rest(self)
            else:
                return visitor.visitChildren(self)




    def list_or_matrix_content_rest(self):

        localctx = DeepLearningDSLParser.List_or_matrix_content_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_or_matrix_content_rest)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 187
                self.list_or_matrix_row()
                self.state = 188
                self.list_or_matrix_content_rest()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_or_matrix_rowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(DeepLearningDSLParser.LBRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Expression_listContext,0)


        def RBRACKET(self):
            return self.getToken(DeepLearningDSLParser.RBRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_list_or_matrix_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_or_matrix_row" ):
                listener.enterList_or_matrix_row(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_or_matrix_row" ):
                listener.exitList_or_matrix_row(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_or_matrix_row" ):
                return visitor.visitList_or_matrix_row(self)
            else:
                return visitor.visitChildren(self)




    def list_or_matrix_row(self):

        localctx = DeepLearningDSLParser.List_or_matrix_rowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_list_or_matrix_row)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.match(DeepLearningDSLParser.LBRACKET)
                self.state = 194
                self.expression_list()
                self.state = 195
                self.match(DeepLearningDSLParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def expression_list_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Expression_list_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_expression_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list" ):
                listener.enterExpression_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list" ):
                listener.exitExpression_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = DeepLearningDSLParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expression_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.expression()
            self.state = 201
            self.expression_list_rest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_list_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def expression_list_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Expression_list_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_expression_list_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression_list_rest" ):
                listener.enterExpression_list_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression_list_rest" ):
                listener.exitExpression_list_rest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list_rest" ):
                return visitor.visitExpression_list_rest(self)
            else:
                return visitor.visitChildren(self)




    def expression_list_rest(self):

        localctx = DeepLearningDSLParser.Expression_list_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expression_list_rest)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 204
                self.expression()
                self.state = 205
                self.expression_list_rest()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Matrix_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRANSPOSE(self):
            return self.getToken(DeepLearningDSLParser.TRANSPOSE, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLearningDSLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def INVERSE(self):
            return self.getToken(DeepLearningDSLParser.INVERSE, 0)

        def MATMULT(self):
            return self.getToken(DeepLearningDSLParser.MATMULT, 0)

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def MATADD(self):
            return self.getToken(DeepLearningDSLParser.MATADD, 0)

        def MATSUB(self):
            return self.getToken(DeepLearningDSLParser.MATSUB, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_matrix_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrix_operation" ):
                listener.enterMatrix_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrix_operation" ):
                listener.exitMatrix_operation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrix_operation" ):
                return visitor.visitMatrix_operation(self)
            else:
                return visitor.visitChildren(self)




    def matrix_operation(self):

        localctx = DeepLearningDSLParser.Matrix_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_matrix_operation)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(DeepLearningDSLParser.TRANSPOSE)
                self.state = 211
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 212
                self.expression()
                self.state = 213
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(DeepLearningDSLParser.INVERSE)
                self.state = 216
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 217
                self.expression()
                self.state = 218
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.match(DeepLearningDSLParser.MATMULT)
                self.state = 221
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 222
                self.expression()
                self.state = 223
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 224
                self.expression()
                self.state = 225
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 227
                self.match(DeepLearningDSLParser.MATADD)
                self.state = 228
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 229
                self.expression()
                self.state = 230
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 231
                self.expression()
                self.state = 232
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 234
                self.match(DeepLearningDSLParser.MATSUB)
                self.state = 235
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 236
                self.expression()
                self.state = 237
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 238
                self.expression()
                self.state = 239
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(DeepLearningDSLParser.IF, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(DeepLearningDSLParser.LBRACE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def RBRACE(self):
            return self.getToken(DeepLearningDSLParser.RBRACE, 0)

        def else_part(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Else_partContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = DeepLearningDSLParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(DeepLearningDSLParser.IF)
            self.state = 244
            self.match(DeepLearningDSLParser.LPAREN)
            self.state = 245
            self.condition()
            self.state = 246
            self.match(DeepLearningDSLParser.RPAREN)
            self.state = 247
            self.match(DeepLearningDSLParser.LBRACE)
            self.state = 248
            self.statement_list()
            self.state = 249
            self.match(DeepLearningDSLParser.RBRACE)
            self.state = 250
            self.else_part()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(DeepLearningDSLParser.ELSE, 0)

        def LBRACE(self):
            return self.getToken(DeepLearningDSLParser.LBRACE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def RBRACE(self):
            return self.getToken(DeepLearningDSLParser.RBRACE, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_else_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_part" ):
                listener.enterElse_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_part" ):
                listener.exitElse_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = DeepLearningDSLParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_else_part)
        try:
            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(DeepLearningDSLParser.ELSE)
                self.state = 253
                self.match(DeepLearningDSLParser.LBRACE)
                self.state = 254
                self.statement_list()
                self.state = 255
                self.match(DeepLearningDSLParser.RBRACE)
                pass
            elif token in [-1, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 48, 51, 52, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLearningDSLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,i)


        def rel_op(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Rel_opContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = DeepLearningDSLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_condition)
        try:
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.expression()
                self.state = 261
                self.rel_op()
                self.state = 262
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rel_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(DeepLearningDSLParser.EQ, 0)

        def NE(self):
            return self.getToken(DeepLearningDSLParser.NE, 0)

        def LT(self):
            return self.getToken(DeepLearningDSLParser.LT, 0)

        def LE(self):
            return self.getToken(DeepLearningDSLParser.LE, 0)

        def GT(self):
            return self.getToken(DeepLearningDSLParser.GT, 0)

        def GE(self):
            return self.getToken(DeepLearningDSLParser.GE, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_rel_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRel_op" ):
                listener.enterRel_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRel_op" ):
                listener.exitRel_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRel_op" ):
                return visitor.visitRel_op(self)
            else:
                return visitor.visitChildren(self)




    def rel_op(self):

        localctx = DeepLearningDSLParser.Rel_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_rel_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 277076930199552) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def for_loop(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.For_loopContext,0)


        def while_loop(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.While_loopContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = DeepLearningDSLParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_loop)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.for_loop()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.while_loop()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(DeepLearningDSLParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLearningDSLParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(DeepLearningDSLParser.AssignmentContext,i)


        def semicolon_opt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLearningDSLParser.Semicolon_optContext)
            else:
                return self.getTypedRuleContext(DeepLearningDSLParser.Semicolon_optContext,i)


        def condition(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(DeepLearningDSLParser.LBRACE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def RBRACE(self):
            return self.getToken(DeepLearningDSLParser.RBRACE, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_for_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_loop" ):
                listener.enterFor_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_loop" ):
                listener.exitFor_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = DeepLearningDSLParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(DeepLearningDSLParser.FOR)
            self.state = 274
            self.match(DeepLearningDSLParser.LPAREN)
            self.state = 275
            self.assignment()
            self.state = 276
            self.semicolon_opt()
            self.state = 277
            self.condition()
            self.state = 278
            self.semicolon_opt()
            self.state = 279
            self.assignment()
            self.state = 280
            self.match(DeepLearningDSLParser.RPAREN)
            self.state = 281
            self.match(DeepLearningDSLParser.LBRACE)
            self.state = 282
            self.statement_list()
            self.state = 283
            self.match(DeepLearningDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(DeepLearningDSLParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(DeepLearningDSLParser.LBRACE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def RBRACE(self):
            return self.getToken(DeepLearningDSLParser.RBRACE, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_while_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_loop" ):
                listener.enterWhile_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_loop" ):
                listener.exitWhile_loop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_loop" ):
                return visitor.visitWhile_loop(self)
            else:
                return visitor.visitChildren(self)




    def while_loop(self):

        localctx = DeepLearningDSLParser.While_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_while_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(DeepLearningDSLParser.WHILE)
            self.state = 286
            self.match(DeepLearningDSLParser.LPAREN)
            self.state = 287
            self.condition()
            self.state = 288
            self.match(DeepLearningDSLParser.RPAREN)
            self.state = 289
            self.match(DeepLearningDSLParser.LBRACE)
            self.state = 290
            self.statement_list()
            self.state = 291
            self.match(DeepLearningDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(DeepLearningDSLParser.DEF, 0)

        def ID(self):
            return self.getToken(DeepLearningDSLParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def param_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Param_listContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(DeepLearningDSLParser.LBRACE, 0)

        def statement_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Statement_listContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Return_stmtContext,0)


        def RBRACE(self):
            return self.getToken(DeepLearningDSLParser.RBRACE, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_function_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_def" ):
                listener.enterFunction_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_def" ):
                listener.exitFunction_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_def" ):
                return visitor.visitFunction_def(self)
            else:
                return visitor.visitChildren(self)




    def function_def(self):

        localctx = DeepLearningDSLParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_function_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(DeepLearningDSLParser.DEF)
            self.state = 294
            self.match(DeepLearningDSLParser.ID)
            self.state = 295
            self.match(DeepLearningDSLParser.LPAREN)
            self.state = 296
            self.param_list()
            self.state = 297
            self.match(DeepLearningDSLParser.RPAREN)
            self.state = 298
            self.match(DeepLearningDSLParser.LBRACE)
            self.state = 299
            self.statement_list()
            self.state = 300
            self.return_stmt()
            self.state = 301
            self.match(DeepLearningDSLParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLearningDSLParser.ID, 0)

        def param_list_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Param_list_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = DeepLearningDSLParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_param_list)
        try:
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(DeepLearningDSLParser.ID)
                self.state = 304
                self.param_list_rest()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_list_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def ID(self):
            return self.getToken(DeepLearningDSLParser.ID, 0)

        def param_list_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Param_list_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_param_list_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list_rest" ):
                listener.enterParam_list_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list_rest" ):
                listener.exitParam_list_rest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list_rest" ):
                return visitor.visitParam_list_rest(self)
            else:
                return visitor.visitChildren(self)




    def param_list_rest(self):

        localctx = DeepLearningDSLParser.Param_list_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_param_list_rest)
        try:
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 309
                self.match(DeepLearningDSLParser.ID)
                self.state = 310
                self.param_list_rest()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(DeepLearningDSLParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def semicolon_opt(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Semicolon_optContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = DeepLearningDSLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(DeepLearningDSLParser.RETURN)
            self.state = 315
            self.expression()
            self.state = 316
            self.semicolon_opt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DeepLearningDSLParser.ID, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def arg_list(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Arg_listContext,0)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def ml_function(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Ml_functionContext,0)


        def io_function(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Io_functionContext,0)


        def plot_function(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Plot_functionContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = DeepLearningDSLParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_function_call)
        try:
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(DeepLearningDSLParser.ID)
                self.state = 319
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 320
                self.arg_list()
                self.state = 321
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.ml_function()
                pass
            elif token in [25, 26, 27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 324
                self.io_function()
                pass
            elif token in [28, 29, 30]:
                self.enterOuterAlt(localctx, 4)
                self.state = 325
                self.plot_function()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def arg_list_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Arg_list_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = DeepLearningDSLParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_arg_list)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 48, 52, 56, 57, 58, 59]:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.expression()
                self.state = 329
                self.arg_list_rest()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_list_restContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def arg_list_rest(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.Arg_list_restContext,0)


        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_arg_list_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list_rest" ):
                listener.enterArg_list_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list_rest" ):
                listener.exitArg_list_rest(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list_rest" ):
                return visitor.visitArg_list_rest(self)
            else:
                return visitor.visitChildren(self)




    def arg_list_rest(self):

        localctx = DeepLearningDSLParser.Arg_list_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_arg_list_rest)
        try:
            self.state = 339
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 335
                self.expression()
                self.state = 336
                self.arg_list_rest()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ml_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINEAR_REGRESSION(self):
            return self.getToken(DeepLearningDSLParser.LINEAR_REGRESSION, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLearningDSLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(DeepLearningDSLParser.COMMA)
            else:
                return self.getToken(DeepLearningDSLParser.COMMA, i)

        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def MLP_CLASSIFIER(self):
            return self.getToken(DeepLearningDSLParser.MLP_CLASSIFIER, 0)

        def NEURAL_NETWORK(self):
            return self.getToken(DeepLearningDSLParser.NEURAL_NETWORK, 0)

        def PREDICT(self):
            return self.getToken(DeepLearningDSLParser.PREDICT, 0)

        def TRAIN(self):
            return self.getToken(DeepLearningDSLParser.TRAIN, 0)

        def KMEANS(self):
            return self.getToken(DeepLearningDSLParser.KMEANS, 0)

        def FIT_PREDICT(self):
            return self.getToken(DeepLearningDSLParser.FIT_PREDICT, 0)

        def GET_CENTROIDS(self):
            return self.getToken(DeepLearningDSLParser.GET_CENTROIDS, 0)

        def AUTOENCODER(self):
            return self.getToken(DeepLearningDSLParser.AUTOENCODER, 0)

        def ENCODE(self):
            return self.getToken(DeepLearningDSLParser.ENCODE, 0)

        def DECODE(self):
            return self.getToken(DeepLearningDSLParser.DECODE, 0)

        def RECONSTRUCT(self):
            return self.getToken(DeepLearningDSLParser.RECONSTRUCT, 0)

        def RECONSTRUCTION_ERROR(self):
            return self.getToken(DeepLearningDSLParser.RECONSTRUCTION_ERROR, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_ml_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMl_function" ):
                listener.enterMl_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMl_function" ):
                listener.exitMl_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMl_function" ):
                return visitor.visitMl_function(self)
            else:
                return visitor.visitChildren(self)




    def ml_function(self):

        localctx = DeepLearningDSLParser.Ml_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ml_function)
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(DeepLearningDSLParser.LINEAR_REGRESSION)
                self.state = 342
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 343
                self.expression()
                self.state = 344
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 345
                self.expression()
                self.state = 346
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
                self.match(DeepLearningDSLParser.MLP_CLASSIFIER)
                self.state = 349
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 350
                self.expression()
                self.state = 351
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 352
                self.expression()
                self.state = 353
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 354
                self.expression()
                self.state = 355
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 357
                self.match(DeepLearningDSLParser.NEURAL_NETWORK)
                self.state = 358
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 359
                self.expression()
                self.state = 360
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 361
                self.expression()
                self.state = 362
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 363
                self.expression()
                self.state = 364
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 366
                self.match(DeepLearningDSLParser.PREDICT)
                self.state = 367
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 368
                self.expression()
                self.state = 369
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 370
                self.expression()
                self.state = 371
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 373
                self.match(DeepLearningDSLParser.TRAIN)
                self.state = 374
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 375
                self.expression()
                self.state = 376
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 377
                self.expression()
                self.state = 378
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 6)
                self.state = 380
                self.match(DeepLearningDSLParser.KMEANS)
                self.state = 381
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 382
                self.expression()
                self.state = 383
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 384
                self.expression()
                self.state = 385
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 7)
                self.state = 387
                self.match(DeepLearningDSLParser.FIT_PREDICT)
                self.state = 388
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 389
                self.expression()
                self.state = 390
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 391
                self.expression()
                self.state = 392
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 8)
                self.state = 394
                self.match(DeepLearningDSLParser.GET_CENTROIDS)
                self.state = 395
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 396
                self.expression()
                self.state = 397
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 9)
                self.state = 399
                self.match(DeepLearningDSLParser.AUTOENCODER)
                self.state = 400
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 401
                self.expression()
                self.state = 402
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 403
                self.expression()
                self.state = 404
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 10)
                self.state = 406
                self.match(DeepLearningDSLParser.ENCODE)
                self.state = 407
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 408
                self.expression()
                self.state = 409
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 410
                self.expression()
                self.state = 411
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 11)
                self.state = 413
                self.match(DeepLearningDSLParser.DECODE)
                self.state = 414
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 415
                self.expression()
                self.state = 416
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 417
                self.expression()
                self.state = 418
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 12)
                self.state = 420
                self.match(DeepLearningDSLParser.RECONSTRUCT)
                self.state = 421
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 422
                self.expression()
                self.state = 423
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 424
                self.expression()
                self.state = 425
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 13)
                self.state = 427
                self.match(DeepLearningDSLParser.RECONSTRUCTION_ERROR)
                self.state = 428
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 429
                self.expression()
                self.state = 430
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 431
                self.expression()
                self.state = 432
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Io_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ_FILE(self):
            return self.getToken(DeepLearningDSLParser.READ_FILE, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def STRING(self):
            return self.getToken(DeepLearningDSLParser.STRING, 0)

        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def WRITE_FILE(self):
            return self.getToken(DeepLearningDSLParser.WRITE_FILE, 0)

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,0)


        def PRINT(self):
            return self.getToken(DeepLearningDSLParser.PRINT, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_io_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIo_function" ):
                listener.enterIo_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIo_function" ):
                listener.exitIo_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIo_function" ):
                return visitor.visitIo_function(self)
            else:
                return visitor.visitChildren(self)




    def io_function(self):

        localctx = DeepLearningDSLParser.Io_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_io_function)
        try:
            self.state = 452
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 436
                self.match(DeepLearningDSLParser.READ_FILE)
                self.state = 437
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 438
                self.match(DeepLearningDSLParser.STRING)
                self.state = 439
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.match(DeepLearningDSLParser.WRITE_FILE)
                self.state = 441
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 442
                self.match(DeepLearningDSLParser.STRING)
                self.state = 443
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 444
                self.expression()
                self.state = 445
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 447
                self.match(DeepLearningDSLParser.PRINT)
                self.state = 448
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 449
                self.expression()
                self.state = 450
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Plot_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLOT(self):
            return self.getToken(DeepLearningDSLParser.PLOT, 0)

        def LPAREN(self):
            return self.getToken(DeepLearningDSLParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DeepLearningDSLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(DeepLearningDSLParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(DeepLearningDSLParser.RPAREN, 0)

        def SCATTER(self):
            return self.getToken(DeepLearningDSLParser.SCATTER, 0)

        def COMMA(self):
            return self.getToken(DeepLearningDSLParser.COMMA, 0)

        def HISTOGRAM(self):
            return self.getToken(DeepLearningDSLParser.HISTOGRAM, 0)

        def getRuleIndex(self):
            return DeepLearningDSLParser.RULE_plot_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlot_function" ):
                listener.enterPlot_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlot_function" ):
                listener.exitPlot_function(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlot_function" ):
                return visitor.visitPlot_function(self)
            else:
                return visitor.visitChildren(self)




    def plot_function(self):

        localctx = DeepLearningDSLParser.Plot_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_plot_function)
        try:
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.match(DeepLearningDSLParser.PLOT)
                self.state = 455
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 456
                self.expression()
                self.state = 457
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
                self.match(DeepLearningDSLParser.SCATTER)
                self.state = 460
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 461
                self.expression()
                self.state = 462
                self.match(DeepLearningDSLParser.COMMA)
                self.state = 463
                self.expression()
                self.state = 464
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 466
                self.match(DeepLearningDSLParser.HISTOGRAM)
                self.state = 467
                self.match(DeepLearningDSLParser.LPAREN)
                self.state = 468
                self.expression()
                self.state = 469
                self.match(DeepLearningDSLParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





