# -*- coding: UTF-8 -*-
from Crypto.Cipher import AES
from Crypto.Hash import SHA
import re, string, base64

def Odd_Even(ka):
    '''
    bin(int('30',16))   bin(int('ea',16)) 
    -> 110000           -> 11101010
    -> 11000            -> 1110101
    -> count('1')       -> count('1') 
    -> even             -> odd
    -> 110001           -> 11101010
    '''
    k = []
    for i in ka:
        if bin(int(i,16)>>1).count('1') %2 == 0:
            k += [hex(1+(int(i,16)>>1<<1))[2:].zfill(2)]
        else:
            k += [hex((int(i,16)>>1<<1))[2:].zfill(2)]
    return ''.join(k)

def GetSHA1(D):
    h = SHA.new()
    h.update(D)
    return h.hexdigest()[:32]

C = '9MgYwmuPrjiecPMx61O6zIuy3MtIXQQ0E59T3xB6u0Gyf1gYs2i3K9Jxaa0zj4gTMazJuApwd6+jdyeI5iGHvhQyDHGVlAuYTgJrbFDrfB22Fpil2NfNnWFBTXyf7SDI'
C = base64.b64decode(C)

Visa = '12345678<8<<<1110182<1111167<<<<<<<<<<<<<<<4'   #校验位的7可按照标准计算得出
VisaNo = Visa[:9]   #证件号
VVisa = Visa[9]
Nationality = Visa[10:13]   #国籍
Birthday = Visa[13:19]      #生日
VBir = Visa[19]
Sex = Visa[20]              #性别
VisaEnd = Visa[21:27]
VVisaEnd = Visa[27]
Others = Visa[28:]
#机读区信息 = 证件号 + 校验数位 + 出生日期 + 校验数位 + 截止日期 + 校验数位 + 机读区信息
Info = VisaNo + VVisa + Birthday + VBir + VisaEnd + VVisaEnd
print Info
#计算“机读区信息”的 SHA-1 散列并获取 Kseed
K_seed = GetSHA1(Info)
#计算D和D的SHA-1散列
D = (K_seed + '0' * 7 + '1').decode('hex')
key = GetSHA1(D)
#将key（D的SHA-1散列）对半分为K1和K2
k1 = Odd_Even(re.findall('.{2}',key[:16]))
k2 = Odd_Even(re.findall('.{2}',key[16:]))
key = k1 + k2
print 'The key is:', key
#以CBC模式解密
cipher = AES.new(key.decode('hex'), AES.MODE_CBC, ('0'*32).decode('hex'))
print 'The M is:', cipher.decrypt(C)