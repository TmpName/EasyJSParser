# -*- coding: utf-8 -*- 
#
# Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
#

#******************************
#   A Basic Javascript parser
#******************************

# TODO LIST
# ---------
# Regex will work only for normal name, not for exotic name
# Object
# Globla/Local variables/function/object
#utiliser un tableau special pr variable passe en parametrzs > clash
# (True)?(a = 2):(a = 3); don't work because of () at first

#help
#https://sarfraznawaz.wordpress.com/2012/01/26/javascript-self-invoking-functions/
#https://nemisj.com/python-api-javascript/
#https://fr.wikiversity.org/wiki/Python/Les_types_de_base
#https://javascriptobfuscator.com/Javascript-Obfuscator.aspx
#https://nemisj.com/python-api-javascript/

#UNICODE ERROR
#print a.decode('utf-8').encode('ascii','replace')
#true = 1 instead of true

# x == 2 && dosomething();
# dosomething() will only be called if x == 2. This is called Short-circuiting.

import re
import types
from types import NoneType
import time

import sys

REG_NAME = '[\w]+'
REG_OP = '[\/\*\-\+\{\}\[\]<>\|=~^%!]+' #not space here
DEBUG = True # Never enable it in kodi, too big size log
MAX_RECURSION = 50
ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

#---------------------------------------------------------------------------------


JScode = """
function XcK(_0xfc1900,_0x9e1420) { return _0xfc1900(_0x9e1420); }
function TYf(_0x3969f8,_0x48db24) { return _0x3969f8/_0x48db24; }
function wyf(_0x234038,_0x42c6db) { return _0x234038-_0x42c6db; }
function eAE(_0x425ad1,_0xc0cae2) { return _0x425ad1<_0xc0cae2; }
function hlO(_0x5319f7,_0x1e7980) { return _0x5319f7!=_0x1e7980; }
function kOL(_0x419965,_0x1ed3ea) { return _0x419965==_0x1ed3ea; }
function iJA(_0x3953f0,_0x2d9f37,_0x4f842b) { return _0x3953f0(_0x2d9f37,_0x4f842b); }
function oET(_0xbb4971,_0x3fdb77) { return _0xbb4971%_0x3fdb77; }
function gJK(_0xe13ab1,_0x363e1d) { return _0xe13ab1==_0x363e1d; }
function pLB(_0x3ab1d7,_0x5b73ee,_0x12dbc2) { return _0x3ab1d7(_0x5b73ee,_0x12dbc2); }
function WNS(_0x5324b2,_0x9c4759) { return _0x5324b2+_0x9c4759; }
function ZeT(_0x11547f,_0x2c0d13) { return _0x11547f+_0x2c0d13; }
function xRD(_0x14f459,_0x569260) { return _0x14f459<_0x569260; }
var _0x254069='3|6|2|7|4|0|5|1|8'.split('|'),_0x38b61f=0;while(true){
switch(_0x254069[_0x38b61f++]){

case'0':var _0x5e82dd=_0x563f72.join(''),_0x5e5aae=[];

continue;
case'1':
for(var _0x1041b1=0;xRD(_0x1e74c2,_0x5e82dd.length);){
var _0x221589=_0x5e82dd.substring(_0x1e74c2,ZeT(_0x1e74c2,2));
var _0x46bf10=_0x5e82dd.substring(_0x1e74c2,WNS(_0x1e74c2,3));
var _0x450a25=pLB(parseInt,_0x221589,16);
_0x1e74c2+=2;
gJK(oET(_0x1041b1,3),0)?(_0x450a25=iJA(parseInt,_0x46bf10,8),_0x1e74c2+=1):kOL(oET(_0x1041b1,2),0)&&hlO(0,_0x1041b1)&&eAE(_0x5e82dd[wyf(_0x1041b1,1)].charCodeAt(0),60)&&(_0x450a25=iJA(parseInt,_0x46bf10,10),_0x1e74c2+=1);
var _0x31b23d=_0x347706[oET(_0x1041b1,7)];
_0x450a25^=213;
_0x450a25^=_0x31b23d;
_0x5e5aae.push(String.fromCharCode(_0x450a25));
_0x1041b1+=1;


}

continue;
case'2':
for(var _0x2d246a=_0x30d464.substring(_0x84a7b0,WNS(_0x84a7b0,36)),_0x347706=new Array(12),_0x1e74c2=0;eAE(_0x1e74c2,_0x2d246a.length);){
var _0x24ac16=_0x2d246a.substring(_0x1e74c2,WNS(_0x1e74c2,3));
_0x347706[TYf(_0x1e74c2,3)]=iJA(parseInt,_0x24ac16,8),_0x1e74c2+=3;
}
continue;
case'3':var _0x30d464='250730212410323372070311542152273760550920272740711f2319b18111418474143f821536444fc0776b2503371864737624097364192f4132ff116067134be2552d190102006',_0x526965=_0x30d464.charCodeAt(0),_0x84a7b0=wyf(_0x526965,55),_0x4d54a4=Math.max(2,_0x84a7b0);continue;
case'4':_0x563f72.splice(_0x84a7b0,36);
continue;
case'5':_0x1e74c2=0;continue;
case'6':_0x84a7b0=Math.min(_0x4d54a4,wyf(wyf(_0x30d464.length,36),2));continue;
case'7':var _0x563f72=_0x30d464.split('');
continue;
case'8':Result=_0x5e5aae.join('');
continue;
}
break;
}

"""

JScodeTTT = """
a = true&true;
debug();
"""

JScodecontinu = """
var i = 4;
var j = "A";
while (i > 0 ){
i = i - 1;
if ( i == 2) { continue; }
j = j + i;

}
debug();
"""

JScode885 = """
ﾟωﾟﾉ= /｀ｍ´）ﾉ ~┻━┻   //*´∇｀*/ ['_']; o=(ﾟｰﾟ)  =_=3; c=(ﾟΘﾟ) =(ﾟｰﾟ)-(ﾟｰﾟ);
(ﾟДﾟ) =(ﾟΘﾟ)= (o^_^o)/ (o^_^o);

(ﾟДﾟ)={
      ﾟΘﾟ: '_' ,
      ﾟωﾟﾉ : ((ﾟωﾟﾉ==3) +'_') [ﾟΘﾟ] ,
      ﾟｰﾟﾉ :(ﾟωﾟﾉ+ '_')[o^_^o -(ﾟΘﾟ)] ,
      ﾟДﾟﾉ:((ﾟｰﾟ==3) +'_')[ﾟｰﾟ] 
      };

(ﾟДﾟ) [ﾟΘﾟ] =((ﾟωﾟﾉ==3) +'_') [c^_^o];
(ﾟДﾟ) ['c'] = ((ﾟДﾟ)+'_') [ (ﾟｰﾟ)+(ﾟｰﾟ)-(ﾟΘﾟ) ];
(ﾟДﾟ) ['o'] = ((ﾟДﾟ)+'_') [ﾟΘﾟ];

(ﾟoﾟ)=(ﾟДﾟ) ['c']+(ﾟДﾟ) ['o']+(ﾟωﾟﾉ +'_')[ﾟΘﾟ]+ ((ﾟωﾟﾉ==3) +'_') [ﾟｰﾟ] + ((ﾟДﾟ) +'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ ((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+((ﾟｰﾟ==3) +'_') [(ﾟｰﾟ) - (ﾟΘﾟ)]+(ﾟДﾟ) ['c']+((ﾟДﾟ)+'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ (ﾟДﾟ) ['o']+((ﾟｰﾟ==3) +'_') [ﾟΘﾟ];(ﾟДﾟ) ['_'] =(o^_^o) [ﾟoﾟ] [ﾟoﾟ];(ﾟεﾟ)=((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟДﾟ) .ﾟДﾟﾉ+((ﾟДﾟ)+'_') [(ﾟｰﾟ) + (ﾟｰﾟ)]+((ﾟｰﾟ==3) +'_') [o^_^o -ﾟΘﾟ]+((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟωﾟﾉ +'_') [ﾟΘﾟ];


(ﾟｰﾟ)+=(ﾟΘﾟ);
(ﾟДﾟ)[ﾟεﾟ]='\\';
(ﾟДﾟ).ﾟΘﾟﾉ=(ﾟДﾟ+ ﾟｰﾟ)[o^_^o -(ﾟΘﾟ)];
(oﾟｰﾟo)=(ﾟωﾟﾉ +'_')[c^_^o];
(ﾟДﾟ) [ﾟoﾟ]='\"';

(ﾟДﾟ) ['_'] ( (ﾟДﾟ) ['_'] (ﾟεﾟ+(ﾟДﾟ)[ﾟoﾟ]+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ ((ﾟｰﾟ) + (o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (o^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (o^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟoﾟ]) (ﾟΘﾟ)) ('_');
"""

