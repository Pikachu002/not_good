def bs(buf):
    buf[0]=buf[0]+  '   000000000000000  '   
    buf[1]=buf[1]+  ' 00               0 '
    buf[2]=buf[2]+  '0     000000      0 '
    buf[3]=buf[3]+  '0     0     0000000 '
    buf[4]=buf[4]+  '0     0             '
    buf[5]=buf[5]+  '0     0             '
    buf[6]=buf[6]+  ' 0    0000          '
    buf[7]=buf[7]+  '  00      00000     '
    buf[8]=buf[8]+  '    000        00   '
    buf[9]=buf[9]+  '       000000    0  '
    buf[10]=buf[10]+'            0     0 '
    buf[11]=buf[11]+'            0     0 '
    buf[12]=buf[12]+'0000000     0     0 '
    buf[13]=buf[13]+'0      000000     0 ' 
    buf[14]=buf[14]+'0               00  '
    buf[15]=buf[15]+' 000000000000000    '
s=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
bs(s)
bs(s)
print(*s,sep='\n')







         

 







