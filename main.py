"""Code to parse morse code."""

from argparse import ArgumentParser
from os.path import exists
from sys import exit as e

def error_message(msg):
    print(f"\n[ERROR] {msg}")
    e(1)

parser = ArgumentParser(prog="Morse code translator.")
parser.add_argument("file", type=str)
parser.add_argument("--morse", default=False, action="store_true")
args = parser.parse_args()
file = args.file
morsify = args.morse

if not exists(file):
    error_message(f"File \"{file}\" was not found.")

with open(file, "r", encoding="utf-8") as f:
    content = f.read()

morse = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '/': ' ',

    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',

    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '-.-.--': '!',
}

if morsify:
    morse = {v: k for k,v in morse.items()}
    translated_text = " ".join(morse[x] if x in morse else x for x in content.upper())
    print(translated_text)
else:
    content = content.split(" ")
    translated_text = "".join(morse[x] if x in morse else x for x in content)
    print(translated_text)
