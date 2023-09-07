import genanki
import random
import re

sourcefilename = 'Mandarin Industry.txt'
deckname = sourcefilename.split(".")[0]
categories = [
    "Management",
    "Production",
    "Safety",
    "Quality",
    "Training",
    "Workflow",
    "Logistics",
    "Resources",
    "Maintenance"
]


# Define Anki note model
model_id = 1607392619

CARD_CSS = """
.card {
    font-family: 'Your Font Name', sans-serif;
    font-size: 30px;
    text-align: center;
}

.front .hanzi {
    font-weight: bold;
    font-size: 45px;
    /* Add your front Hanzi font styles here */
}

.front .pinyin {
    font-style: italic;
    /* Add your front Pinyin font styles here */
}

.back .hanzi {
    font-weight: bold;
    font-size: 45px;
    /* Add your back Hanzi font styles here */
}

.back .pinyin {
    font-style: italic;
    /* Add your back Pinyin font styles here */
}

.meaning {
    font-size: 30px;
}
"""

model = genanki.Model(
    model_id,
    'Mandarin Hack',
    fields=[
        {'name': 'Hanzi'},
        {'name': 'Pinyin'},
        {'name': 'Meaning'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<div class="front"><div class="hanzi">{{Hanzi}}</div><div class="pinyin">{{Pinyin}}</div></div>',
            'afmt': '<div class="back"><div class="hanzi">{{Hanzi}}</div><div class="pinyin">{{Pinyin}}</div><hr id="answer"><div class="meaning">{{Meaning}}</div></div>',
        },
        {
            'name': 'Card 2',
            'qfmt': '<div class="front"><div class="meaning">{{Meaning}}</div></div>',
            'afmt': '<div class="back"><div class="hanzi">{{Hanzi}}</div><div class="pinyin">{{Pinyin}}</div><hr id="answer"><div class="meaning">{{Meaning}}</div></div>',
        },
    ],
    css=CARD_CSS
)

deck_ids = {
    'Management': 1234567890,
    'Production': 2345678901,
    'Safety': 3456789012,
    'Quality': 4567890123,
    'Training': 5678901234,
    'Workflow': 6789012345,
    'Logistics': 7890123456,
    'Resources': 8901234567,
    'Maintenance': 9012345678
}

decks = {}
for category in categories:
    unique_id = deck_ids[category]  #random.randrange(1 << 30, 1 << 31) # Generate a random ID
    decks[category] = genanki.Deck(unique_id, f"{deckname}::{category}")

with open(sourcefilename, 'r', encoding='utf-8') as file:
	for line in file:
		line = line.strip()  # Remove leading/trailing whitespace
		if line:
			parts = line.split('-')
			hanzi = parts[0].split(' ')[0]  # Extract the Chinese word
			pinyin = re.search(r'\((.*?)\)', parts[0]).group(1) if re.search(r'\((.*?)\)', parts[0]) else None
			meaning = parts[1].strip() # Extract the meaning
			category = parts[2].strip()  # Extract the category
			print(hanzi)
			print(pinyin)
			print(meaning)
			print(category)
			try:
				print("try")
				if category in categories:
					print("creating")
					note = genanki.Note(
						model=model,
						fields=[hanzi, pinyin, meaning],
						tags=[category]
						)
					decks[category].add_note(note)
			except Exception as e:
				print(e)

# Save the deck to an Anki package (*.apkg) file
deck_list = list(decks.values())
genanki.Package(deck_list).write_to_file(f'{deckname}.apkg')

