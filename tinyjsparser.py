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

#phrase=raw_input()
#phrase.xxx


#https://javascriptweblog.wordpress.com/2011/04/04/the-javascript-comma-operator/



import re
import types
from types import NoneType
import time

import sys

REG_NAME = '[\w]+'
REG_OP = '[\/\*\-\+\{\}<>\|\&=~^%!]+' #not space here, and no bracket
DEBUG = True # Never enable it in kodi, too big size log
MAX_RECURSION = 50
ALPHA = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

#---------------------------------------------------------------------------------

JScodesdfdfds = """
a = '#';
b = ( a != '#');
debug();
"""



JScodefffff = """
a = 'A';
a += '~';
debug();
"""


#var _0xd97fd7=_0x4869aa[_0x7a4b('28')]($,_0x4869aa[_0x7a4b('29')]('#','p')).text();
#    _0xd97fd7=       $(#p).text();
# _0x1853c9 = 9d au lieu de 0d


JScode = """


window.p = 'AmWncdZqOr';
var _0xa4b7 = ['push', 'sKA', 'ready', '9|8|6|2|4|1|7|11|12|5|10|13|3|0', '#streamurl', 'text', 'substring', 'epX', 'length', '8|9|7|6|3|1|0|5|2|4', 'split', 'hRs', 'uSu', '1|3|4|5|0|6|2', 'RbZ', 'ZGr', 'Zqu', 'FBD', 'rPe', 'pow', 'KzL', '0|2|5|1|3|4', 'fGi', 'fromCharCode', 'dew', 'rZj', 'bWh', 'ZjA', 'ysG', 'charCodeAt', 'jYD', 'kKG', 'IQO', 'gif'];


(function(_0x389e2e, _0x1ccc06) {
        var _0x3edeb0 = function(_0x12e01f) {
            while (--_0x12e01f) {
                _0x389e2e['push'](_0x389e2e['shift']());
            }

        };
        _0x3edeb0(++_0x1ccc06);
    }
    (_0xa4b7, 444));


var _0x7a4b = function(_0x389e2e, _0x1ccc06) {
    _0x389e2e = _0x389e2e - 0;

    var _0x3edeb0 = _0xa4b7[_0x389e2e];
    return _0x3edeb0;
};

var _0x4869aa = {
    'jYD': function _0x5a23c5(_0x292aa0, _0x387698) {
        return _0x292aa0(_0x387698);
    },
    'epX': function _0x5f50fe(_0x5e2bff, _0x547293) {
        return _0x5e2bff < _0x547293;
    },
    'hRs': function _0x152fe0(_0x173c13, _0x98d9ef) {
        return _0x173c13 ^ _0x98d9ef;
    },
    'uSu': function _0x91eab9(_0x45e58b, _0xd1f058) {
        return _0x45e58b % _0xd1f058;
    },
    'Jia': function _0x30706c(_0x1230ba, _0x289191, _0x11ee82) {
        return _0x1230ba(_0x289191, _0x11ee82);
    },
    'MYg': function _0x4e205f(_0xe27ddb, _0xf067ff) {
        return _0xe27ddb >= _0xf067ff;
    },
    'RbZ': function _0x31b1a8(_0x114615, _0x65b84) {
        return _0x114615 + _0x65b84;
    },
    'ZGr': function _0x2e4204(_0x35cc4f, _0x233886) {
        return _0x35cc4f < _0x233886;
    },
    'FBD': function _0x5e86fd(_0x5705ec, _0x1d01c4) {
        return _0x5705ec & _0x1d01c4;
    },
    'Zqu': function _0x5d4a7b(_0x373be7, _0x2d8041) {
        return _0x373be7 << _0x2d8041;
    },
    'rPe': function _0x57303b(_0x402588, _0x2ef2a1) {
        return _0x402588 * _0x2ef2a1;
    },
    'KzL': function _0x3d9b90(_0x29276d, _0x544c3d) {
        return _0x29276d >= _0x544c3d;
    },
    'fGi': function _0x3b75d9(_0x50d04c, _0x3279a7) {
        return _0x50d04c & _0x3279a7;
    },
    'dew': function _0x22a6c6(_0x3d2820, _0x306388) {
        return _0x3d2820 * _0x306388;
    },
    'OWe': function _0x93a61c(_0x42c840, _0x319b9a) {
        return _0x42c840 / _0x319b9a;
    },
    'rZj': function _0x4b6d60(_0x31a5bc, _0x275383) {
        return _0x31a5bc != _0x275383;
    },
    'bWh': function _0x5ae633(_0x53b452, _0x645d0b) {
        return _0x53b452 << _0x645d0b;
    },
    'ZjA': function _0x2779d4(_0xa0f786, _0x2e0c16) {
        return _0xa0f786 >> _0x2e0c16;
    },
    'ysG': function _0x3af8fd(_0x27c45e, _0xf2d4e4) {
        return _0x27c45e * _0xf2d4e4;
    },
    'kKG': function _0x48e415(_0x4aa626, _0x20ccc3) {
        return _0x4aa626 + _0x20ccc3;
    },
    'waX': function _0x53a972(_0x134ea6, _0x31c280) {
        return _0x134ea6 < _0x31c280;
    },
    'IQO': function _0x558c8b(_0x3b09a0, _0x49e441) {
        return _0x3b09a0 * _0x49e441;
    },
    'gif': function _0x458653(_0x1bd05a, _0x536a03) {
        return _0x1bd05a + _0x536a03;
    },
    'bLD': function _0x309754(_0x25e56b, _0x560d72, _0x43c36c) {
        return _0x25e56b(_0x560d72, _0x43c36c);
    },
    'sKA': function _0x551899(_0x4cc6f4, _0x16fd7d) {
        return _0x4cc6f4 * _0x16fd7d;
    }

};
var _0x4a3f26 = _0x7a4b('1')['split']('|'),
    _0x14602e = 0;
while (true) {
    switch (_0x4a3f26[_0x14602e++]) {

        case '0':
            _0x4869aa['jYD']($, _0x7a4b('2'))[_0x7a4b('3')](_0x5bf24a);
            continue;
        case '1':
            var _0xf0d52b = _0x11894f[_0x7a4b('4')](0, _0x58e425);
            continue;
        case '2':
            var _0x5bf24a = '';
            continue;
        case '3':
            while (_0x4869aa[_0x7a4b('5')](_0xf0d52b, _0x11894f[_0x7a4b('6')])) {
                var _0x126680 = _0x7a4b('7')[_0x7a4b('8')]('|'),
                    _0x3cc582 = 0;

                while (true) {
                    switch (_0x126680[_0x3cc582++]) {

                        case '0':
                            var _0x279fee = _0x4869aa[_0x7a4b('9')](_0x4fd569, _0x58c4a2[_0x4869aa[_0x7a4b('10')](_0x4b5dad, 3)]);

                            continue;
                        case '1':     
                            do {
                            
                                var _0x58ef54 = _0x7a4b('11')[_0x7a4b('8')]('|'),
                                    _0xa7be18 = 0;
                                while (true) {
                                    switch (_0x58ef54[_0xa7be18++]) {

                                        case '0':
                                            _0x21a6bf = _0x4869aa['Jia'](parseInt, _0x1853c9, 16);
                                            continue;
                                        case '1':
                                            if (_0x4869aa['MYg'](_0x4869aa['RbZ'](_0xf0d52b, 1), _0x11894f['length'])) {
                                                _0x2e6efb = 143;
                                            }
                                            continue;
                                        case '2':
                                            _0x425958 += 7;
                                            continue;
                                        case '3':
                                            var _0x1853c9 = _0x11894f[_0x7a4b('4')](_0xf0d52b, _0x4869aa[_0x7a4b('12')](_0xf0d52b, 2));
                                            continue;
                                        case '4':
                                            _0xf0d52b++;
                                            continue;
                                        case '5':
                                            _0xf0d52b++;
                                            continue;
                                        case '6':
                                            
                                            if (_0x4869aa[_0x7a4b('13')](_0x425958, 28)) {
                                                var _0x5157c4 = _0x4869aa['FBD'](_0x21a6bf, _0x1333c0);
                                                _0x4fd569 += _0x4869aa[_0x7a4b('14')](_0x5157c4, _0x425958);

                                            } else {
                                                var _0x5157c4 = _0x4869aa[_0x7a4b('15')](_0x21a6bf, _0x1333c0);
                                                _0x4fd569 += _0x4869aa[_0x7a4b('16')](_0x5157c4, Math[_0x7a4b('17')](2, _0x425958));
                                            }
                                            continue;
                                    }
                                    break;
                                }

                            }
                            while (_0x4869aa[_0x7a4b('18')](_0x21a6bf, _0x2e6efb));
                            continue;
                        case '2':
                            for (i = 0; _0x4869aa[_0x7a4b('13')](i, 4); i++) {
                                var _0x5901b5 = _0x7a4b('19')[_0x7a4b('8')]('|'),
                                    _0x4a573e = 0;
                                while (true) {
                                    switch (_0x5901b5[_0x4a573e++]) {

                                        case '0':
                                            var _0x5e73dd = _0x4869aa[_0x7a4b('20')](_0x279fee, _0xc093ea);
                                            continue;
                                        case '1':
                                            var _0x3852b3 = String[_0x7a4b('21')](_0x5e73dd);
                                            continue;
                                        case '2':
                                            var _0x2d6869 = _0x4869aa[_0x7a4b('22')](_0x4869aa['OWe'](_0x58e425, 3), i);
                                            continue;
                                        case '3':
                                            if (_0x4869aa[_0x7a4b('23')](_0x3852b3, '#')) _0x5bf24a += _0x3852b3;
                                            continue;


                                        case '4':
                                            _0xc093ea = _0x4869aa[_0x7a4b('24')](_0xc093ea, _0x4869aa['OWe'](_0x58e425, 3));
                                            continue;
                                        case '5':
                                            _0x5e73dd = _0x4869aa[_0x7a4b('25')](_0x5e73dd, _0x2d6869);
                                            continue;
                                    }
                                    break;
                                }

                            }
                            continue;
                        case '3':
                            var _0x21a6bf = 0;
                            continue;
                        case '4':
                            _0x4b5dad += 1;
                            continue;
                        case '5':
                            var _0xc093ea = _0x4869aa[_0x7a4b('12')](_0x2e6efb, _0x1333c0);
                            continue;
                        case '6':
                            var _0x425958 = 0;
                            continue;
                        case '7':
                            var _0x4fd569 = 0;
                            continue;
                        case '8':
                            var _0x2e6efb = 128;
                            continue;
                        case '9':
                            var _0x1333c0 = 127;
                            continue;
                    }
                    break;
                }

            }
            continue;
        case '4':
            var _0x58e425 = _0x4869aa[_0x7a4b('26')](3, 8);
            continue;
        case '5':
            _0x11894f = _0x11894f[_0x7a4b('4')](_0x58e425);
            continue;
        case '6':
            _0x11894f = _0xd97fd7;
            continue;
        case '7':
            var _0x58c4a2 = [];
            continue;
        case '8':
            var _0x11894f = _0xd97fd7[_0x7a4b('27')](0);
            continue;
        case '9':
            var _0xd97fd7 = _0x4869aa[_0x7a4b('28')]($, _0x4869aa[_0x7a4b('29')]('#', p))['text']();
            continue;
        case '10':
            var _0xf0d52b = 0;
            continue;

        case '11':
            for (i = 0; _0x4869aa['waX'](i, _0xf0d52b[_0x7a4b('6')]); i += 8) {

                _0x58e425 = _0x4869aa[_0x7a4b('30')](i, 8);
                var _0x2f5a6c = _0xf0d52b['substring'](i, _0x4869aa[_0x7a4b('31')](i, 8));
                var _0x357bed = _0x4869aa['bLD'](parseInt, _0x2f5a6c, 16);
                _0x58c4a2[_0x7a4b('32')](_0x357bed);
            }

            continue;


        case '12':
            _0x58e425 = _0x4869aa[_0x7a4b('33')](3, 8);
            continue;
        case '13':
            var _0x4b5dad = 0;
            continue;
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

JScodegfhhg ="""
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

