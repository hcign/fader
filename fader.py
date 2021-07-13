# Made by @hcign on instagram!
# Discord: hcign#0495
# Twitter: @hcign
#basic html colours, more have been added.
#        'pink':(222,31,171),
#        'purple':(81,15,138),
#        'blue':(11,25,222),
#        'cyan':(5,189,245),
#        'turquoise':(14,161,129),
#        'lime':(5,255,9),
#        'green':(4,85,6),
#        'white':(255,255,255),
#        'grey':(50,50,50),
#        'red':(252,8,8),
#        'yellow':(255,202,0)

import argparse
import time
from sys import exit
import os
from os import path

#sets end of script for output doc
clear="\033[0;00m"
os.system('clear')
colors = {
        'yellow':(255,202,0),
        'darkblue':(1,12,59),
        'sunyellow':(246,255,0),
        'forestgreen':(35,117,2),
        'gold':(207,165,0),
        'blueviolet':(116,3,255),
        'hotpink':(255,0,212),
        'candy':(255,0,102),
        'sienna':(160,82,45),
        'crimson':(220,20,60),
        'pink':(222,31,171),
        'purple':(81,15,138),
        'blue':(11,25,222),
        'cyan':(5,189,245),
        'turquoise':(14,161,129),
        'lime':(5,255,9),
        'green':(4,85,6),
        'white':(255,255,255),
        'grey':(50,50,50),
        'red':(252,8,8),
        'lightcoral':(240,128,128)
        }   
        
def gradiant(startrgb,endrgb,text):

    #calculates the amount to change red, green, and blue values each character
    changer = int((int(endrgb[0]) - int(startrgb[0]))/len(text))
    changeg = int((int(endrgb[1]) - int(startrgb[1]))/len(text))
    changeb = int((int(endrgb[2]) - int(startrgb[2]))/len(text))

    r = int(startrgb[0]) #initial red value
    g = int(startrgb[1]) #initial green value
    b = int(startrgb[2]) #initial blue value

    for letter in text:
        if letter == '\n': continue
        print(f"\x1b[38;2;{r};{g};{b}m{letter}",end="")
        r+=changer 
        g+=changeg 
        b+=changeb 

def validatergb(rgb):
    #validates a tuple rgb 
    
    if not len(rgb) == 3:
        return False
    
    try:
        if 0 <= int(rgb[0]) <= 255 and 0 <= int(rgb[1]) <= 255 and 0 <= int(rgb[2]) <= 255:
            return True
        else:
            return False
    except ValueError:
        return False
