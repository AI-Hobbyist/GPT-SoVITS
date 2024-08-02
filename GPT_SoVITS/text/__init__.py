import os
if os.environ.get("version","v1")=="v1":
  from text.symbols import symbols
else:
  from text.symbols2 import symbols

_symbol_to_id = {s: i for i, s in enumerate(symbols)}

def cleaned_text_to_sequence(cleaned_text):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  phones = [_symbol_to_id[symbol] for symbol in cleaned_text]
  return phones

