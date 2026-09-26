# Text Normalization for TTS — Complete Rules

ElevenLabs models (especially smaller/faster ones like Flash v2.5) mispronounce raw numbers, symbols, dates, and abbreviations. Always normalize before sending to TTS.

## Number Normalization

| Type | Raw | Normalized |
|------|-----|-----------|
| Cardinal | `123` | one hundred twenty-three |
| Cardinal (large) | `1,000,000` | one million |
| Ordinal | `2nd` | second |
| Ordinal | `21st` | twenty-first |
| Decimal | `3.14` | three point one four |
| Fraction | `⅔` | two-thirds |
| Fraction | `3/4` | three-quarters |
| Roman numeral | `XIV` | fourteenth (or "the fourteenth" if a title) |

## Currency Normalization

| Raw | Normalized |
|-----|-----------|
| `$42.50` | forty-two dollars and fifty cents |
| `$1,000,000` | one million dollars |
| `£1,001.32` | one thousand and one pounds and thirty-two pence |
| `€500` | five hundred euros |
| `¥1000` | one thousand yen |
| `₹500` | five hundred rupees |
| `₹5,00,000` | five lakh rupees |
| `₹1.5Cr` | one and a half crore rupees |
| `₹5L` | five lakh rupees |
| `₹10,00,00,000` | one hundred crore rupees |

**Hindi/Indian currency rule:** Indian numbering system uses lakh (1,00,000) and crore (1,00,00,000). Always expand using lakh/crore terminology for Hindi/Hinglish scripts. For English scripts targeting Indian audience, use lakh/crore. For international English, use million/billion.

## Date & Time Normalization

| Raw | Normalized |
|-----|-----------|
| `2024-01-15` | January fifteenth, twenty twenty-four |
| `01/02/2023` | January second, twenty twenty-three (US) or first of February, twenty twenty-three (UK/India) |
| `9:30 AM` | nine thirty AM |
| `14:30` | two thirty PM |
| `9:00` | nine o'clock |
| `2025` (as year) | twenty twenty-five |
| `1990s` | the nineteen nineties |

**Context rule:** If the script is for an Indian audience, use DD/MM/YYYY interpretation. If unclear, state both.

## Abbreviation Expansion

| Raw | Normalized | Note |
|-----|-----------|------|
| `Dr.` | Doctor | |
| `Mr.` | Mister | |
| `Mrs.` | Missus | |
| `govt` | government | Common in Hindi/Indian English |
| `Ave.` | Avenue | |
| `St.` | Street | But "St. Patrick" stays — context-dependent |
| `etc.` | etcetera | |
| `vs.` | versus | |
| `e.g.` | for example | |
| `i.e.` | that is | |
| `approx.` | approximately | |
| `dept.` | department | |
| `Jan.` | January | (and other month abbreviations) |

## Unit Expansion

| Raw | Normalized |
|-----|-----------|
| `100km` | one hundred kilometers |
| `5kg` | five kilograms |
| `30°C` | thirty degrees Celsius |
| `100%` | one hundred percent |
| `50ml` | fifty milliliters |
| `6ft` | six feet |
| `TB` | terabyte |
| `GB` | gigabyte |
| `MHz` | megahertz |
| `sq ft` | square feet |

## Phone Numbers

Spell each digit, group with pauses:
- `555-123-4567` → five five five, one two three, four five six seven
- `+91 98765 43210` → plus ninety-one, nine eight seven six five, four three two one zero

## URLs and Technical

| Raw | Normalized |
|-----|-----------|
| `example.com` | example dot com |
| `elevenlabs.io/docs` | eleven labs dot io slash docs |
| `Ctrl+Z` | control Z |
| `Ctrl+C` | control C |
| `@` | at |
| `#` | hashtag (social media) or number (general) |
| `&` | and |

## Symbols

| Raw | Normalized |
|-----|-----------|
| `+` | plus |
| `-` (math) | minus |
| `=` | equals |
| `>` | greater than |
| `<` | less than |
| `*` | times (math) or star (general) |
| `/` | slash or divided by (math context) |

## Edge Cases

1. **Model numbers**: Leave as-is. "iPhone 15" stays "iPhone 15", not "iPhone fifteen"
2. **Version numbers**: "v3" stays "v3" or expand to "version three" based on context
3. **Acronyms that are words**: "NASA" stays "NASA" (read as word). "FBI" stays "FBI" (read as letters). The TTS model handles these correctly.
4. **Mixed alphanumeric**: "A4 paper" stays "A four paper". "B12 vitamin" stays "B twelve vitamin"
5. **Addresses**: `123 Main St` → "one two three Main Street" (spell out house numbers digit by digit for addresses)
6. **Hindi mixed**: `₹5L ka phone` → "paanch lakh ka phone" (for Hinglish) or "five lakh ka phone" (for mixed)
