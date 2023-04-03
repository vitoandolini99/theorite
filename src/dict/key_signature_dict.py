import json
from src.dict.res_dict import resolution_dictionary
from vendor.rp import resource_path

key_signature_dictionary = {
    "img/key_signatures/clean.png":
        ("C Major", "D Dorian", "E Phrygian", "F Lydian", "G Mixolydian", "A Minor", "B Locrian"),
    "img/key_signatures/1flat.png":
        ("F Major", "G Dorian", "A Phrygian", "Bb Lydian", "C Mixolydian", "D Minor", "E Locrian"),
    "img/key_signatures/2flat.png":
        ("Bb Major", "C Dorian", "D Phrygian", "Eb Lydian", "F Mixolydian", "G Minor", "A Locrian"),
    "img/key_signatures/3flat.png":
        ("Eb Major", "F Dorian", "G Phrygian", "Ab Lydian", "Bb Mixolydian", "C Minor", "D Locrian"),
    "img/key_signatures/4flat.png":
        ("Ab Major", "Bb Dorian", "C Phrygian", "Db Lydian", "Eb Mixolydian", "F Minor", "G Locrian"),
    "img/key_signatures/5flat.png":
        ("Db Major", "Eb Dorian", "F Phrygian", "Gb Lydian", "Ab Mixolydian", "Bb Minor", "C Locrian"),
    "img/key_signatures/6flat.png":
        ("Gb Major", "Ab Dorian", "Bb Phrygian", "Cb Lydian", "Db Mixolydian", "Eb Minor", "F Locrian"),
    "img/key_signatures/7flat.png":
        ("Cb Major", "Db Dorian", "Eb Phrygian", "Fb Lydian", "Gb Mixolydian", "Ab Minor", "Bb Locrian"),
    "img/key_signatures/1sharp.png":
        ("G Major", "A Dorian", "B Phrygian", "C Lydian", "D Mixolydian", "E Minor", "F# Locrian"),
    "img/key_signatures/2sharp.png":
        ("D Major", "E Dorian", "F# Phrygian", "G Lydian", "A Mixolydian", "B Minor", "C# Locrian"),
    "img/key_signatures/3sharp.png":
        ("A Major", "B Dorian", "C# Phrygian", "D Lydian", "E Mixolydian", "F# Minor", "G# Locrian"),
    "img/key_signatures/4sharp.png":
        ("E Major", "F# Dorian", "G# Phrygian", "A Lydian", "B Mixolydian", "C# Minor", "D# Locrian"),
    "img/key_signatures/5sharp.png":
        ("B Major", "C# Dorian", "D# Phrygian", "E Lydian", "F# Mixolydian", "G# Minor", "A# Locrian"),
    "img/key_signatures/6sharp.png":
        ("F# Major", "G# Dorian", "A# Phrygian", "B Lydian", "C# Mixolydian", "D# Minor", "E# Locrian"),
    "img/key_signatures/7sharp.png":
        ("C# Major", "D# Dorian", "E# Phrygian", "F# Lydian", "G# Mixolydian", "A# Minor", "B# Locrian")
}
with open(resource_path('settings/settings.json')) as settings:
    data = json.loads(settings.read())
height = resolution_dictionary[data["resolution"]][1]

coefficient = height / 540

modes = {("img/text/majorkey.png", (round(271 * coefficient), round(110 * coefficient))): "Major",
         ("img/text/minorkey.png", (round(271 * coefficient), round(110 * coefficient))): "Minor",
         ("img/text/locrian.png", (round(340 * coefficient), round(110 * coefficient))): "Locrian",
         ("img/text/lydian.png", (round(320 * coefficient), round(110 * coefficient))): "Lydian",
         ("img/text/mixolydian.png", (round(465 * coefficient), round(110 * coefficient))): "Mixolydian",
         ("img/text/dorian.png", (round(320 * coefficient), round(110 * coefficient))): "Dorian",
         ("img/text/phrygian.png", (round(395 * coefficient), round(110 * coefficient))): "Phrygian"
}