def Main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("filename", type=str, help='[38;2;244;12;203mTh[38;2;233;24;194me[38;2;222;36;185m [38;2;211;48;176mf[38;2;200;60;167mi[38;2;189;72;158ml[38;2;178;84;149me[38;2;167;96;140m [38;2;156;108;131mt[38;2;145;120;122mo[38;2;134;132;113m [38;2;123;144;104mr[38;2;112;156;95me[38;2;101;168;86ma[38;2;90;180;77md[38;2;79;192;68m [38;2;68;204;59mf[38;2;57;216;50mr[38;2;46;228;41mo[38;2;35;240;32mm [40;37m')
    parser.add_argument("color1",type=str,help='[38;2;247;8;206mTh[38;2;239;16;200me[38;2;231;24;194m [38;2;223;32;188mf[38;2;215;40;182mi[38;2;207;48;176mr[38;2;199;56;170ms[38;2;191;64;164mt[38;2;183;72;158m [38;2;175;80;152mc[38;2;167;88;146mo[38;2;159;96;140ml[38;2;151;104;134mo[38;2;143;112;128mr[38;2;135;120;122m [38;2;127;128;116mo[38;2;119;136;110mf[38;2;111;144;104m [38;2;103;152;98mt[38;2;95;160;92mh[38;2;87;168;86me[38;2;79;176;80m [38;2;71;184;74mg[38;2;63;192;68mr[38;2;55;200;62ma[38;2;47;208;56md[38;2;39;216;50mi[38;2;31;224;44ma[38;2;23;232;38mn[38;2;15;240;32mt [40;37m')
    parser.add_argument("color2",type=str,help='[38;2;255;0;212mT[38;2;248;7;206mh[38;2;241;14;200me[38;2;234;21;194m [38;2;227;28;188ms[38;2;220;35;182me[38;2;213;42;176mc[38;2;206;49;170mo[38;2;199;56;164mn[38;2;192;63;158md[38;2;185;70;152m [38;2;178;77;146mc[38;2;171;84;140mo[38;2;164;91;134ml[38;2;157;98;128mo[38;2;150;105;122mr[38;2;143;112;116m [38;2;136;119;110mo[38;2;129;126;104mf[38;2;122;133;98m [38;2;115;140;92mt[38;2;108;147;86mh[38;2;101;154;80me[38;2;94;161;74m [38;2;87;168;68mg[38;2;80;175;62mr[38;2;73;182;56ma[38;2;66;189;50md[38;2;59;196;44mi[38;2;52;203;38ma[38;2;45;210;32mn[38;2;38;217;26mt [40;37m')
    args = parser.parse_args()

    color1 = args.color1.lower()
    color2 = args.color2.lower()

    if color1 in colors.keys():
        startcolor = colors.get(color1)
    elif validatergb(tuple(color1.split(','))):
        startcolor = tuple(color1.split(','))
    else:
        #scans for wether color 1 is invalid
        print('[38;2;255;255;255mI[38;2;255;250;253mn[38;2;255;245;251mv[38;2;255;240;249ma[38;2;255;235;247ml[38;2;255;230;245mi[38;2;255;225;243md[38;2;255;220;241m [38;2;255;215;239me[38;2;255;210;237mn[38;2;255;205;235mt[38;2;255;200;233mr[38;2;255;195;231my[38;2;255;190;229m [38;2;255;185;227mf[38;2;255;180;225mo[38;2;255;175;223mr[38;2;255;170;221m [38;2;255;165;219mc[38;2;255;160;217mo[38;2;255;155;215ml[38;2;255;150;213mo[38;2;255;145;211mr[38;2;255;140;209m1[38;2;255;135;207m.[38;2;255;130;205m [38;2;255;125;203mU[38;2;255;120;201ms[38;2;255;115;199me[38;2;255;110;197m [38;2;255;105;195m-[38;2;255;100;193mh[38;2;255;95;191m [38;2;255;90;189mf[38;2;255;85;187mo[38;2;255;80;185mr[38;2;255;75;183m [38;2;255;70;181mh[38;2;255;65;179me[38;2;255;60;177ml[38;2;255;55;175mp')
        exit(1)

    if color2 in colors.keys():
        endcolor = colors.get(color2)
    elif validatergb(tuple(color2.split(','))):
        endcolor = tuple(color2.split(','))
    else:
        #scans for wether color 2 is invalid
        print('[38;2;255;255;255mI[38;2;255;250;253mn[38;2;255;245;251mv[38;2;255;240;249ma[38;2;255;235;247ml[38;2;255;230;245mi[38;2;255;225;243md[38;2;255;220;241m [38;2;255;215;239me[38;2;255;210;237mn[38;2;255;205;235mt[38;2;255;200;233mr[38;2;255;195;231my[38;2;255;190;229m [38;2;255;185;227mf[38;2;255;180;225mo[38;2;255;175;223mr[38;2;255;170;221m [38;2;255;165;219mc[38;2;255;160;217mo[38;2;255;155;215ml[38;2;255;150;213mo[38;2;255;145;211mr[38;2;255;140;209m2[38;2;255;135;207m.[38;2;255;130;205m [38;2;255;125;203mU[38;2;255;120;201ms[38;2;255;115;199me[38;2;255;110;197m [38;2;255;105;195m-[38;2;255;100;193mh[38;2;255;95;191m [38;2;255;90;189mf[38;2;255;85;187mo[38;2;255;80;185mr[38;2;255;75;183m [38;2;255;70;181mh[38;2;255;65;179me[38;2;255;60;177ml[38;2;255;55;175mp')
        exit(1)
    #scans for file name
    if not path.exists(args.filename):
        print(f"[38;2;255;255;255mC[38;2;254;244;251mo[38;2;253;233;247mu[38;2;252;222;243ml[38;2;251;211;239md[38;2;250;200;235m [38;2;249;189;231mn[38;2;248;178;227mo[38;2;247;167;223mt[38;2;246;156;219m [38;2;245;145;215mf[38;2;244;134;211mi[38;2;243;123;207mn[38;2;242;112;203md[38;2;241;101;199m [38;2;240;90;195mf[38;2;239;79;191mi[38;2;238;68;187ml[38;2;237;57;183me[38;2;236;46;179m {args.filename}")
        exit(2)

    with open(args.filename, encoding='utf8', mode='r', errors='replace') as f: 
        for line in f.readlines():
            gradiant(startcolor,endcolor,line)
            print('')
    print(clear)
if __name__ == '__main__':
    Main()