JScodeQ ="""
eval(function(p,a,c,k,e,r){e=String;if(!''.replace(/^/,String)){while(c--)r[c]=k[c]||c;k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('(0(){4 1="5 6 7 8";0 2(3){9(3)}2(1)})();',10,10,'function|b|something|a|var|some|sample|packed|code|alert'.split('|'),0,{}));
"""


JScode753 ="""
dd = /\uff40\uff4d\u00b4\uff09\uff89 ~\u253b\u2501\u253b   /["_"];

o = ff = _ = 3;

c = gg = ff - ff;

ee = gg = (o ^ _ ^ o) / (o ^ _ ^ o);

ee = {
  "gg" : "_",
  "dd" : ((dd == 3) + "_")[gg],
  "cc" : (dd + "_")[o ^ _ ^ o - gg],
  "bb" : ((ff == 3) + "_")[ff]
};


ee[gg] = ((dd == 3) + "_")[c ^ _ ^ o];
ee["c"] = (ee + "_")[ff + ff - gg];
ee["o"] = (ee + "_")[gg];


ii = ee["c"] + ee["o"] + (dd + "_")[gg] + ((dd == 3) + "_")[ff] + (ee + "_")[ff + ff] + ((ff == 3) + "_")[gg] + ((ff == 3) + "_")[ff - gg] + ee["c"] + (ee + "_")[ff + ff] + ee["o"] + 
((ff == 3) + "_")[gg];
ee["_"] = (o ^ _ ^ o)[ii][ii];
hh = ((ff == 3) + "_")[gg] + ee.bb + (ee + "_")[ff + ff] + ((ff == 3) + "_")[o ^ _ ^ o - gg] + ((ff == 3) + "_")[gg] + (dd + "_")[gg];
ff += gg;

ee[hh] = "\\";
ee.aa = (ee + ff)[o ^ _ ^ o - gg];
offo = (dd + "_")[c ^ _ ^ o];

ee[ii] = '"';

ret = ee["_"](ee["_"](hh + ee[ii] + ee[hh] + gg + ff + gg + ee[hh] + gg + (ff + gg) + ff + ee[hh] + gg + ff + (ff + gg) + ee[hh] + 
gg + ((o ^ _ ^ o) + (o ^ _ ^ o)) + ((o ^ _ ^ o) - gg) + ee[hh] + gg + ((o ^ _ ^ o) + (o ^ _ ^ o)) + ff + ee[hh] + (ff + gg) + (c ^ _ ^ o) + ee[hh] + ff + ((o ^ _ ^ o) - gg) + ee[hh] + gg + gg + (c ^ _ ^ o) + ee[hh] + 
gg + ff + (ff + gg) + ee[hh] + gg + (ff + gg) + ff + ee[hh] + gg + (ff + gg) + ff + ee[hh] + gg + (ff + gg) + (ff + (o ^ _ ^ o)) + ee[hh] + 
(ff + gg) + ff + ee[hh] + ff + (c ^ _ ^ o) + ee[hh] + gg + gg + ((o ^ _ ^ o) - gg) + ee[hh] + gg + ff + gg + ee[hh] + gg + ((o ^ _ ^ o) + (o ^ _ ^ o)) + ((o ^ _ ^ o) + (o ^ _ ^ o)) + ee[hh] + 
gg + ff + gg + ee[hh] + gg + ((o ^ _ ^ o) - gg) + (o ^ _ ^ o) + ee[hh] + gg + ff + (o ^ _ ^ o) + ee[hh] + gg + ((o ^ _ ^ o) + (o ^ _ ^ o)) + ((o ^ _ ^ o) - gg) + ee[hh] + gg + (ff + gg) + 
gg + ee[hh] + gg + ((o ^ _ ^ o) + (o ^ _ ^ o)) + (c ^ _ ^ o) + ee[hh] + gg + ((o ^ _ ^ o) + (o ^ _ ^ o)) + ff + ee[hh] + ff + ((o ^ _ ^ o) - gg) + ee[hh] + (ff + gg) + gg + ee[ii])(gg))("_");
debug();
"""

JScode4554 ="""
(function(s, opt_attributes, key, pairs, i, params) {
  /** @type {function (new:String, *=): string} */
  i = String;
  if (!''.replace(/^/,String)) {
    for (;key--;) {
      /** @type {(number|string)} */
      params[key] = pairs[key] || key;

    }
    /** @type {Array} */
    pairs = [function(urlParam) {
      return params[urlParam];
    }];

    /**
     * @return {?}
     */
    i = function() {
      return "\\w+";
    };

    /** @type {number} */
    key = 1;
  }

  for (;key--;) {
    if (pairs[key]) {
      /** @type {string} */
      s = s.replace(new RegExp("\\b" + i(key) + "\\b", "g"), pairs[key]);

    }
  }

  return s;
})('(0(){4 1="5 6 7 8";0 2(3){9(3)}2(1)})();', 10, 10, "function|b|something|a|var|some|sample|packed|code|alert".split("|"), 0, {});
"""

JScode7788 = """
(function(){var b="some sample packed code";function something(a){alert(a)}something(b)})();
"""

JScodeswitch = """
switch(0) {
    case 0:
        a = 1;
        break;
    case 1:
        a = 2;
        break;
}
debug();
"""

JScode7744 ="""
eval(function(p, a, c, k, e, r) {
    e = String;
    if (!''.replace(/^/, String)) {
        while (c--) r[c] = k[c] || c;
        k = [function(e) {
            return r[e]
        }];
        e = function() {
            return '\\w+'
        };
        c = 1
    };

    while (c--)

        if (k[c]) p = p.replace(new RegExp('\\b' + e(c) + '\\b', 'g'), k[c]);

    return p
}('(0(){4 1="5 6 7 8";0 2(3){9(3)}2(1)})();', 10, 10, 'function|b|something|a|var|some|sample|packed|code|alert'.split('|'), 0, {}));
"""

JScode77878 = """
var cars = ["aa", "bb", "cc", "dd"];
var i, len, text="to erase";
for (i = 0, len = cars.length, text = ""; i < len; i++) {
    text += cars[i] + " " ;
    if ( i == 0) break;
}

var j = 2.5;
j*=2;

text += j;

debug();

"""

JScode741 ="""
var t = 78;

$(document).ready(function() {
    var y = $("#aQydkd1Gbfx").text();
    var x = $("#aQydkd1Gbf").text();
    var s = [];
    for (var i = 0; i < y.length; i++) {
        var j = y.charCodeAt(i);
        if ((j >= 33) && (j <= 126)) {
            s[i] = String.fromCharCode(33 + ((j + 14) % 94));
        } else {
            s[i] = String.fromCharCode(j);
        }
    }
    var tmp = s.join("");
    var str = tmp.substring(0, tmp.length - _CoRPE1bSt9()) + String.fromCharCode(tmp.slice(0 - _CoRPE1bSt9()).charCodeAt(0) + _0oN0h2PZmC()) + tmp.substring(tmp.length - _CoRPE1bSt9() + 1);
    $("#streamurl").text(str);
});
t = 10;

function nWuEkcMO4z() {
    return 2 + 1;
}

function _CoRPE1bSt9() {
    return nWuEkcMO4z() + 1478067443 - 1478067445;
}

function _0oN0h2PZmC() {
    return _CoRPE1bSt9() - _7L9xjpbs4N();
}

function _7L9xjpbs4N() {
    return -2;
}
"""

def ASCIIDecode(string):
    i = 0
    l = len(string)
    ret = ''
    while i < l:
        c =string[i]
        if string[i:(i+2)] == '\\x':
            c = chr(int(string[(i+2):(i+4)],16))
            i+=3
        if string[i:(i+2)] == '\\u':
            c = chr(int(string[(i+2):(i+6)],16))
            i+=5     
        ret = ret + c
        i = i + 1

    return ret

def IsUnicode(s):
    if isinstance(s, unicode):
        return True
    return False
   
def out(string):
    if DEBUG:
        print str(string.decode('latin-1').encode('ascii','replace'))
        
def Ustr(string):
    if isinstance(string, unicode):
        return str(string.encode('ascii','replace'))
    return str(string)
 
    
