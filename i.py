
def i(buf):
    buf[0]=buf[0]+  '0000000000 '
    buf[1]=buf[1]+  '0        0 '
    buf[2]=buf[2]+  '0        0 '
    buf[3]=buf[3]+  '00      00 '
    buf[4]=buf[4]+  '  0    0   '
    buf[5]=buf[5]+  '  0    0   '
    buf[6]=buf[6]+  '  0    0   '
    buf[7]=buf[7]+  '  0    0   '
    buf[8]=buf[8]+  '  0    0   '
    buf[9]=buf[9]+  '  0    0   '
    buf[10]=buf[10]+'  0    0   '
    buf[11]=buf[11]+'  0    0   '
    buf[12]=buf[12]+'00      00 '
    buf[13]=buf[13]+'0        0 ' 
    buf[14]=buf[14]+'0        0 '
    buf[15]=buf[15]+'0000000000 '
s=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
i(s)
i(s)
print(*s,sep='\n')
