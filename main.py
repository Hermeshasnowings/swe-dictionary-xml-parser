import xml.etree.ElementTree as ET
import json

# Parse the XML file
tree = ET.parse('swe_eng.xml')
root = tree.getroot()

# List to store all words
words_list = []

# Iterate over each word in the XML
for word in root.findall('Word'):
    word_data = {
        "ID": word.get("ID"),
        "MatchingID": word.get("MatchingID"),
        "Type": word.get("Type"),
        "Value": word.get("Value"),
        "Variant": word.get("Variant"),
        "VariantID": word.get("VariantID"),
        "BaseLang": {
            "Meaning": word.find("BaseLang/Meaning").text if word.find("BaseLang/Meaning") is not None else None,
            "Comment": word.find("BaseLang/Comment").text if word.find("BaseLang/Comment") is not None else None,
            "Phonetic": {
                "Text": word.find("BaseLang/Phonetic").text if word.find("BaseLang/Phonetic") is not None else None
            },
            "Example": word.find("BaseLang/Example").text if word.find("BaseLang/Example") is not None else None,
            "Index": word.find("BaseLang/Index").get("Value") if word.find("BaseLang/Index") is not None else None
        },
        "TargetLang": {
            "Translation": word.find("TargetLang/Translation").text if word.find("TargetLang/Translation") is not None else None,
            "Synonym": word.find("TargetLang/Synonym").text if word.find("TargetLang/Synonym") is not None else None,
            "Comment": word.find("TargetLang/Comment").text if word.find("TargetLang/Comment") is not None else None,
            "Example": word.find("TargetLang/Example").text if word.find("TargetLang/Example") is not None else None
        }
    }
    
    # Append the word data to the list
    words_list.append(word_data)

# Write the JSON data to a file
with open('swedish_words.json', 'w', encoding='utf-8') as json_file:
    json.dump(words_list, json_file, ensure_ascii=False, indent=4)

print("XML data has been converted to JSON format.")