def logwrite(stri):
    fh = open('G:\\JSparser\\debug.txt', "a")
    fh.write(stri)
    fh.close()

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
    
def GetNextUsefullchar(string):
    j = 0
    try:
        while (string[j].isspace()):
            j = j + 1
    except:
        return '',0       
    return string[j],j

    
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
        
        #Return if the is complete and before the char wanted but not if it's the first one
        if (ch in separator) and (p==0) and (a==0) and (b==0) and (c1==0) and (c2==0) and not(n) and (i>0):
            return ret[:-1]
        
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

        #return if the chain is complete but with the char wanted
        if (ch in separator) and (p==0) and (a==0) and (b==0) and (c1==0) and (c2==0) and not(n) and (i>0):
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

    def __init__(self):
        self.type = None
        self.buffer = ''
        self.__op = ''
        self.__value = None
        
        #buffers
        self.buf=[]
        self.opBuf = []
        
    def SetOp(self,op):
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
                if self.opBuf[1] == '!':
                    self.buf[1] = not self.buf[1]
                    self.opBuf[1] = self.opBuf[1].replace('!','')
                if self.opBuf[1] == '+':
                    self.buf[0] = self.buf[0] + self.buf[1]
                if self.opBuf[1] == '|':
                    if not self.buf[0]:
                        self.buf[0] = self.buf[1]
                if '==' in self.opBuf[1]:
                    self.buf[0] = (self.buf[1] == self.buf[0])
                    self.type == 'Logic'
                if '!=' in self.opBuf[1]:
                    self.buf[0] = (self.buf[1] != self.buf[0])
                    self.type == 'Logic'
                    
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
        
