from note_construct import *

file = './notation/note_test8.png'
des = './wav_output/note_test8.wav'

exprs = notation_to_parameters(file)
for i in range(len((exprs[0]))):
    if len(exprs[6][i]) < 10:
        print('notation should be longer!!')
        continue
    expr = (exprs[0][i], exprs[1][i], exprs[2][i], exprs[3][i], exprs[4][i], exprs[5][i], exprs[6][i])
    note_construct(expr, des)