def GetFirstChar(string):
    j = 0
    try:
        while (string[j].isspace()):
            j = j + 1
    except:
        return ''
    return string[j]
    
def GetNextchar(string, pos):
    if len(string) <= (pos + 1):
        return ''
    return string[pos+1]
    
def GetPrevchar(string, pos):
    if (pos - 1) < 0:
        return ''
    return string[pos-1]
    
def GetBeetweenChar(str,char1,char2):
        s = str.find(char1)
        if s == -1:
            return 0,''
            
        n = 1
        e = s + 1
        while (n > 0) and (e < len(str)):
            c = str[e]
            if c == char1:
                n = n + 1
            if c == char2:
                n = n - 1
            e = e + 1
            
        s = s + 1
        e = e - 1
        return e,str[s:e]
        
def CheckType(value):
    if (isinstance(value, types.StringTypes)):
        return 'String'
    if isinstance(value, ( bool ) ):
        return 'Bool'
    if isinstance(value, ( int, long, float ) ):
        return 'Numeric'
    if type(value) in [list,tuple, dict]:
        return 'Array'
    if (isinstance(value, (NoneType))):
        return 'Undefined'
    if isinstance(value, fonction):
        return 'Fonction'        
    return 'Unknow'

#Fonction to return only one parameter from a string with correct closed [] () "" and ''      
def GetItemAlone(string,separator = ' '):

    l = len(string) - 1
    ret = ''
    
    i = -1
    p = 0 #parenthese
    a = 0 #accolade
    b = 0 #bracket
    c1 = 0
    c2 = 0
    n = False
    last_char = ''

    s = False
    
    while (i < l):
        i = i + 1
        ch = string[i]
        ret = ret + ch
        n = False
        
        #Skip empty space
        if (ch.isspace()):
            continue

        if ch == '"' and not GetPrevchar(string,i) == '\\' and not c2:
            c1 = 1 - c1
        if ch == "'" and not GetPrevchar(string,i) == '\\' and not c1:
            c2 = 1 - c2

        if not c1 and not c2:
            if ch == '(':
                p = p + 1
            if ch == ')':
                p = p - 1
            if ch == '{':
                a = a + 1
            if ch == '}':
                a = a - 1
            if ch == '[':
                b = b + 1
            if ch == ']':
                b = b - 1

            if ch == '.' and not ((last_char in '0123456789') or (string[i+1] in '0123456789')):
                n = True
        
        if (ch in separator) and (p==0) and (a==0) and (b==0) and (c1==0) and (c2==0) and not(n):
            return ret
            
        last_char = ch   

    return ret
    
def MySplit(string,char,NoEmpty = False):
    r = []
    l = len(string)
    i = 0
    chain = 0
    p = 0
    e = ""
    
    if l == 0:
        if (NoEmpty):
            return []
            
    while (l > i):
        c = string[i]
        if c == '"':
            chain = 1-chain
        if c == '(':
            p = p + 1
        if c == ')':
            p = p - 1           
            
        if (c == char) and (chain == 0) and (p==0):
            r.append(e.strip())
            e = ''
        else:    
            e = e + c
            
        i = i + 1

    r.append(e.strip())
    return r
    
def GetConstructor(value):
    if isinstance(value, ( int, long ) ):
        r = fonction('Number','','\n    [native code]\n',True)
        return r
    elif isinstance(value, fonction):
        r = fonction('Function','','\n    [native code]\n',True)
        return r
    elif (isinstance(value, types.StringTypes)):
        r = fonction('String','','\n    [native code]\n',True)
        return r
    return ''

class JSBuffer(object):
    PRIORITY = {'+':3 , '-':3 , '*':4 , '/':4 , '>':1 , '<':1 , '&':2 , '|':2}
    #print prio.get('*',0)
    def __init__(self):
        self.type = None
        self.buffer = ''
        self.__op = ''
        self.__value = None
        
        #buffers
        self.buf=[]
        self.opBuf = []
        
    def SetOp(self,op):
        #print 'Set op  ' + str(op)
        if (op == '&') and  (self.__op == '&'):
            return
        if (op == '|') and  (self.__op == '|'):
            return
        else:
            self.__op = self.__op + op
            
    def CheckString(self):
        if len(self.buf) >= len(self.opBuf):
            return True
        return False
        
    #Need 3 values for priority   
    def AddValue(self,value):
        out('ADD ' + Ustr(value) + ' ' + Ustr(type(value)) + ' a ' + Ustr(self.buf))
        if not self.type:
            self.type = CheckType(value)
            self.Push(value,self.__op)
            return       
         
        if not self.__op:
            out( 'op ' + str(self.opBuf) + ' - buff ' +str(self.buf))
            raise Exception("Missing operator")
            
        self.Push(value,self.__op)
        self.__op = ''
    
    def GetPrevious(self):
        ret = self.buf[-1]
        del self.buf[-1]
        self.__op = self.opBuf[-1]
        del self.opBuf[-1]
        if len(self.buf) == 0:
            self.type = None
        return ret
        
    def Compute(self):
    
        #check type
        if len(self.buf) > 1:
            if not (self.type == CheckType(self.buf[len(self.buf) -1])):
                #Type different mais juste operation logique
                if self.opBuf[1] == '==':
                    self.type = 'Logic'
                #Type different mais JS convertis en string
                else:
                    out('string convertion')
                    
                    if not CheckType(self.buf[0]) == 'String':
                        self.buf[0]=self.SpecialStr(self.buf[0])
                    if len(self.buf) > 1:
                        if not CheckType(self.buf[1]) == 'String':
                            self.buf[1]=self.SpecialStr(self.buf[1])
                    self.type = 'String'

        #Work for operateur + | !
        if self.type == 'String':
            if '!' in self.opBuf[0]:
                self.buf[0] = not self.buf[0]
                self.opBuf[0] = self.opBuf[0].replace('!','')
            if len(self.buf) > 1:
                if '!' in self.opBuf[1]:
                    self.buf[1] = not self.buf[1]
                    self.opBuf[1] = self.opBuf[1].replace('!','')
                if '+' in self.opBuf[1]:
                    self.buf[0] = self.buf[0] + self.buf[1]
                if '|' in self.opBuf[1]:
                    if not self.buf[0]:
                        self.buf[0] = self.buf[1]
                #decale
                del self.opBuf[-1]
                del self.buf[-1]
                                       
        #work for all operator      
        elif self.type == 'Numeric':
            if len(self.buf) > 1:
                self.buf[0] = self.opBuf[0] + str(self.buf[0]) + self.opBuf[1] + str(self.buf[1])
                self.opBuf[0] = ''
                #decale
                del self.opBuf[-1]
                del self.buf[-1]
            else:
                self.buf[0] = self.opBuf[0] + str(self.buf[0])
                self.opBuf[0] = ''

        #work for bool     
        elif self.type == 'Bool':
            if len(self.buf) > 1:
                self.buf[0] = self.opBuf[0] + str(self.buf[0]) + self.opBuf[1] + str(self.buf[1])
                self.opBuf[0] = ''
                #decale
                del self.opBuf[-1]
                del self.buf[-1]
            else:
                self.buf[0] = self.opBuf[0] + str(self.buf[0])
                self.opBuf[0] = ''
                
        # work for
        elif self.type == 'Logic':
            if not self.buf[0] == self.buf[1]:
                self.buf[0] = False
            else:
                self.buf[0] = True
            #decale
            del self.opBuf[-1]
            del self.buf[-1]
            
        elif len(self.buf) > 1:
            print self.type
            print self.buf
            print self.opBuf
            raise Exception("Can't compute")
    
    #on decale tout
    def Push(self,value,op):
        
        if len(self.buf) > 1:
            self.Compute()

        self.buf.append(value)
        self.opBuf.append(op)
        return

    def SpecialStr(self,value):
        if CheckType(value) == 'Numeric':
            return str(value)
        if value == None:
            return 'Undefined'
        if value == True:
            return 'true'
        if value == False:
            return 'false'
        if type(value) in [list]:
            convert_first_to_generator = (str(w) for w in value)
            return ','.join(convert_first_to_generator)
        if type(value) in [dict]:
            return '[object Object]'
        if CheckType(value) == 'Fonction':
            return value.ToStr()
        
        return str(value)
    
    #ok all finished, force compute
    def GetBuffer(self):
    
        #Force compute
        self.Compute()
        while len(self.buf) > 1:
            self.Compute()
          
        if self.type == 'Logic':
            return self.buf[0]
    
        if self.type == 'Numeric':
            return self.SafeEval(self.buf[0])
            
        if self.type == 'Bool':
            if self.SafeEval(self.buf[0].replace('True','1').replace('False','0')):
                return True
            else:
                return False
        
        if self.type == None:
            return ''
        
        return self.buf[0]
        
    #WARNING : Take care if you edit this function, eval is realy unsafe.
    #better to use ast.literal_eval() but not implemented before python 3
    def SafeEval(self,str):
        if not str:
            raise Exception ('Nothing to eval')
        f = re.search('[^0-9+-.\(\)<>=&%!*\^\/]',str)
        if f:
            raise Exception ('Wrong parameter to Eval : ' + str)
            return 0
        #str = str.replace('!','not ')
        #str = str.replace('=','==')
        #print '>>' + str
        return eval(str)
        
        