class Hack(object):
    def __init__(self,var):
        self.var = var
    def text(self):
        return self.var

class JsParserHelper1(object):
    def __init__(self):
        self.reset()
        self.used = False
        
    def reset(self):
        type = None
        self.name = ''
        self.at1 = None
        self.t = None
        self.arg = None
        self.rest_code = ''
        self.op = None
        self.eval = False    
      
    def process(self,JScode):
        self.reset()
        self.memo = JScode
    
        r = re.search('^(\w[\w]*)',JScode)
        if not r:
            return False
            
        self.used = True
            
        #By defaut
        self.t = 'var'
            
        self.name = r.group(1)
        JScode = JScode[(len(self.name)):]
        
        c,p = GetNextUsefullchar(JScode)
        while (c in '.[') and c:
            JScode = JScode[p:]
            if c == '[':
                a = GetItemAlone(JScode,']')
                JScode = JScode[(len(a)):]
                self.at1 = a[1:-1]
                self.eval = True
            if c == '.':
                a = GetItemAlone(JScode[1:],'[(.\/*-+{}<>|=~^%!')
                JScode = JScode[(len(a)+1):]
                self.at1 = a
                
            c,p = GetNextUsefullchar(JScode)

        if c == '(':
            a = GetItemAlone(JScode,')')
            #JScode = JScode[(len(a)):]
            #self.at1.append(a[1:-1])
            self.arg = a[1:-1]
            self.t = 'fct'
        
        #operation ?
        op = None
        m = re.search('^(' + REG_OP + '|\[|$)',JScode, re.UNICODE)
        if m and JScode:
            op = m.group(1).strip()
            if op == '[':
                op = ''
            #prb because the only possible case  is ==
            if len(op) > 1 and op[0] == '=' and not op[1] == '=':
                op = op[0]
                      
            self.op = op
            self.t = 'ope'
        
        if self.t == 'fct':
            out('Fonction :' + self.name + ' method: ' + str(self.at1) + ' arg: ' + self.arg)
            self.rest_code = JScode
        elif self.t == 'var':
            out('Variable :' + self.name + ' []= ' + str(self.at1) )
            self.rest_code = JScode
        elif self.t == 'ope':
            out('operation :' + self.name )
            self.rest_code = self.memo
            
        return True
        
        
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
        
    #Syntax > aaaaaa.bbbbbb(cccccc) ou bbbb(cccc) ou "aaaa".bb(ccc) ou aa[bb](cc)    
    def FonctionParser(self,vars,allow_recursion,name,function,JScode):         
        #Extraction info
        #m = re.search(r'^(?:([\w]+)\.)*([\w]+(?:\[[^\]]+\])*) *\(', JScode,re.DOTALL | re.UNICODE)
      
        arg = GetItemAlone(JScode,')')
        pos3 = len(arg)
        arg=arg[1:-1].strip()

        out( 'fonction > Name: ' + Ustr(name) + ' arg: ' + Ustr(arg) + ' function: ' + Ustr(function) )     
        
        #hack ?
        if isinstance(name, Hack):
            a = MySplit(arg,',',True)
            
            #function = text
            if a:
            #ecriture
                vv = self.evalJS(a[0],vars,allow_recursion)
                self.AddHackVar(name.var,vv)
                JScode = JScode[( pos3 + 0):]
                return vv,JScode
            else:
            #lecture
                vv = self.GetVarHack(name.var)
                out('Hack vars (set): ' + vv)
                JScode = JScode[( pos3 + 0):]
                return vv,JScode
        
        #Definite function ?
        fe = self.IsFunc(vars,function)
        if not fe:
            try:
                fe = self.IsFunc(vars,name+'["' + function + '"]')
            except:
                pass        

        if fe:
            if fe == '$':
                JScode = JScode[( pos3 + 0):]
                a = MySplit(arg,',',True)
                vv = self.evalJS(a[0],vars,allow_recursion)
                fff = Hack(vv)
                
                return fff,JScode
                
            elif isinstance(fe, types.MethodType):
                #print fe.im_func.__name__ #parseint
                #print fe.im_class.__name__ #Basic
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
                    JScode = n + '(' +arg + ')' + JScode[( pos3 + 0):]
                    return '',JScode

                for i in a:
                    vv = self.evalJS(i,vars,allow_recursion)
                    a2.append(RemoveGuil(vv))
                
                if (len(p) > 0) and (len(a2)>0):
                    nv = tuple(zip(p, a2))
                    for z,w in nv:
                        self.SetVar(vars,z,w)

                self.Parse(c,vars,allow_recursion)
                
                if self.Return:
                    self.Return = None
                    
                JScode = JScode[( pos3 + 0):]
                return self.ReturnValue,JScode
            else:
                raise Exception("Strnage fonction")
                
        #Native fonction
        # http://stackoverflow.com/questions/1091259/how-to-test-if-a-class-attribute-is-an-instance-method
        
        if name:
            if type(name) in [list,tuple,dict]:
                s = name
            elif name.startswith('"') or name.startswith("'"):
                s = RemoveGuil(name)
            else:
                if self.IsVar(vars,name):
                    s = self.GetVar(vars,name)
                else:
                    s = name
        else:
            s = ''
        
        Find_lib = False
        for lib in List_Lib:
            if hasattr(lib, function):
                arg = MySplit(arg,',')
                for i in range(len(arg)):
                    arg[i] = self.evalJS(arg[i],vars,allow_recursion)
                
                #Lib need init
                if hasattr(lib, 'Get'):
                    #s = self.GetVar(vars,name)
                    cls =  lib(s)
                    r = getattr(cls, function)(arg)
                    #set new value if chnaged, never reached ??
                    NV = getattr(cls, 'Get')()
                    if not NV == s:
                        self.SetVar(vars,name,NV)
                        
                #Classic lib
                else:
                    r = getattr(lib(), function)(arg)
                    
                #InterpretedCode.AddValue(r)
                JScode = JScode[( pos3 ):]
                
                Find_lib = True
                
                break
                
        if Find_lib:
            return r,JScode    

        #replace
        #print re.sub('1',lambda m: f(m.group()),s)
        if function=='replace':
            arg = MySplit(arg,',')
            t1 = arg[0]
            t2 = self.evalJS(arg[1],vars,allow_recursion)
            
            #out('***** replace ' + str(arg) ) 
            
            #s = self.GetVar(vars,name)
            
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
            #String mode
            else:
                s = s.replace(t1,t2)
                #t1 = self.evalJS(t1,vars,func,allow_recursion)
            JScode = JScode[( pos3 ):]
            return s,JScode
            
        #hack var
        if function=='text':
            #s = self.GetVar(vars,name)
            #ignored for the moment
            JScode = JScode[( pos3):]
            return s,JScode                  
            
        #array
        if function=='Array':
            JScode = JScode[(pos3):]
            return [],JScode
    
        #function
        if function=='function':
            pos9 = len(JScode[( pos3 + 0):])
            v = self.MemFonction(vars,'',arg,False,JScode[( pos3 + 0):])[2]
            pos3 = pos3 + pos9
            JScode = JScode[( pos3 ):]
            return v,JScode         
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
            JScode = v + JScode[ (pos3 ):]
            return '',JScode
        #eval ?
        if function=='eval':
            out('Eval')
            arg = RemoveGuil(arg)
            out('To eval >' + arg)
            self.ForceReturn = True
            r = self.Parse(arg,vars,allow_recursion)
            JScode = JScode[( pos3 ):]
            return r,JScode

        self.PrintVar(vars)
        raise Exception("Unknow fonction : " + function)
        
    def VarParser(self,vars,allow_recursion,variable,JScode):
    
        #Special vars
        if variable.startswith('window.'):
            variable = variable[7:] 
        
        #recup operator
        op = ''
        m = re.search('^(' + REG_OP + '|\[|$)',JScode, re.UNICODE)
        if m:
            op = m.group(1).strip()
            if op == '[':
                op = ''
            #prb because the only possible case  is ==
            if len(op) > 1 and op[0] == '=' and not op[1] == '=':
                op = op[0]

            New_Var = False
      
        out('Variable : ' + str(variable) + '  operator : ' + op )
        
        if not self.IsVar(vars,variable):
            out('*** VARIABLE NOT INITIALISEE ***')
            New_Var = True

        # if it's a creation/modification
        if op == '=':
        
            out('creation')
        
            JScode = JScode[1:]
            
            v1 = GetItemAlone(JScode,',')
            JScode = JScode[(len(v1)):]
            
            v1 = v1.strip()

            self.VarManage(allow_recursion,vars,variable,v1)
            
            #and return it
            r = self.GetVar(vars,variable)
            return r,JScode

            
        #error ?
        if  New_Var:
            raise Exception("Can't find var " + str(variable))
        
        r = self.GetVar(vars,variable)
        
        #just put var
        if len(op) == 2:
            if op[0] in '=!':
                return r,JScode
                        
        #Only modification
        if len(op) == 2:

            out("> var " + variable + "=" + str(r))
            
            #check if it's i++ ou i -- form
            if op == '++':
                self.SetVar(vars,variable,r + 1)
                JScode = JScode[2:]
                return r,JScode

            elif op == '--':
                self.SetVar(vars,variable,r-1)
                JScode = JScode[2:]
                return r,JScode

            #a+=1 form
            elif op[1] == '=' and op[0] in '+-*/%^':
                n = GetItemAlone(JScode[2:],';,')
                out('A rajouter ' + n)
                r = self.evalJS(variable + op[0] + n ,vars,allow_recursion)
                #self.SetVar(vars,variable,r)
                
                if isinstance(r, ( int, long , float) ):
                    self.VarManage(allow_recursion,vars,variable,str(r))
                if isinstance(r, ( str) ):
                    self.VarManage(allow_recursion,vars,variable,'"'+ r + '"')
                else:
                    self.VarManage(allow_recursion,vars,variable,str(r))
                    
                JScode = JScode[(len(n) + 2):]
                return r,JScode
                
        #just var     
        return r,JScode
        
    def checkoperator(self,strg):
        if strg == GetItemAlone(strg,'/*-+^=!'):
            return False
        return True
    
        
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
            
            item = None

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
                
            #remove "useless" code
            if JScode.startswith('new '):
                JScode = JScode[4:]
                continue
                
                
            #Special value
            m = re.search('^(true|false|null|String)',JScode, re.UNICODE)
            if m:
                v = m.group(1)
                JScode = JScode[len(v):]
                
                if v == 'true':  
                    InterpretedCode.AddValue(True)
                if v == 'false':
                    InterpretedCode.AddValue(False)
                if v == 'null':
                    InterpretedCode.AddValue(None)
                if v == 'String':
                    self.SetVar(vars,'TEMPORARY_VARS'+str(allow_recursion),'')
                    JScode = 'TEMPORARY_VARS'+str(allow_recursion) + JScode
                #if v == 'Array':
                #    InterpretedCode.AddValue([])

                continue
                
                
            #hackVars
            r = re.search('^\$\("#([\w]+)"\)\.text\(\)',JScode)
            if r:
                InterpretedCode.AddValue(self.GetVar(self.HackVars,r.group(1)))
                JScode = JScode[(r.end()):]
                continue
 
            if JScode[0] == '$':
                InterpretedCode.AddValue('$')
                JScode = JScode[1:]
                continue 
                
            #new function delcaration ?
            if JScode.startswith("function "):
                m = re.search(r'^(\()* *function(?: ([\w]+))* *\(([^\)]*)\) *{', JScode,re.DOTALL)
                if m:
                    name = ''
                    openparenthesis = False
                    if m.group(2):
                        name = m.group(2)
                    if m.group(1):
                        openparenthesis = True
                
                    replac,pos3,xyz = self.MemFonction(vars,name,m.group(3),openparenthesis,JScode)
                    JScode = replac
                    v = self.IsFunc(vars,name)
                    InterpretedCode.AddValue(v)
                    continue             
                    
            # pointeur vers fonction ?
            if hasattr(Basic, JScode):
                fm = getattr(Basic(), JScode)
                InterpretedCode.AddValue(fm)
                JScode = ''
                continue                
            
            #3 - numeric chain
            r = re.search('(^[0-9]+)',JScode)
            if r and not item:
                InterpretedCode.AddValue(int(JScode[0:r.end()]))
                JScode = JScode[(r.end()):]
                continue #for this one continue directly

            #4 - Regex
            r = re.search('^\/.*\/(.*$)',JScode)
            if r and not item:
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
                continue #return directly
                
                
            #1 - Array / method
            if c == "[":
                pos2,c2 = GetBeetweenChar(JScode,'[',']')
                v = self.evalJS(c2,vars,allow_recursion)

                if v == 'constructor':
                    v2 = InterpretedCode.GetPrevious()
                    v3 = GetConstructor(v2)
                #elif CheckType(v) == 'Numeric':
                #    v2 = InterpretedCode.GetPrevious()
                #    InterpretedCode.AddValue(v2[int(v)])
                #elif InterpretedCode.CheckString():
                #    v2 = InterpretedCode.GetPrevious()
                #    try:
                #        item = v2[v]
                #    except:
                 #       bb(mm)
                else:
                    InterpretedCode.AddValue([])
                    
                JScode = JScode[(pos2 + 1):]             
                continue

            #2 - Alpha chain
            elif c == '"' or c == "'":

                ee = GetItemAlone(JScode,c)
                e = len(ee)
                vv = ee[1:-1]
                
                # raw string cannot end in a single backslash
                #if vv[-1:] == '\\' and  not vv[-2:-1] == '\\':
                #    vv = vv + '\\'
                    
                #warning with this function
                #if not vv.endswith('\\'):
                #    vv = vv.decode('string-escape')
                
                JScode = JScode[(e):]
                
                #to be faster
                if len(JScode) == 0:
                    InterpretedCode.AddValue(vv)
                    continue
                #normal way
                else:
                    self.SetVar(vars,'TEMPORARY_VARS'+str(allow_recursion),vv)
                    JScode = 'TEMPORARY_VARS'+str(allow_recursion) + JScode
                
                #item = vv
                continue               

            item = ''
            #5 Variable/fonction/object
            P1 = JsParserHelper1()
            while(P1.process(JScode)):
                JScode = P1.rest_code
                item = P1.name
                r = None
                
                if P1.op:
                    m = re.search('^(\({0,1}\w[\w\.]*\){0,1} *(?:\[[^\]]+\])* *)(' + REG_OP + '|\[|$)',JScode, re.UNICODE)

                    out('creation/modification ' + str(m.groups()) + ' ' + str(len(m.group(2))) )
                    m = re.search('^(\({0,1}\w[\w\.]*\){0,1} *(?:\[[^\]]+\])* *)(' + REG_OP + '|\[|$)',JScode, re.UNICODE)
                    vv = m.group(1).strip()
                    JScode = JScode[(len(m.group(1))):]
                    r,JScode = self.VarParser(vars,allow_recursion,vv,JScode)
                    
                    InterpretedCode.AddValue(r)
                    continue
                else:
                
                    if P1.t == 'var':
                        if not self.IsVar(vars,P1.name):
                            raise Exception('Variable error : ' + P1.name)
                            
                        #C'est fini ?
                        if (P1.name == 'TEMPORARY_VARS'+str(allow_recursion)) and (P1.at1 == None):
                            r = self.GetVar(vars,'TEMPORARY_VARS'+str(allow_recursion))
                            self.InitVar(vars,'TEMPORARY_VARS'+str(allow_recursion))
                            JScode = JScode[(len('TEMPORARY_VARS'+str(allow_recursion))):]
                            InterpretedCode.AddValue(r)
                            continue

                        Var_string = P1.name
                        
                        #hack
                        if not P1.at1 == None:
                            eee = self.evalJS(P1.at1,vars,allow_recursion)
                            if eee == 'length':
                                t1 = self.evalJS(P1.name,vars,allow_recursion)
                                r = len(t1)
                                P1.at1 = None
                            
                            else:
                                r = self.GetVar(vars,Var_string+'[' + str(eee) + ']')
                        else:       
                            r = self.GetVar(vars,Var_string)
                            
                    
                    elif P1.t == 'fct':
                        if not(P1.at1 == None):
                            fonction = P1.at1
                            name = P1.name
                        else:
                            fonction = P1.name
                            name = ''
                            
                        if P1.eval:   
                            fonction = self.evalJS(fonction,vars,allow_recursion)

                        #hack devrait etre acive tout le temps
                        if 'TEMPORARY_VARS' in name:
                            name = self.evalJS(name,vars,allow_recursion)
                            
                        r,JScode = self.FonctionParser(vars,allow_recursion,name,fonction,JScode)

                        
                    self.SetVar(vars,'TEMPORARY_VARS'+str(allow_recursion),r)
                    JScode = 'TEMPORARY_VARS'+str(allow_recursion) + JScode
     
            if JScode.startswith('TEMPORARY_VARS'+str(allow_recursion)):
                r = self.GetVar(vars,'TEMPORARY_VARS'+str(allow_recursion))
                self.InitVar(vars,'TEMPORARY_VARS'+str(allow_recursion))
                JScode = JScode[(len('TEMPORARY_VARS'+str(allow_recursion))):]
                InterpretedCode.AddValue(r)
                continue     
            if P1.used:
                continue
            

                

                
            # --var method, HACK
            if JScode[0:2] == '--' or JScode[0:2] == '++':
                m = re.search('^(\({0,1}\w[\w\.]*\){0,1} *(?:\[[^\]]+\])* *)(' + REG_OP + '|\[|$)',JScode[2:], re.UNICODE)
                if m:
                    l = len(m.group(1))
                    JScode = m.group(1) +JScode[0:2] + JScode[(l+2):]
                    continue
                else:
                    bb(mm)

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
    
        #variable = variable.strip()
        
        index = None
        if '[' in variable:
            index = variable.split('[')[1][:-1]
            variable = variable.split('[')[0]
            index = self.evalJS(index,var,50)
            
        if '.' in variable:
            index = variable.split('.')[1]
            variable = variable.split('.')[0]
            
        #out('Variable Get ' + variable + ' index :' + str(index))
        
        for j in var:
            if j[0] == variable:
                r = j[1]
                if not(index == None):
                    if type(r) in [list,tuple,str]:
                        if CheckType(index) == 'Numeric':
                            if int(index) < len(r):
                                r = r[int(index)]
                            else:
                                r = 'undefined'
                        elif CheckType(index) == 'String':
                            index = RemoveGuil(index)
                            if index == 'length':
                                r = len(r)
                            else:
                                try:
                                    r = r[index]
                                except:
                                    r = r[int(index)]
                    if type(r) in [dict]:
                        index = RemoveGuil(index)
                        r = r.get(index)              
                return r
                
        #search it in hackvar ?
        for j in self.HackVars:
            if j[0] == variable:
                return j[1]
                
        raise Exception('Variable not defined: ' + str(variable))
            
    def SetVar(self,var,variable,value,i = None):
    
        #print 'Setvar Variable =' + variable + ' value=' + str(value) + ' index=' + str(i)

        variable = variable.strip()
        
        #cleaning
        if variable[0] == '(':
            variable = variable[1:-1]

        #Existing var ?
        for j in var:
            if j[0] == variable:

                if i == None:
                    #vars ?
                    if (isinstance(value, types.StringTypes)):
                        var[var.index(j)] = (variable,value)
                    #Numeric
                    else:
                        var[var.index(j)] = (variable,value)
                else:   
                #Array 
                    if type(var[var.index(j)][1]) in [list,tuple]:

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
    
    def IsVar(self,var,variable,index = None):
        try:
            variable = variable.split('[')[0]
            variable = variable.split('.')[0]
            for j in var:
                if j[0] == variable:
                    if index == None:
                        return True
                    if index in var[var.index(j)][1]:
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
        if f == '$':
            return '$'
        if isinstance(f, fonction):
            return f
        elif isinstance(f, types.MethodType):
            return f
        else:
            return self.IsFunc(vars,f)
        
    def VarManage(self,allow_recursion,vars,name,value=None):

        index = None
        init = False
        
        #out('Variable manager name: ' + str(name) + ' value: ' + str(value) + ' ' + str(type(value)))
        
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
                    
                    #hack
                    if value == '':
                        value = []
                    #normal way
                    else:  
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
                #string and other            
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
    def MemFonction(self,vars,name,parametres,openparenthesis,data):
    
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
        
        out('Extract function :' + name + ' ' + str(param))
        #out('data ' + str(data))
        
        pos = 0
        replac = ''
        
        while not data[0] == '{':
            data = data[1:]
            
        pos2,content = GetBeetweenChar(data,'{','}')
        #out('content ' + str(content))
        
        fm = fonction(name,param,content.lstrip())
        self.SetVar(vars,name,fm)
        
        data = data[(pos2+1):]
        
        if openparenthesis:
            c,p = GetNextUsefullchar(data)
            if c == ')':
                data = data[(p+1):]
                openparenthesis = False

        selfinvoked = False
        if len(data) > 0:
            if data[0] == '(':
                selfinvoked = True

        #self invoked ?
        if selfinvoked:
            paraminvoked = GetItemAlone(data,')')
            out( "Self invoked " + str(paraminvoked) )
            replac = name + paraminvoked
            
            data = data[(len(paraminvoked)):]
            
            if openparenthesis:
                c,p = GetNextUsefullchar(data)
                if c == ')':
                    data = data[(p+1):]
                    openparenthesis = False

        replac = replac + data
          
        return replac, 0 , name
        
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
            
            #selfinvoke = (function a(){})() or (function a(){}() )
            
            #fonction
            m = re.search(r'^(\()* *function(?: ([\w]+))* *\(([^\)]*)\) *{', chain,re.DOTALL)
            if m:
                name = ''
                openparenthesis = False
                if m.group(2):
                    name = m.group(2)
                if m.group(1):
                    openparenthesis = True
            
                replac,pos3,xyz = self.MemFonction(vars,name,m.group(3),openparenthesis,chain)
                
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
            m = re.search(r'^([\w]+) *(\(|\{)', chain,re.DOTALL)
            #Syntax > aaaaa(bbbbb) .........
            if m:
                name = m.group(1)
                sp = m.group(2)
                if sp == '(':
                    pos3,arg = GetBeetweenChar(chain[(m.end()-1):],'(',')')
                    code = chain[(m.end() + pos3):]
                elif sp == '{':
                    arg = ''
                    code = chain[(m.end()-1):]
                else:
                    raise Exception('> Er 74')
                
                out( 'DEBUG > Name: ' + name + ' arg: ' + arg + ' code: ' + code + '\n' )
                
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
                    
                #boucle do/while
                if name == 'do':
                    f = code
                    e = ''
                    if sp =='{':
                        f = GetItemAlone(f,'}')
                    
                    if f.startswith('{'):
                        f = f[1:-1]
                        
                    #Need to check the while part ?
                    chain2,pos2 = self.ExtractFirstchain(JScode)
                    if 'while' in chain2:
                        chain2 = chain2.lstrip()
                        JScode = JScode[(pos2 + 1):]
                        m2 = re.search(r'while\s*\((.+?)\);$', chain2,re.DOTALL)
                        if m2:
                            e = m2.group(1)
                        
                    if not e:
                        raise Exception('> While error')
                        
                    out('> Boucle do/while : test :' + e + ' code: ' + f)
                    
                    #loop
                    #1 forced execution because do/while
                    self.Parse(f,vars,allow_recursion)
                    if self.Break:
                        self.Break = False
                        continue #stop all
                        
                    if self.continu:
                        self.continu = False
                    #and now the loop
                    while (self.CheckTrueFalse(self.evalJS(e,vars,allow_recursion))):
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
                    f = code
                    
                    if v == 'undefined':
                        continue
                        
                    v = str(v)
                        
                    #out('> Boucle switch : Case=' + v + ' code= ' + f[0:50] + '\n')
                    
                    #Search the good case code
                    f = f[1:]
                    StrToSearch = "case'" + v + "':"
                    
                    while ((not f.startswith(StrToSearch)) and (len(f) > 0)):
                        tmp_str = GetItemAlone(f,';}')
                        f = f[(len(tmp_str)+1):]

                    if len(f) < 1:
                        self.PrintVar(vars)
                        raise Exception("Can't find switch value " + str(v))
                        
                    f = f[(len(StrToSearch)+0):]
                        
                    #out('\n> New block : ' + f[0:50])
                    
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

            #hack need to be reenabled
            #Non gere encore
            if not chain.endswith(';'):
                print '> ' + JScode
                raise Exception('> ERROR : can t parse >' + chain)
            
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
        #vars.append(('True',True))
        #vars.append(('False',False))
        
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

    def pow(self,arg):
        t1 = arg[0]
        t2 = arg[1]
        return pow(t1,t2)

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
            sr = self._array[int(p1):int(p2)]
        else:
            sr = self._array[int(p1):]
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

    def shift(self,arg):
        if len(self._array) == 0:
            return None
        return self._array.pop(0)
                        
class Basic(object):
    def __init__(self):
        pass
        
    def parseInt(self,arg):
        t1 = arg[0]
        t2 = arg[1]
        if t1 == '':
            return None
        r = int(t1,int(t2))
        return r

    def alert(self,arg):
            #t1 = self.evalJS(arg,vars,allow_recursion)
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

JP.AddHackVar('#AmWncdZqOr',"332f98cc836ecb269255d1cc9dd38b5af2fe96d10da0cd97e30efdd9da189ef6f3da0bfcc5af890afdedf25888f6839a0bb2b98ef30dfd97abfa05ebd0b7820a")
#print 'Return : ' + str(JP.ProcessJS(JScode))

JP.ProcessJS(JScode,Liste_var)
print 'Decoded url : ' + JP.GetVarHack("#streamurl")
