import codecs
import re
import os
import subprocess
import config

LHan = [[0x2E80, 0x2E99],    # Han # So  [26] CJK RADICAL REPEAT, CJK RADICAL RAP
        [0x2E9B, 0x2EF3],    # Han # So  [89] CJK RADICAL CHOKE, CJK RADICAL C-SIMPLIFIED TURTLE
        [0x2F00, 0x2FD5],    # Han # So [214] KANGXI RADICAL ONE, KANGXI RADICAL FLUTE
        0x3005,              # Han # Lm       IDEOGRAPHIC ITERATION MARK
        0x3007,              # Han # Nl       IDEOGRAPHIC NUMBER ZERO
        [0x3021, 0x3029],    # Han # Nl   [9] HANGZHOU NUMERAL ONE, HANGZHOU NUMERAL NINE
        [0x3038, 0x303A],    # Han # Nl   [3] HANGZHOU NUMERAL TEN, HANGZHOU NUMERAL THIRTY
        0x303B,              # Han # Lm       VERTICAL IDEOGRAPHIC ITERATION MARK
        [0x3400, 0x4DB5],    # Han # Lo [6582] CJK UNIFIED IDEOGRAPH-3400, CJK UNIFIED IDEOGRAPH-4DB5
        [0x4E00, 0x9FC3],    # Han # Lo [20932] CJK UNIFIED IDEOGRAPH-4E00, CJK UNIFIED IDEOGRAPH-9FC3
        [0xF900, 0xFA2D],    # Han # Lo [302] CJK COMPATIBILITY IDEOGRAPH-F900, CJK COMPATIBILITY IDEOGRAPH-FA2D
        [0xFA30, 0xFA6A],    # Han # Lo  [59] CJK COMPATIBILITY IDEOGRAPH-FA30, CJK COMPATIBILITY IDEOGRAPH-FA6A
        [0xFA70, 0xFAD9],    # Han # Lo [106] CJK COMPATIBILITY IDEOGRAPH-FA70, CJK COMPATIBILITY IDEOGRAPH-FAD9
        [0x20000, 0x2A6D6],  # Han # Lo [42711] CJK UNIFIED IDEOGRAPH-20000, CJK UNIFIED IDEOGRAPH-2A6D6
        [0x2F800, 0x2FA1D]]  # Han # Lo [542] CJK COMPATIBILITY IDEOGRAPH-2F800, CJK COMPATIBILITY IDEOGRAPH-2FA1D

def build_re():
  L = []
  for i in LHan:
    if isinstance(i, list):
      f, t = i
      try: 
        f = chr(f)
        t = chr(t)
        L.append('%s-%s' % (f, t))
      except:
        pass # A narrow python build, so can't use chars > 65535 without surrogate pairs!
    else:
      try:
        L.append(chr(i))
      except:
        pass

  RE = '[%s]' % ''.join(L)
  return re.compile(RE, re.UNICODE)

def generate_unicodes():
  with codecs.open(config.text_source, encoding='utf-8', mode='r') as src:
    content = src.read()
    words = set([])
    RE = build_re()
    for n in RE.findall(content):
      words.add(n)

    unicodes = '\n'.join(['U+%04x' % ord(c) for c in list(words)])
    with codecs.open(config.unicodes_output, encoding='utf-8', mode='w+') as out:
      out.write(unicodes)

def subset(font_source, unicodes_output, font_output):
  command = f'{config.pyftsubset} "{font_source}" --unicodes-file="{unicodes_output}" --output-file="{font_output}"'
  print('\n\n', command, '\n\n')
  subprocess.Popen(command, shell=True).wait()


generate_unicodes()
subset(config.font_source, config.unicodes_output, config.font_output)