class fonction(object):
    def __init__(self, name,param, data,c = False):
        self.name = name
        self.code = data
        self.param = param
        self.const = c
        self.native = False
        
        if data == '':
            self.native = True
        
    def ToStr(self):
        return 'function ' + self.name + '(' + str(self.param)[1:-1] + ') {'+ self.code + '}'
    
class JsParser(object):

    def __init__(self):
        self.Unicode = False
        self.HackVars = []
        self.debug = False
        self.LastEval = ''
        self.SpecialOption = ''
        
        self.Return = False
        self.Break = False
        self.continu = False
        self.ForceReturn = False
        
                        
    def SetReturn(self,r,v):
        self.Return = True
        self.RecursionReturn = r
        self.ReturnValue = v
    
    def AddHackVar(self,name, value):
        self.HackVars.append((name,value))
        
    def GetVarHack(self,name):
        return self.GetVar(self.HackVars,name)
        
    def PrintVar(self,vars):
        for i,j in vars:
            print i + ' : ' + str(j)
    
    #Need to take care at chain var with " and '
    def ExtractFirstchain(self,string):

        #print string.encode('ascii','replace')
    
        if len(string.strip()) == 0:
            return '',0
    
        l = len(string)
        string = string + ' ' #To prevent index out of range, hack
        
        i = -1
        p = 0 #parenbthese
        a = 0 #accolade
        b = 0 #bracket
        f = False #fonction ?
        r = False #Regex
        com1 = False
        com2 = False
        prev = '' #previous char
        c1 = 0 #string with "
        c2 = 0 #string with '
        
        stringR = ''
        
        while (l > i):
        
            i = i + 1
            
            #ignore comment
            if string[i:(i+2)] == '/*':
                com1 = True
            if (com1):
                if string[i:(i+2)] == '*/':
                    com1 = False
                    i = i + 1
                continue
            if string[i:(i+2)] == '//' and  not (r):
                com2 = True
            if (com2):
                if string[i] == '\n':
                    com2 = False
                else:
                    continue

            ch = string[i]
         
            if ch == '(':
                p = p + 1
            if ch == ')':
                p = p - 1
            if ch == '{':
                a = a + 1
            if ch == '}':
                a = a - 1
            if ch == '[':
                b = b + 1
            if ch == ']':
                b = b - 1
            if (r) and ch == '/':
                r = False
            if ch == '/' and prev == '=':
                r = True
            if ch == '"' and not GetPrevchar(string,i) == '\\' and not c2:
                c1 = 1 - c1
            if ch == "'" and not GetPrevchar(string,i) == '\\' and not c1:
                c2 = 1 - c2
                
            #vire espace inutile
            if ch.isspace() and not c1 and not c2:
                if not( prev in ALPHA and GetNextchar(string,i) in ALPHA ):
                    continue
                
            stringR = stringR + ch
                
            #memorise last char
            if not ch.isspace():
                prev = ch               
                               
            #Dans tout les cas les parenthses doivent etre fermees, ainsi que les crochet
            if (p == 0) and (b == 0):
                #Si on rencontre un ; par defaut
                if (ch == ';') and not (f):
                    #Ok, accolade fermees aussi, c'est tout bon
                    if (a == 0):
                        return stringR,i
                    #Accoloade non fermee, c'est une fonction
                    else:
                        f = True
                #si c'est une fonction et l'accolade fermee
                if (f) and (a == 0):
                
                    #quel est le caractere suivant ?
                    j = i + 1
                    while (string[j].isspace()) and(l > j):
                        j = j + 1
                    #Si parenthese on repart
                    if string[j] == '(':
                        continue
                    
                    # Mal formated string ?
                    # Sometime, coder forget the last ; before the }
                    # Desactived for the moment, because can bug in 'a = {};'
                    if False:
                        j = -2            
                        while (stringR[j].isspace()) or (stringR[j] == '}'):
                            j = j - 1
                        if not (stringR[j] == ';'):
                            j = j + 1
                            stringR = stringR[:j] + ';' + stringR[j:]
                        
                    # if there is a last ; add it
                    if string[i+1] == ';':
                        stringR = stringR + ';'
                        i = i + 1

                    return stringR,i
        
        #chaine bugguée ?
        if ';' not in string:
            #out('ERROR Extract chain without ";" > ' + string )
            return string.rstrip() + ';', i
            
        raise Exception("Can't extract chain " + string)

    #Everything Without a "Real" is False   
    def CheckTrueFalse(self,string):
        #out( '> Check True or false : ' + str(string) )

        if isinstance(string, ( bool ) ):
            if string == True:
                return True       
        elif (isinstance(string, types.StringTypes)):
            if not string == '':
                return True
        if isinstance(string, ( int, long , float) ):
            if not (string == 0):
                return True
        if isinstance(string, ( list, tuple) ):
            if not (string == []):
                return True
        return False
        
    def evalJS(self,JScode,vars,allow_recursion):
    
        if allow_recursion < 0:
            raise Exception('Recursion limit reached')
            
        allow_recursion = allow_recursion - 1

        #plus que la chaine a evaluer
        JScode = JScode.strip()
        
        debug = JScode
        
        out( '-------------')
        out( str(allow_recursion) + ' : A evaluer >'+ JScode + '<\n')
            
        #********************************************************
        
        InterpretedCode = JSBuffer()
        
        while (len(JScode)>0):
            c = JScode[0]

            #print 'InterpretedCode > ' + InterpretedCode
            out( 'JScode > ' + JScode.encode('ascii','replace') + '\n')

            #Alpha chain
            if c == '"':
                ee = GetItemAlone(JScode[0:],'"')
                e = len(ee) - 1
                vv = JScode[1:e]
                if vv[-1:] == '\\' and  not vv[-2:-1] == '\\':
                    vv = vv + '\\'
                vv = vv.decode('string-escape')
                #if it's not the form "abc".err
                if not GetNextchar(JScode,e) == '.':
                    InterpretedCode.AddValue(vv)
                    JScode = JScode[(e+1):]
                    continue
                else:
                    self.SetVar(vars,'TEMPORARY_VARS',vv)
                    JScode = 'TEMPORARY_VARS' + JScode[(e+1):]
            if c == "'":
                ee = GetItemAlone(JScode[0:],"'")
                e = len(ee) - 1
                vv = JScode[1:e]
                if vv[-1:] == '\\' and  not vv[-2:-1] == '\\':
                    vv = vv + '\\'
                vv = vv.decode('string-escape')                
                #if it's not the form "abc".err
                if not GetNextchar(JScode,e ) == '.':
                    InterpretedCode.AddValue(JScode[1:e])
                    JScode = JScode[(e+1):]
                    continue
                else:
                    self.SetVar(vars,'TEMPORARY_VARS',JScode[1:e])     
                    JScode = 'TEMPORARY_VARS' + JScode[(e+1):]
                    
            #numeric chain
            r = re.search('(^[0-9]+)',JScode)
            if r:
                InterpretedCode.AddValue(int(JScode[0:r.end()]))
                JScode = JScode[(r.end()):]
                continue
            #Regex
            r = re.search('^\/.*\/(.*$)',JScode)
            if r:
                reg = r.group(0)
                flag = r.group(1)
                #test if the regex is valid
                if flag:
                    for i in flag:
                        if i not in 'gimuy':
                            reg = None
                            break
                InterpretedCode.AddValue(reg)
                JScode = JScode[(len(r.group(0))):]
                continue            
            #parentheses
            if c == "(":
                pos2,c2 = GetBeetweenChar(JScode,'(',')')
                #useless parenthese ?
                if re.match(r'^[\w]+$',c2,re.UNICODE):
                    JScode = c2 + JScode[(pos2 + 1):]
                    continue              
                v = self.evalJS(c2,vars,allow_recursion)
                InterpretedCode.AddValue(v)
                JScode = JScode[(pos2 + 1):]
                continue
            #braket BUGGED
            if c == "[":
                pos2,c2 = GetBeetweenChar(JScode,'[',']')
                v = self.evalJS(c2,vars,allow_recursion)
                if v == 'constructor':
                    v2 = InterpretedCode.GetPrevious()
                    v3 = GetConstructor(v2)
                    InterpretedCode.AddValue(v3)
                elif CheckType(v) == 'Numeric':
                    v2 = InterpretedCode.GetPrevious()
                    InterpretedCode.AddValue(v2[int(v)])
                elif InterpretedCode.CheckString():
                    v2 = InterpretedCode.GetPrevious()
                    try:
                        InterpretedCode.AddValue(v2[v])
                    except:
                        bb(mm)
                else:
                    InterpretedCode.AddValue([])
                JScode = JScode[(pos2 + 1):]
                continue           
                
            #hackVars
            r = re.search('^\$\("#([\w]+)"\)\.text\(\)',JScode)
            if r:
                InterpretedCode.AddValue(self.GetVar(self.HackVars,r.group(1)))
                JScode = JScode[(r.end()):]
                continue
                
            #remove useless code
            if JScode.startswith('new '):
                JScode = JScode[4:]
                continue
                
            #Special value
            m = re.search('^(true|false)',JScode, re.UNICODE)
            if m:
                v = m.group(1)
                if v == 'true':  
                    InterpretedCode.AddValue(True)
                if v == 'false':
                    InterpretedCode.AddValue(False)
                JScode = JScode[len(v):]
                continue
                
            name = ''            
            #Extraction info
            m = re.search(r'^(?:([\w]+)\.)*([\w]+(?:\[[^\]]+\])*) *\(', JScode,re.DOTALL | re.UNICODE)
            #Syntax > aaaaaa.bbbbbb(cccccc) ou bbbb(cccc) ou "aaaa".bb(ccc) ou aa[bb](cc)
            if m:
                name == ''
                if m.group(1):
                    name = m.group(1)
                function = m.group(2)
                pos3,arg = GetBeetweenChar(JScode[(m.end()-1):],'(',')')

                out( 'DEBUG EVAL > Name: ' + Ustr(name) + ' arg: ' + Ustr(arg) + ' function: ' + Ustr(function) )
             
                if function:
                    
                    out( "> function: " + function + ' arg=' + arg)
                    
                    #Definite function ?
                    fe = self.IsFunc(vars,function)

                    if fe:
                        if fe.native:
                            function = fe.name
                            out( "> function (native): " + function + ' arg=' + arg)
                        else :
                            out('> fonction definie par code : ' + function)
                            n,p,c,ct = fe.name,fe.param,fe.code,fe.const
                            a = MySplit(arg,',',True)
                            a2 = []
                            #out('code de la fonction : ' + c)
                            
                            if ct:
                                #hack
                                #Make replacement
                                JScode = n + '(' +arg + ')' + JScode[(len(m.group(0)) + pos3 + 0):]
                                continue

                            for i in a:
                                vv = self.evalJS(i,vars,allow_recursion)
                                a2.append(self.RemoveGuil(vv))
                            
                            if (len(p) > 0) and (len(a2)>0):
                                nv = tuple(zip(p, a2))
                                for z,w in nv:
                                    self.SetVar(vars,z,w)

                            v = self.Parse(c,vars,allow_recursion)
                            
                            if self.Return:
                                self.Return = False
                                InterpretedCode.AddValue(v)
                                
                            JScode = JScode[(len(m.group(0)) + pos3 + 0):]
                            continue
                    
                    #array
                    if function=='Array':
                        InterpretedCode.AddValue([])
                        JScode = JScode[(len(m.group(0)) + pos3):]
                        continue
   
                    #Native
                    #charCodeAt
                    if function=='charCodeAt':
                        s = self.GetVar(vars,name)
                        v = self.evalJS(arg,vars,allow_recursion)
                        InterpretedCode.AddValue(ord(s[int(v)]))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #length
                    if function=='length':
                        s = self.GetVar(vars,name)
                        InterpretedCode.AddValue(len(s))
                        JScode = JScode[(len(m.group(0)) + pos3):]
                        continue
                    #parseInt
                    if function=='parseInt':
                        arg = MySplit(arg,',')
                        t1 = self.evalJS(arg[0],vars,allow_recursion)
                        t2 = self.evalJS(arg[1],vars,allow_recursion)
                        r = int(t1,int(t2))
                        InterpretedCode.AddValue(r)
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue                   
                    #Substring
                    if function=='substring':
                        s = self.GetVar(vars,name)
                        arg = MySplit(arg,',')
                        p1 = self.evalJS(arg[0],vars,allow_recursion)
                        if len(arg)> 1:
                            p2 = self.evalJS(arg[1],vars,allow_recursion)
                            InterpretedCode.AddValue(s[ int(p1) : int(p2) ])
                        else:
                            InterpretedCode.AddValue(s[ int(p1) :])
                        #out('Substring : var = ' + s + ' index=' + str(p1) )
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #join
                    if function=='join':
                        t = arg.replace('"','').replace("'","")
                        s = self.GetVar(vars,name)
                        #out('Join : avec ' + str(t) + 'var = ' + str(s))
                        InterpretedCode.AddValue(t.join(s))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #replace
                    #print re.sub('1',lambda m: f(m.group()),s)
                    if function=='replace':
                        arg = MySplit(arg,',')
                        t1 = arg[0]
                        t2 = self.evalJS(arg[1],vars,allow_recursion)
                        
                        s = self.GetVar(vars,name)
                        
                        if not t1.startswith('/'):
                            t1 = self.evalJS(t1,vars,allow_recursion)
                            
                        #regex mode ?
                        if t1.startswith('/'):

                            jr = re.findall(t1.split('/')[1], s)

                            for k in jr:
                                out('replace ' + str(t2))
                                if not self.IsFunc(vars,t2):
                                    #print str(k) + ' > ' + str(t2)
                                    s = s.replace(k,t2)
                                else:
                                    v = self.evalJS(t2+'('+ k + ')',vars,allow_recursion)
                                    v = str(v)
                                    s = s.replace(k,v)
                            InterpretedCode.AddValue( s )
                        #String mode
                        else:
                            #t1 = self.evalJS(t1,vars,func,allow_recursion)
                            InterpretedCode.AddValue( s.replace(t1,t2))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #slice
                    if function=='slice':
                        s = self.GetVar(vars,name)
                        arg = arg.split(',')
                        p1 = self.evalJS(arg[0],vars,allow_recursion)
                        if len(arg)> 1:
                            p2 = self.evalJS(arg[1],vars,allow_recursion)
                            sr = s[int(p1):int(p2)]
                        else:
                            sr = s[int(p1):]
                        sr = '"' + sr + '"'
                        InterpretedCode.AddValue(sr)
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #string.fromCharCode
                    if (function=='fromCharCode') and (name=='String'):
                        v = self.evalJS(arg,vars,allow_recursion)
                        #out('StringFromCharcode ' +  r.group(1) + '=' + str(v))
                        InterpretedCode.AddValue(chr(int(v)))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #split
                    if function=='split':
                        arg = arg.replace('"','').replace("'","")
                        s = self.GetVar(vars,name)
                        if arg == '':
                            InterpretedCode.AddValue(list(s))
                        else:
                            InterpretedCode.AddValue(s.split(arg))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #splice
                    if function=='splice':
                        s = self.GetVar(vars,name)
                        arg = MySplit(arg,',')
                        t1 = self.evalJS(arg[0],vars,allow_recursion) + 1
                        t2 = self.evalJS(arg[1],vars,allow_recursion) 
                        if len(arg) > 2:
                            raise Exception("Not implemented - splice")
                        tab = s[:t1] + s[(t1 + t2):]
                        tabsup = s[t1:(t1 + t2)]
                        InterpretedCode.AddValue(tabsup)
                        self.SetVar(vars,name,tab)

                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #push
                    if function=='push':
                        s = self.GetVar(vars,name)
                        arg = MySplit(arg,',')
                        t1 = self.evalJS(arg[0],vars,allow_recursion)
                        if len(arg) > 1:
                            #use s.extend-[array]);
                            raise Exception("Not implemented - push")
                        s.append(t1)
                        self.SetVar(vars,name,s)
                        #self.VarManage(allow_recursion,vars,name,str(s))
                        v = len(s)
                        InterpretedCode.AddValue(v)
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue                        
                    #math function
                    #max
                    if function=='max':
                        arg = MySplit(arg,',')
                        t1 = self.evalJS(arg[0],vars,allow_recursion)
                        t2 = self.evalJS(arg[1],vars,allow_recursion)
                        InterpretedCode.AddValue(max(t1,t2))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #min
                    if function=='min':
                        arg = MySplit(arg,',')
                        t1 = self.evalJS(arg[0],vars,allow_recursion)
                        t2 = self.evalJS(arg[1],vars,allow_recursion)
                        InterpretedCode.AddValue(min(t1,t2))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue                        
                    #function
                    if function=='function':
                        pos9 = len(JScode[(len(m.group(0)) + pos3 + 0):])
                        v = self.MemFonction(vars,'',arg,False,JScode[(len(m.group(0)) + pos3 + 0):])[2]
                        pos3 = pos3 + pos9
                        InterpretedCode.AddValue(v)
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #RegExp
                    if function=='RegExp':
                        arg = MySplit(arg,',')
                        t1 = self.evalJS(arg[0],vars,allow_recursion)
                        t2 = self.evalJS(arg[1],vars,allow_recursion)
                        InterpretedCode.AddValue('/' + self.RemoveGuil(t1) + '/' + self.RemoveGuil(t2))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue             
                    #alert
                    if function=='alert':
                        print '------------ALERT-------------------'
                        print arg
                        print '------------------------------------'
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #debug
                    if function=='debug':
                        print '------------------------------------'
                        self.PrintVar(vars)
                        print '------------------------------------'
                        raise Exception("DEBUG")
                    #constructor
                    if function=='Function':
                        #pos9 = len(JScode[(len(m.group(0)) + pos3 + 0):])
                        NewCode = self.evalJS(arg,vars,allow_recursion)

                        v = self.MemFonction(vars,'','',False,'{'+ NewCode + '}')[2]
                        #pos3 = pos3 + pos9
                        #InterpretedCode.AddValue(v)
                        JScode = v + JScode[(len(m.group(0)) + pos3 ):]
                        continue
                    #eval ?
                    if function=='eval':
                        out('Eval')
                        out('To eval >' + arg)
                        self.ForceReturn = True
                        r = self.Parse(arg,vars,allow_recursion)
                        JScode = r + JScode[(len(m.group(0)) + pos3 ):]
                        continue

                    print vars
                    raise Exception("Unknow fonction : " + function)
                    
            #TODO hack inside
            if InterpretedCode.type == 'String':
                if c == '.':
                    self.SetVar(vars,'TEMPORARY_VARS',InterpretedCode.GetPrevious())
                    JScode = 'TEMPORARY_VARS' + JScode
                    continue


            #variables
            m = re.search('^(\({0,1}\w[\w\.]*\){0,1} *(?:\[[^\]]+\])* *)(' + REG_OP + '|$)',JScode, re.UNICODE)
            if m:
                v = m.group(1).strip()
                pos7 = len(m.group(1))
                
                if self.IsVar(vars,v):
                    r = self.GetVar(vars,v)

                    op = ''
                    if len(m.groups()) > 1:
                        op = m.group(2).strip()

                    out("> var " + v + "=" + str(r))
                    
                    if self.IsVar(vars,v):
                        #just var
                        if len(op) < 2:
                            pass
                        #if !=
                        elif op == '!=':
                            pass
                        #check if it's i++ ou i -- form
                        elif op == '++':
                            self.SetVar(vars,v,r + 1)
                            pos7+=2
                        elif op == '--':
                            self.SetVar(vars,v,r-1)
                            pos7+=2
                        #a == 1
                        elif (op == '||') or (op == '&&'):
                            #InterpretedCode.AddValue(r)
                            #InterpretedCode.SetOp(op[0])
                            pos7+=1
                        #a+=1 form
                        elif op[1] == '=' and not op[0] == '=':
                            n = GetItemAlone(JScode[m.end():],' ' + REG_OP)
                            if op[0] == '+':
                                r = self.evalJS(v+'+'+n ,vars,allow_recursion)
                            elif op[0] == '-':
                                r = self.evalJS(v+'-'+n ,vars,allow_recursion)
                            elif op[0] == '*':
                                r = self.evalJS(v+'*'+n ,vars,allow_recursion)
                            elif op[0] == '/':
                                r = self.evalJS(v+'/'+n ,vars,allow_recursion)                            
                            self.SetVar(vars,v,r)
                            l = len(n) + 2
                            pos7 = pos7 + l
                                
                        InterpretedCode.AddValue(r)       
                        JScode = JScode[pos7:]
                        
                        # A new variable ?
                        if len(JScode) > 0:
                            if JScode[1] == ',':
                                rr(pp)
                        
                        continue
                        
                    raise Exception("Can't find var " + r.group(1))

                
            #Space to remove
            if c == ' ' or c == '\n':
                JScode = JScode[1:]
                continue
                
            #Escape char
            if c == '\\':
                JScode = JScode[1:]
                continue
                
            #Special if (A)?(B):(C)
            if c == '?':
                out( " ****** Special if 1 ********* ")
                #need to find all part
                A = InterpretedCode.GetPrevious()
                B = GetItemAlone(JScode,':')
                C = GetItemAlone(JScode[len(B):])
                
                Totlen = len(B) + len(C)
                B = B[1:-1]
                if B.startswith('('):
                    B = B[1:-1]
                if C.startswith('('):
                    C = C[1:-1]               
                if A:
                    r = self.Parse(B,vars,allow_recursion)
                else:
                    r = self.Parse(C,vars,allow_recursion)

                InterpretedCode.AddValue(r)
                JScode = JScode[Totlen :]
                continue

            #another special if
            if JScode[0:2] == '&&':
                out( " ****** Special if 2 ********* ")
                A = InterpretedCode.GetPrevious()
                B = GetItemAlone(JScode[2:])
                
                Totlen = len(B) + 2
                if B.startswith('('):
                    B = B[1:-1]
                if A:
                    r = self.Parse(B,vars,allow_recursion)
                    
                #InterpretedCode.AddValue(r)
                JScode = JScode[Totlen :]
                continue                    
                
            #Simple operation
            if c in '+<>-*/=&%|!^.':
                InterpretedCode.SetOp(c)
                JScode = JScode[1:]
                continue      
                
            #No sure how to put this
            if JScode == '{}':
                InterpretedCode.AddValue({})
                JScode = JScode[2:]
                continue
            if JScode == '[]':
                InterpretedCode.AddValue([])
                JScode = JScode[2:]
                continue
        
            #???
            if JScode == ';':
                JScode = JScode[1:]
                continue
                
            # pointeur vers fonction ?
            if JScode == 'parseInt':
                fm = fonction('parseInt','','')
                #self.SetVar(vars,name,fm)
                InterpretedCode.AddValue(fm)
                JScode = ''
                continue
                
            # Not found part
            # We will make another turn
            self.PrintVar(vars)
            out("Can't eval string :" + JScode)
            out("Last eval : " + str(self.LastEval))

            #print debug.encode('ascii','replace')
            raise Exception(str(allow_recursion) + " : Can't Eval chain : " + JScode)


        InterpretedCode2 = InterpretedCode.GetBuffer()
        
        out( str(allow_recursion) + ' : Evalue > '+ Ustr(InterpretedCode2) + " type " + Ustr(type(InterpretedCode2)) )
        out( '-------------')

        self.LastEval = InterpretedCode2
        return InterpretedCode2
        
    def RemoveGuil(sel,string):
        if not (isinstance(string, types.StringTypes)):
            return string
        string = string.strip()
        if string.startswith('"') and string.endswith('"'):
            return string[1:-1]
        if string.startswith("'") and string.endswith("'"):
            return string[1:-1]            
        return string
        
    def InitVar(self,var,variable):
        variable = variable.strip()
    
        for j in var:
            if j[0] == variable:
                var.remove(j)
                return
    
        
    def GetVar(self,var,variable):
    
        variable = variable.strip()
        
        index = None
        if '[' in variable:
            index = variable.split('[')[1][:-1]
            variable = variable.split('[')[0]
            index = self.evalJS(index,var,50)
            
        if '.' in variable:
            index = variable.split('.')[1]
            variable = variable.split('.')[0]  
            
        for j in var:
            if j[0] == variable:
                r = j[1]
                if not(index == None):
                    if type(r) in [list,tuple]:
                        if CheckType(index) == 'Numeric':
                            if int(index) < len(r):
                                r = r[int(index)]
                            else:
                                r = 'undefined'
                        elif CheckType(index) == 'String':
                            index = self.RemoveGuil(index)
                            r = r[index]
                    if type(r) in [dict]:
                        index = self.RemoveGuil(index)
                        r = r[index]                   
                return r
                
        raise Exception('Variable not defined: ' + variable)
            
    def SetVar(self,var,variable,value,i = 0):
    
        #print 'Setvar Variable =' + variable + ' value=' + str(value) + ' index=' + str(i)

        variable = variable.strip()
        
        #cleaning
        if variable[0] == '(':
            variable = variable[1:-1]

        #Existing var ?
        for j in var:
            if j[0] == variable:

                #vars ?
                if (isinstance(var[var.index(j)][1], types.StringTypes)):
                    var[var.index(j)] = (variable,value)
                #Array 
                elif type(var[var.index(j)][1]) in [list,tuple]:

                    Listvalue = var[var.index(j)][1]

                    #ok this place doesn't esist yet
                    l = int(i) - len(Listvalue) + 1
                    while l > 0:
                        Listvalue.append('undefined')
                        l = l - 1
                    #Now modify it
                    if type(value) in [list,tuple]:
                        Listvalue = value
                    else:
                        Listvalue[int(i)] = value
                    var[var.index(j)] = (variable,Listvalue)
                #dictionnary
                elif type(var[var.index(j)][1]) in [dict]:
                    Listvalue = var[var.index(j)][1]
                    Listvalue[i] = value
                    var[var.index(j)] = (variable,Listvalue)                
                #Numeric
                else:
                    var[var.index(j)] = (variable,value)

                return
                
        #New var
        var.append((variable,value))
    
    def IsVar(self,var,variable):
        try:
            variable = variable.split('[')[0]
            variable = variable.split('.')[0]
            for j in var:
                if j[0] == variable:
                    return True
            return False
        except:
            return False
        
    #Need to use metaclass here
    def IsFunc(self,vars,name):
        bExist = False
        bExist = self.IsVar(vars,name)
        if not bExist:
            return False
            
        f = self.GetVar(vars,name)
        if isinstance(f, fonction):
            return f
        else:
            return self.IsFunc(vars,f)
        
    def VarManage(self,allow_recursion,vars,name,value=None):

        index = None
        init = False
        
        try:
            value = value.strip()
        except:
            pass
        name = name.strip()
        
        #variable is an object
        if '.' in name:
            index = name.split('.')[1]
            name = name.split('.')[0]
        #Variable is an array ?
        m = re.search(r'^\({0,1}([\w]+)\){0,1}\[(.+?)\]$', name,re.DOTALL | re.UNICODE)
        if m:
            name = m.group(1)
            index = m.group(2)
            index = self.evalJS(index,vars,allow_recursion)
            
        if name.startswith('('):
            name = name[1:-1].strip()
            
        #Error check
        if '+' in name:
            raise Exception('Variable problem')
  
        if value:
            if isinstance(value, ( int, long , float) ):
                value = self.evalJS(value,vars,allow_recursion)
            else:
                #Values is an array []
                if value.startswith('[') and value.endswith(']'):
                    value = value[1:-1]
                    
                    valueT = MySplit(value,',')
                    v = []
                    for k in valueT:
                        v2 = self.evalJS(k,vars,allow_recursion)
                        v.append(v2)
                    value = v
                    if index == None:
                        index = 0
                        init = True
                #Values is an array {}
                elif value.startswith('{') and value.endswith('}'):
                    value = value[1:-1]
                    valueT = MySplit(value,',',True)
                    v = {}
                    for k in valueT:
                        l = k.split(':')
                        #WARNING : no eval here in JS
                        #v2g = self.evalJS(l[0],vars,func,allow_recursion)
                        v2g = self.RemoveGuil(l[0])
                        v2d = self.evalJS(l[1],vars,allow_recursion)
                        v[v2g] = v2d
                    value = v
                    if index == None:
                        index = 0
                        init = True
                             
                else:
                    value = self.evalJS(value,vars,allow_recursion)
                

        name = name.strip()


        #Output for debug
        if not (index == None):
            out( '> Variable in parser => ' + Ustr(name) + '[' + Ustr(index) + ']' + ' = ' + Ustr(value))
        else:
            out( '> Variable in parser => ' + Ustr(name) + ' = ' + Ustr(value))
                           
        #chain
        if (isinstance(value, types.StringTypes)):
            self.SetVar(vars,name,value,index)
        #number
        elif isinstance(value, ( int, long , float) ):
            self.SetVar(vars,name,value,index)
        #list
        elif type(value) in [list,tuple,dict]:
            if init:
                self.InitVar(vars,name)
            self.SetVar(vars,name,value,index)
        #fonction
        elif isinstance(value, fonction):
            self.SetVar(vars,name,value,index)        
        #undefined
        elif value == None:
            self.SetVar(vars,name,None,index)
        else:
            print type(value)
            raise Exception('> ERROR : Var problem >' + str(value))
        return
        

    #(Function(arg){code})(arg2) Self invoked
    # Function(arg){code}(arg2)  Not self invoked 
    def MemFonction(self,vars,name,parametres,selfinvoked,data):
    
        if not name:
            n0 = 0
            while self.IsFunc(vars,'AnonymousFunc' + str(n0)):
                n0=n0+1
            name = 'AnonymousFunc' + str(n0)
            
        if (self.SpecialOption):
            if self.SpecialOption.split('=')[0] == 'Namefunc':
                name = self.SpecialOption.split('=')[1]
            self.SpecialOption = ''
             
        param = MySplit(parametres,',',True)
        
        out('Extract function :' + name + ' Selfinvok :' + str(selfinvoked) + ' ' + str(param))
        #out('data ' + str(data))
        
        pos = 0
        replac = ''
        
        pos2,content = GetBeetweenChar(data,'{','}')
        #out('content ' + str(content))
        pos = pos2 + 1

        fm = fonction(name,param,content.lstrip())
        self.SetVar(vars,name,fm)
        
        #self invoked ? Not working yet
        if selfinvoked:
            pos = data.find(')',pos) + 1
            data = data[pos:]
        else:
            data = data[pos:] 

        #param in function ?
        if len(data)> 0:
            r = name + data
            if not data.endswith(';'):
                r = r + ';'
            replac = r

            pos = pos + len(data)
          
        return replac, pos , name
        
    def Parse(self,JScode,vars,allow_recursion=MAX_RECURSION):
    
        if allow_recursion < 0:
            raise Exception('Recursion limit reached')
            
        allow_recursion = allow_recursion - 1
    
        #************************
        #    Post traitement
        #************************
        
        #Need all functions first, because they can be called first and be at the bottom of the code
        #So we extract all functions first, and replace them by a simple call in the code, if they are self invoked
        
        posG = 0
        Startoff = 0
        Endoff = 0
        
        while (True):

            chain,pos = self.ExtractFirstchain(JScode[posG:])
            if not (chain):
                break
            
            Startoff = posG
            Endoff = posG + pos + 1
            posG = Endoff
            
            #skip empty char
            chain = chain.strip()
             
            #out('/////////////////')
            #out('> ' + chain)
            #out('/////////////////')
            
            #fonction
            m = re.search(r'^(\()* *function(?: ([\w]+))* *\(([^\)]*)\) *{', chain,re.DOTALL)
            if m:
                name = ''
                selfinvoked = False
                if m.group(2):
                    name = m.group(2)
                if m.group(1):
                    selfinvoked = True
            
                replac,pos3,xyz = self.MemFonction(vars,name,m.group(3),selfinvoked,chain)
                JScode = JScode[:Startoff]+ replac + JScode[Endoff:]

                posG = Startoff + len(replac)

        #***********************
        # The real Parser
        #**********************

        while (True):
        
            if self.continu:
                break;
        
            chain,pos = self.ExtractFirstchain(JScode)
            if not (chain):
                break
                
            JScode = JScode[(pos+1):]
                        
            chain = chain.lstrip()
            chain = chain.rstrip()
            
            #empty ?
            if chain == ';':
                continue
              
            out( 'D++++++++++++++++++' )
            out(chain.encode('ascii','replace') )
            out( 'F++++++++++++++++++')
            
            #hackVars ?
            m = re.search(r'^\$\("#([^"]+)"\)\.text\(([^\)]+)\);', chain)
            if m:
                out( '> hack ' + m.group(0) + ' , variable est ' + m.group(1))
                self.SetVar(self.HackVars,m.group(1),self.GetVar(vars,m.group(2)))
                continue
                
            #useless ( or [
            if chain.startswith('(') or chain.startswith('['):
                out( "Useless () or []" )
                if chain.endswith(');') or chain.endswith('];'):
                    chain = chain[1:-2] + ';'
                
  
            name = ''            
            #Extraction info
            #Problem, catch fonction too :(
            m = re.search(r'^([\w]+) *\(', chain,re.DOTALL)
            #Syntax > aaaaa(bbbbb) .........
            if m:
                name = m.group(1)
                pos3,arg = GetBeetweenChar(chain[(m.end()-1):],'(',')')
                code = chain[(m.end() + pos3):]
                out( 'DEBUG > Name: ' + name + ' arg: ' + arg + ' code: ' + code )
                
                #Jquery
                if name == 'DOCUMENT_READY':
                    out('DOCUMENT_READY ' + arg)
                    self.SpecialOption = 'Namefunc=DR'
                    self.Parse(arg,vars,allow_recursion)

                    #It's not the correct place to do that, but for the moment ...
                    self.Parse('DR();',vars,allow_recursion)
                    
                    continue

                #For boucle ?
                if name == 'for':
                    arg = arg.split(';')
                    v = arg[0] + ';'
                    t = arg[1]
                    i = arg[2] + ';'
                    f = code
                    if GetFirstChar(f) =='{':
                        f = GetBeetweenChar(f,'{','}')[1]
                    
                    #out('> Boucle for : Var=' + v + ' test=' + t + ' incrementation=' + i + ' code=' + f)
                    
                    #init var              
                    self.Parse(v,vars,allow_recursion)
                    #loop
                    while (self.CheckTrueFalse(self.evalJS(t,vars,allow_recursion))):
                        #fonction
                        self.Parse(f,vars,allow_recursion)
                        if self.Break:
                            self.Break = False
                            break
                        #incrementation
                        self.Parse(i,vars,allow_recursion)

                    continue
                    
                #boucle while ?
                if name == 'while':
                    f = code
                    if GetFirstChar(f) =='{':
                        f = GetBeetweenChar(f,'{','}')[1]
                    
                    #out('> Boucle while : Var=' + v + ' test=' + t + ' incrementation=' + i + ' code=' + f)
                    
                    #loop
                    while (self.CheckTrueFalse(self.evalJS(arg,vars,allow_recursion))):
                        #fonction
                        self.Parse(f,vars,allow_recursion)
                        if self.Break:
                            self.Break = False
                            break
                            
                        if self.continu:
                            self.continu = False

                    continue
                    
                #boucle switch
                if name == 'switch':
                    v = self.evalJS(arg,vars,allow_recursion)
                    
                    if v == 'undefined':
                        continue
                    
                    f = code
                    f = f[:-1]
                    p = f.find("case'" + v + "':")
                    
                    out('> Boucle switch : Var=' + v + ' code=' + f + ' position=' + str(p))
                    
                    if p == -1:
                        raise Exception("Can't find switch value " + str(v))
                    f = f[(p + len(v) + 7):]
                    
                    out('> New block : ' + f)
                    
                    self.Parse(f,vars,allow_recursion)
                    
                    continue
                    
                #Boucle if
                if name == 'if':
                    t = arg
                    f = code
                    e = ''
                    
                    if GetFirstChar(f) =='{':
                        f = GetBeetweenChar(f,'{','}')[1]

                    #Need to check if there is else statement ?
                    chain2,pos2 = self.ExtractFirstchain(JScode)
                    if 'else' in chain2:
                        chain2 = chain2.lstrip()
                        JScode = JScode[(pos2 + 1):]
                        m2 = re.search(r'else\s*{(.+?)}$', chain2,re.DOTALL)
                        if m2:
                            e = m2.group(1)
                    
                    #out('> Boucle if : test=' + arg + ' code=' + f + ' else=' + e)
                    if (self.CheckTrueFalse(self.evalJS(t,vars,allow_recursion))):
                        self.Parse(f,vars,allow_recursion)
                    elif (e):
                        self.Parse(e,vars,allow_recursion)
                    continue  

            #Variable operation/creation/modification ?
            m =  re.search(r'^\({0,1}([\w\.]+)\){0,1}(?:\[([^\]]+)\])*\){0,1}\s*(?:[\^\/\*\-\+])*=',chain,re.DOTALL | re.UNICODE)
            m2 = re.search(r'^\({0,1}([\w\.]+)\){0,1}(?:\.([\w]+))*\){0,1}\s*(?:[\^\/\*\-\+])*=',chain,re.DOTALL | re.UNICODE)
            if m or chain.startswith('var ') or m2:
                out('var')

                if chain.startswith('var '):
                    chain = chain[4:]
                
                #Now need to extract all vars from chain
                while (chain):
                    
                    v1 = GetItemAlone(chain,',').strip()

                    chain=chain[(len(v1)):]
                    if v1.endswith(',') or v1.endswith(';'):
                        v1 = v1[:-1]
                        
                    #A=B=C=8,A=1
                    if '=' in v1:
                        t3 = GetItemAlone(v1,'=')
                        #just '='
                        if v1[(len(t3)) - 2] not in '+-*/^':
                            t1 = []
                            while v1:
                                t3 = GetItemAlone(v1,'=')
                                v1 = v1[(len(t3)):]
                                if t3.endswith('='):
                                    t3 = t3[:-1]
                                t1.append(t3.strip())

                            l = len(t1) - 2
                            while ( l >= 0 ):
                                self.VarManage(allow_recursion,vars,t1[l],t1[l+1])
                                l = l - 1
                        #+= ou /= or other
                        else:
                            ope = v1[(len(t3)) - 2]
                            t2 = t3[:-2]
                            v1 = v1[(len(t3)):]
                            t3 = GetItemAlone(v1,'=')
                            r = self.evalJS(t2+ope+t3 ,vars,allow_recursion)
                            self.VarManage(allow_recursion,vars,t2,str(r))
                    #A,B,C
                    else:
                        self.VarManage(allow_recursion,vars,v1,None)
                                    
                continue
  
            #break
            if chain.startswith('break'):
                self.Break = True
                return
                
            #continue
            if chain.startswith('continue'):
                self.continu = True
                return
            
            #Return ?                
            if chain.startswith('return'):
                m = re.match(r'return *;', chain)
                if m:
                    self.Return = True
                    return None
                m = re.match(r'^return *([^;]+)', chain)
                if m:
                    chain = m.group(1)
                    r = self.evalJS(chain,vars,allow_recursion)
                    self.Return = True
                    return r              
                    

            #Pas trouve, une fonction ?
            if chain.endswith(';'):
                rrr = self.evalJS(chain[:-1],vars,allow_recursion)
                if self.ForceReturn:
                    self.ForceReturn = False
                    return rrr
            
            #Non gere encore
            #print '> ' + JScode
            #raise Exception('> ERROR : can t parse >' + chain)
            
        return

    def ProcessJS(self,JScode,vars = []):
        vars_return = []
        
        #unicode ?
        #if isinstance(JScode, unicode):
        if (False):
            out('Unicode convertion')
            JScode = unicode(JScode, "utf-8")
            self.Unicode = True
        
        #Special
        vars.append(('String',''))
        vars.append(('true',True))
        vars.append(('false',False))
        
        #Hack
        JScode = JScode.replace('$(document).ready','DOCUMENT_READY')
        JScode = JScode.replace('.length','.length()')
        
        #Start the parsing
        ret = self.Parse(JScode,vars)
        
        #Memorise vars
        
        
        return ret

        
#---------------------------------------------------------------------------------------------------------------------------------------- 

#main


# -*- coding: utf-8 -*- 
#s = "abcşiüğ"
#my_unicode_string = unicode(s, "utf-8")
#print my_unicode_string[3].encode('utf-8')
#print ord(my_unicode_string[3])

JP = JsParser()
Liste_var = []

#JP.AddHackVar('aQydkd1Gbfx',"u'@D||&FBgHO`cfggghaddOb`]bg]_]_OE59ys33I")
#print 'Return : ' + str(JP.ProcessJS(JScode))
JP.ProcessJS(JScode,Liste_var)
print 'Decoded url : ' + JP.GetVar(Liste_var,'Result')



