# -*- coding: utf-8 -*- 
#
# Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
#

#******************************
#   A Basic Javascript Parser/Interpreter
#******************************

# TODO LIST
# ---------
# Regex will work only for normal name, not for exotic name
# Object
# Globla/Local variables/function/object
# utiliser un tableau special pr variable passe en parametrzs > clash


#help
#https://sarfraznawaz.wordpress.com/2012/01/26/javascript-self-invoking-functions/
#https://nemisj.com/python-api-javascript/
#https://fr.wikiversity.org/wiki/Python/Les_types_de_base
#https://javascriptobfuscator.com/Javascript-Obfuscator.aspx
#https://nemisj.com/python-api-javascript/

#UNICODE ERROR
#print a.decode('utf-8').encode('ascii','replace')
#true = 1 instead of true


#https://javascriptweblog.wordpress.com/2011/04/04/the-javascript-comma-operator/



import re
import types
from types import NoneType
import time

import sys

REG_NAME = '[\w]+'
REG_OP = '[\/\*\-\+\{\}<>\|=~^%!]+' #not space here, and no bracket
DEBUG = True # Never enable it in kodi, too big size log
MAX_RECURSION = 50
ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

#---------------------------------------------------------------------------------

JScode = """
a = eval('1+1') + eval('2+2');
debug();
"""

