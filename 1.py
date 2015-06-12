#-*- coding:utf-8 -*-

words="abcdefghijklmnopqrstuvwxyz"
num = len(words)-1

def change(w,x,y):
    xn = words.find(x)
    yn = words.find(y)
#    print "xn %s yn %s num %s" % (xn,yn,num)
    if xn > yn:
        n = num - xn + yn
    else :
        n = yn -xn
    dd=""
    for wx in w:
        wn = words.find(wx)
        if wn == -1:
            dd += wx
        else:
            if wn+n > num:
                dd += words[int(int(wn+n) % int(num+1))]
            else:
                dd += words[int(wn+n)]
#        print "wx %s wn %s dd %s n %s wn %s wn+n %s" % (wx,wn,dd,n,wn,(wn+n))

    return dd





if __name__ == '__main__':
    cc="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    ba = change(cc,'k','m')
    print ba

    print change('map','o','q')

    import string

    table = string.maketrans(
            "abcdefghijklmnopqrstuvwxyz",
            "cdefghijklmnopqrstuvwxyzab"
            )

    print cc.translate(table)
