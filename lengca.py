import genanki
import random


deckname = "Mandarin Dasar"
sourcefilename = 'Mandarin HSK Dasar.txt'
filename = f"Import-{deckname}.apkg"

# Define Anki note model

unique_id = random.randrange(1 << 30, 1 << 31) # Generate a random ID

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


deck = genanki.Deck(unique_id, deckname)

with open(sourcefilename, 'r', encoding='utf-8') as file:
	for line in file:
		line = line.strip()  # Remove leading/trailing whitespace

		if line:
			parts = line.split('-')
			hanzi = parts[0].split('(')[0].strip()  # Extract the Chinese word
			pinyin = parts[0].split('(')[1].strip()  # Extract the Pinyin
			meaning = parts[1].strip()  # Extract the meaning

			note = genanki.Note(
						model=model,
						fields=[hanzi, "("+pinyin, meaning]
						)

			deck.add_note(note)


# Save the deck to an Anki package (*.apkg) file
genanki.Package(deck).write_to_file(f'{deckname}.apkg')