JScodefdgdg = """
function oIa(_0x41645b,_0x10c153) { return _0x41645b-_0x10c153; }
function EKC(_0x2250c2,_0x1160e6) { return _0x2250c2-_0x1160e6; }
function XzN(_0x283e6a,_0x49206b) { return _0x283e6a(_0x49206b); }
function dFN(_0x422306,_0x51e2dc,_0x230729) { return _0x422306(_0x51e2dc,_0x230729); }
function XcK(_0x2ec800,_0x3087df) { return _0x2ec800/_0x3087df; }
function TYf(_0x42c4ab,_0x3a8e71) { return _0x42c4ab<_0x3a8e71; }
function MEA(_0x1f7e16,_0xe5b384) { return _0x1f7e16%_0xe5b384; }
function FxE(_0x3738d3,_0x36a500,_0x2f551f) { return _0x3738d3(_0x36a500,_0x2f551f); }
function yfs(_0x563f72,_0x3d8b3f) { return _0x563f72-_0x3d8b3f; }
function bqe(_0x526965,_0x84a7b0) { return _0x526965!=_0x84a7b0; }
function rZh(_0x1e74c2,_0x24ac16) { return _0x1e74c2%_0x24ac16; }
function OLB(_0x31b23d,_0x2d246a) { return _0x31b23d==_0x2d246a; }
function tVi(_0x221589,_0x46bf10) { return _0x221589%_0x46bf10; }
function wqo(_0x5e82dd,_0x5e5aae) { return _0x5e82dd==_0x5e5aae; }
function BOg(_0x174a99,_0x52dfc2,_0x254069) { return _0x174a99(_0x52dfc2,_0x254069); }
function WNS(_0xfc1900,_0x9e1420) { return _0xfc1900+_0x9e1420; }
function ZeT(_0x3969f8,_0x48db24) { return _0x3969f8+_0x48db24; }
function xRD(_0x234038,_0x42c6db) { return _0x234038<_0x42c6db; }
var _0x22b8e5='3|6|2|7|4|0|5|1|8'.split('|'),_0x3aae80=0;while(true){
switch(_0x22b8e5[_0x3aae80++]){

case'0':var _0x4ff92f=_0x49dbe3.join(''),_0x3303a2=[];continue;
case'1':
for(var _0x2142d2=0;xRD(_0x4c3948,_0x4ff92f.length);){
var _0x208bb1=_0x4ff92f.substring(_0x4c3948,ZeT(_0x4c3948,2));
var _0x28906b=_0x4ff92f.substring(_0x4c3948,WNS(_0x4c3948,3));
var _0xb1703c=_0x4ff92f.substring(_0x4c3948,WNS(_0x4c3948,4)),_0x306459=BOg(parseInt,_0x208bb1,16);
_0x4c3948+=2,wqo(tVi(_0x2142d2,3),0)?(_0x306459=BOg(parseInt,_0x28906b,8),_0x4c3948+=1):OLB(rZh(_0x2142d2,2),0)&&bqe(0,_0x2142d2)&&xRD(_0x4ff92f[yfs(_0x2142d2,1)].charCodeAt(0),60)&&(_0x306459=FxE(parseInt,_0xb1703c,10),_0x4c3948+=2);
var _0x3a9a19=_0x1701aa[MEA(_0x2142d2,9)];_0x306459^=213,_0x306459^=_0x3a9a19,_0x3303a2.push(String.fromCharCode(_0x306459)),_0x2142d2+=1;
}
continue;
case'2':for(var _0x6594be=_0x22b5f6.substring(_0x21dc81,WNS(_0x21dc81,30)),_0x1701aa=new Array(10),_0x4c3948=0;TYf(_0x4c3948,_0x6594be.length);){
var _0x46b158=_0x6594be.substring(_0x4c3948,WNS(_0x4c3948,3));_0x1701aa[XcK(_0x4c3948,3)]=dFN(parseInt,_0x46b158,8),_0x4c3948+=3;
}
continue;
case'3':var _0x22b5f6='1125737736416423734301622231515467e007035500471b26074004102101035f2207e00153530116201131e00252300052053526900431020004112177a00722340012560704101013550001',_0x53f09a=_0x22b5f6.charCodeAt(0),_0x21dc81=EKC(_0x53f09a,52),_0x3f9f56=Math.max(2,_0x21dc81);continue;
case'4':_0x49dbe3.splice(_0x21dc81,30);continue;
case'5':_0x4c3948=0;continue;
case'6':_0x21dc81=Math.min(_0x3f9f56,oIa(oIa(_0x22b5f6.length,30),2));continue;
case'7':var _0x49dbe3=_0x22b5f6.split('');continue;
case'8':Result=_0x3303a2.join('');continue;
}
break;
}

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

JScode7521 ="""
function(p,a,c,k,e,r){e=String;if(!''.replace(/^/,String)){while(c--)r[c]=k[c]||c;k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('(0(){4 1="5 6 7 8";0 2(3){9(3)}2(1)})();',10,10,'function|b|something|a|var|some|sample|packed|code|alert'.split('|'),0,{});
debug();
"""


JScodesss ="""
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

"""

JScoderfvg ="""
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

def RemoveGuil(string):
    if not (isinstance(string, types.StringTypes)):
        return string
    string = string.strip()
    if string.startswith('"') and string.endswith('"'):
        return string[1:-1]
    if string.startswith("'") and string.endswith("'"):
        return string[1:-1]            
    return string


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
    c1 = 0 #chain with "
    c2 = 0 #chain with '
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
            return ret[:-1]
            
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
        ret = None
        if len(self.buf) > 0:
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
        self.ReturnValue = None
        
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

            #Alpha chain
            if c == '"' or c == "'":
                ee = GetItemAlone(JScode[0:],c)
                e = len(ee)
                vv = JScode[1:e]
                
                # raw string cannot end in a single backslash
                #if vv[-1:] == '\\' and  not vv[-2:-1] == '\\':
                #    vv = vv + '\\'
                    
                #warning with this function
                #if not vv.endswith('\\'):
                #    vv = vv.decode('string-escape')
                
                InterpretedCode.AddValue(vv)
                JScode = JScode[(e+1):]
                continue
                    
            #TODO hack inside
            if c == '.' and InterpretedCode.type == 'String':         
                self.SetVar(vars,'TEMPORARY_VARS',InterpretedCode.GetPrevious())
                JScode = 'TEMPORARY_VARS' + JScode
                continue
                    
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
                
            #hackVars
            r = re.search('^\$\("#([\w]+)"\)\.text\(\)',JScode)
            if r:
                InterpretedCode.AddValue(self.GetVar(self.HackVars,r.group(1)))
                JScode = JScode[(r.end()):]
                continue
                
            #remove "useless" code
            if JScode.startswith('new '):
                JScode = JScode[4:]
                continue
                
            #Special value
            m = re.search('^(true|false|null|String)',JScode, re.UNICODE)
            if m:
                v = m.group(1)
                if v == 'true':  
                    InterpretedCode.AddValue(True)
                if v == 'false':
                    InterpretedCode.AddValue(False)
                if v == 'null':
                    InterpretedCode.AddValue(None)
                if v == 'String':
                    InterpretedCode.AddValue('')
                #if v == 'Array':
                #    InterpretedCode.AddValue([])
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
                        if isinstance(fe, types.MethodType):
                            print fe.im_func.__name__ #parseint
                            print fe.im_class.__name__ #Basic
                            function = fe.im_func.__name__
                            out( "> function (native): " + function + ' arg=' + arg)
                            #and continu with native fonction
                            
                        elif isinstance(fe, fonction):
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
                                a2.append(RemoveGuil(vv))
                            
                            if (len(p) > 0) and (len(a2)>0):
                                nv = tuple(zip(p, a2))
                                for z,w in nv:
                                    self.SetVar(vars,z,w)

                            self.Parse(c,vars,allow_recursion)
                            
                            if self.Return:
                                self.Return = False
                                InterpretedCode.AddValue(self.ReturnValue)
                                self.Return = None
                                
                            JScode = JScode[(len(m.group(0)) + pos3 + 0):]
                            continue
                        else:
                            raise Exception("Strnage fonction")
                            
                    #Native fonction
                    # http://stackoverflow.com/questions/1091259/how-to-test-if-a-class-attribute-is-an-instance-method
                    
                    Find_lib = False
                    for lib in List_Lib:
                        if hasattr(lib, function):
                            arg = MySplit(arg,',')
                            for i in range(len(arg)):
                                arg[i] = self.evalJS(arg[i],vars,allow_recursion)
                            
                            #Lib need init
                            if hasattr(lib, 'Get'):
                                s = self.GetVar(vars,name)
                                cls =  lib(s)
                                r = getattr(cls, function)(arg)
                                #set new value if chnaged, never reached ??
                                NV = getattr(cls, 'Get')()
                                if not NV == s:
                                    self.SetVar(vars,name,NV)
                                    
                            #Classic lib
                            else:
                                r = getattr(lib(), function)(arg)
                                
                            InterpretedCode.AddValue(r)
                            JScode = JScode[(len(m.group(0)) + pos3 ):]
                            
                            Find_lib = True
                            
                            break
                            
                    if Find_lib:
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
                            
                        #regex mode ? HACK
                        if t1.startswith('/'):
                            jr = re.findall(t1.split('/')[1], s)

                            for k in jr:
                                if not self.IsFunc(vars,t2):
                                    s = s.replace(k,t2)
                                    out('Replace ' + str(k) + " by " + str(t2))
                                else:
                                    v = self.evalJS(t2+'('+ k + ')',vars,allow_recursion)
                                    v = str(v)
                                    s = s.replace(k,v)
                                    out('Replace ' + str(k) + " by " + str(v))
                            InterpretedCode.AddValue( s )
                        #String mode
                        else:
                            #t1 = self.evalJS(t1,vars,func,allow_recursion)
                            InterpretedCode.AddValue( s.replace(t1,t2))
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue
                        
                    #array
                    if function=='Array':
                        InterpretedCode.AddValue([])
                        JScode = JScode[(len(m.group(0)) + pos3):]
                        continue
                
                    #function
                    if function=='function':
                        pos9 = len(JScode[(len(m.group(0)) + pos3 + 0):])
                        v = self.MemFonction(vars,'',arg,False,JScode[(len(m.group(0)) + pos3 + 0):])[2]
                        pos3 = pos3 + pos9
                        InterpretedCode.AddValue(v)
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
                        arg = RemoveGuil(arg)
                        out('To eval >' + arg)
                        self.ForceReturn = True
                        r = self.Parse(arg,vars,allow_recursion)
                        InterpretedCode.AddValue(r)
                        JScode = JScode[(len(m.group(0)) + pos3 ):]
                        continue

                    print vars
                    raise Exception("Unknow fonction : " + function)
                    
            # pointeur vers fonction ?
            if hasattr(Basic, JScode):
                fm = getattr(Basic(), JScode)
                InterpretedCode.AddValue(fm)
                JScode = ''
                continue

            #variables
            m = re.search('^(\({0,1}\w[\w\.]*\){0,1} *(?:\[[^\]]+\])* *)(' + REG_OP + '|\[|$)',JScode, re.UNICODE)
            if m:
                #Recup variable
                v = m.group(1).strip()
                JScode = JScode[(len(m.group(1))):]
 
                New_Var = False
                
                #recup operator
                op = ''
                if len(m.groups()) > 1:
                    op = m.group(2).strip()
                if op == '[':
                    op = ''
                #prb because the only possible case  is ==
                if len(op) > 1 and op[0] == '=' and op[1] != '=':
                    op = op[0]
              
                out('Variable=' + str(v) + '  operator : ' + op )                   
                
                if not self.IsVar(vars,v):
                    out('*** VARIABLE NOT INITIALISEE ***')
                    New_Var = True

                # if it's a creation/modification
                if op == '=':
                    JScode = JScode[1:]
                    
                    v1 = GetItemAlone(JScode,',')
                    JScode = JScode[(len(v1)):]
                    
                    v1 = v1.strip()
                    self.VarManage(allow_recursion,vars,v,v1)
                    
                    #and return it
                    r = self.GetVar(vars,v)
                    InterpretedCode.AddValue(r)
                    
                    continue
                    
                #error ?
                if  New_Var:
                    raise Exception("Can't find var " + str(v))
                
                r = self.GetVar(vars,v)
                
                #just put var
                if len(op) == 2:
                    if op[0] in '=!':
                        InterpretedCode.AddValue(r)
                        continue               
                                
                #Only modification
                if len(op) == 2:

                    out("> var " + v + "=" + str(r))
                    
                    #check if it's i++ ou i -- form
                    if op == '++':
                        self.SetVar(vars,v,r + 1)
                        JScode = JScode[2:]
                        InterpretedCode.AddValue(r)
                        continue
                    elif op == '--':
                        self.SetVar(vars,v,r-1)
                        JScode = JScode[2:]
                        InterpretedCode.AddValue(r)
                        continue
                    #a+=1 form
                    elif op[1] == '=' and not op[0] == '=':
                        n = GetItemAlone(JScode[2:],' ,' + REG_OP)
                        r = self.evalJS(v + op[0] + n ,vars,allow_recursion)
                        #self.SetVar(vars,v,r)
                        self.VarManage(allow_recursion,vars,v,str(r))           
                            
                        InterpretedCode.AddValue(r)
                        JScode = JScode[(len(n) + 2):]
                        continue
                        
                #just var
                InterpretedCode.AddValue(r)
                continue
                
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
                C = GetItemAlone(JScode[(len(B) + 1):])
                
                Totlen = len(B) + len(C) + 2
                B = B[1:]
                if B.startswith('('):
                    B = B[1:-1]
                if C.startswith('('):
                    C = C[1:-1]               
                if A:
                    r = self.evalJS(B,vars,allow_recursion)
                else:
                    r = self.evalJS(C,vars,allow_recursion)

                InterpretedCode.AddValue(r)
                JScode = JScode[Totlen :]
                continue

            #Short-circuiting evaluations
            if JScode[0:2] == '&&' or JScode[0:2] == '||':
                out( " ****** Short-circuiting  ********* ")
                A = InterpretedCode.GetPrevious()
                B = GetItemAlone(JScode[2:])
                
                Totlen = len(B) + 2
                if B.startswith('('):
                    B = B[1:-1]
                    
                #for && if the first operand evaluates to false, the second operand is never evaluated
                if JScode[0:2] == '&&':
                    if A:
                        r = self.evalJS(B,vars,allow_recursion)
                        InterpretedCode.AddValue(r)
                    else:
                        InterpretedCode.AddValue(A)
                #for || if the result of the first operand is true, the second operand is never operated
                if JScode[0:2] == '||':
                    if not A:
                        r = self.evalJS(B,vars,allow_recursion)
                        InterpretedCode.AddValue(r)
                    else:
                        InterpretedCode.AddValue(A)
                        
                JScode = JScode[Totlen :]
                continue                    
                
            #Operation
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
                
            #comma
            if c == ',':
                InterpretedCode.GetPrevious()
                JScode = JScode[1:]
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
                            index = RemoveGuil(index)
                            r = r[index]
                    if type(r) in [dict]:
                        index = RemoveGuil(index)
                        self.PrintVar(var)
                        r = r.get(index)              
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
        
    def GetTypeVar(self,var,variable):
        try:
            variable = variable.split('[')[0]
            variable = variable.split('.')[0]
            for j in var:
                if j[0] == variable:
                    return type(j[1])
            return 'Undefined'
        except:
            return 'Undefined'   
    
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
        elif isinstance(f, types.MethodType):
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
            if self.GetTypeVar(vars,name) == 'tuple':
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
                        v2g = RemoveGuil(l[0])
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

            #Variable creation/modification ?
            #m =  re.search(r'^\({0,1}([\w\.]+)\){0,1}(?:\[([^\]]+)\])*\){0,1}\s*(?:[\^\/\*\-\+])*=',chain,re.DOTALL | re.UNICODE)
            #m2 = re.search(r'^\({0,1}([\w\.]+)\){0,1}(?:\.([\w]+))*\){0,1}\s*(?:[\^\/\*\-\+])*=',chain,re.DOTALL | re.UNICODE)
            if chain.startswith('var '):
                out('var')

                chain = chain[4:]
                
                #Now need to extract all vars from chain
                while (chain):
                    v1 = GetItemAlone(chain,',').strip()

                    chain=chain[(len(v1) + 1):]
                    
                    if v1.endswith(',') or v1.endswith(';'):
                        v1 = v1[:-1]

                    if (True):
                        self.evalJS(v1,vars,allow_recursion)
                    else:
                        t3 = GetItemAlone(v1,'=')
                    
                        #A=B=C=8,A=1
                        if '=' in v1:
                            #just '='
                            if v1[(len(t3)) - 2] not in '+-*/^':
                                t1 = []
                                while v1:
                                    t3 = GetItemAlone(v1,'=')
                                    v1 = v1[(len(t3)+1):]
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
                    self.ReturnValue = None
                    return
                m = re.match(r'^return *([^;]+)', chain)
                if m:
                    chain = m.group(1)
                    r = self.evalJS(chain,vars,allow_recursion)
                    self.Return = True
                    self.ReturnValue = r
                    return           
                    

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
        #vars.append(('true',True))
        #vars.append(('false',False))
        
        #Hack
        JScode = JScode.replace('$(document).ready','DOCUMENT_READY')
        JScode = JScode.replace('.length','.length()')
        
        #Start the parsing
        ret = self.Parse(JScode,vars)
        
        #Memorise vars
        
        
        return ret

        
#----------------------------------------------------------------------------------------------------------------------------------------
# fonctions
#

class Math(object):
    def __init__(self):
        pass

    def max(self,arg):
        t1 = arg[0]
        t2 = arg[1]
        return max(t1,t2)
        
    def min(self,arg):
        t1 = arg[0]
        t2 = arg[1]
        return min(t1,t2)
        
    def abs(self,arg):
        return abs(arg[0])    

class String(object):
    def __init__(self,__string=''):
        self._string = __string

    def Get(self):
        return self._string

    def charCodeAt(self,arg):
        v = arg[0]
        return ord(self._string[int(v)])

    def length(self,arg):
        return len(self._string)

    def substring(self,arg):
            p1 = arg[0]
            if len(arg)> 1:
                p2 = arg[1]
                return self._string[ int(p1) : int(p2) ]
            else:
               return self._string[ int(p1) :]

    def replace_not_working(self,arg):
        t1 = arg[0]
        t2 = arg[1]
        
        #if not t1.startswith('/'):
        #    t1 = self.evalJS(t1,vars,allow_recursion)
            
        #regex mode ? HACK
        if t1.startswith('/'):
            jr = re.findall(t1.split('/')[1], self._string)

            for k in jr:
                if not self.IsFunc(vars,t2):
                    r = self._string.replace(k,t2)
                    out('Replace ' + str(k) + " by " + str(t2))
                else:
                    v = self.evalJS(t2+'('+ k + ')',vars,allow_recursion)
                    v = str(v)
                    r = self._string.replace(k,v)
                    out('Replace ' + str(k) + " by " + str(v))
        #String mode
        else:
            #t1 = self.evalJS(t1,vars,func,allow_recursion)
            r = s.replace(t1,t2)
        return r
            
    def fromCharCode(self,arg):
        return chr(int(arg[0]))

    def split(self,arg):
        arg = arg[0].replace('"','').replace("'","")
        if arg == '':
            return list(self._string)
        else:
            return self._string.split(arg)

class Array(object):
    def __init__(self,__array=[]):
        self._array = __array
        
    def Get(self):
        return self._array
        
    def join(self,arg):
        t = arg[0].replace('"','').replace("'","")
        return t.join(self._array)

    def push(self,arg):
        t1 = arg[0]
        if len(arg) > 1:
            #use s.extend-[array]);
            raise Exception("Not implemented - push")
        self._array.append(t1)

        v = len(self._array)
        return v
        
    def slice(self,arg):
        p1 = arg[0]
        if len(arg)> 1:
            p2 = arg[1]
            sr = s[int(p1):int(p2)]
        else:
            sr = s[int(p1):]
        sr = '"' + sr + '"'
        return sr
        
    def splice(self,arg):
        t1 = arg[0]
        t2 = arg[1]
        if len(arg) > 2:
            raise Exception("Not implemented - splice")
        tab = self._array[:t1] + self._array[(t1 + t2):]
        tabsup = self._array[t1:(t1 + t2)]

        self._array = tab
        return tabsup

                        
class Basic(object):
    def __init__(self):
        pass
        
    def parseInt(self,arg):
        t1 = arg[0]
        t2 = arg[1]
        r = int(t1,int(t2))
        return r

    def alert(self,arg):
            t1 = self.evalJS(arg,vars,allow_recursion)
            print '------------ALERT-------------------'
            print arg
            print '------------------------------------'
            return ''

    def RegExp(self,arg):
        t1 = RemoveGuil(arg[0])
        t2 = RemoveGuil(arg[1])
        return '/' + t1 + '/' + t2

List_Lib = [Basic,Array,String,Math]
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
