import json
from flashtext import KeywordProcessor

def load_json_data(file_path):
    """ Load JSON data from a file. """
    with open(file_path, 'r') as file:
        return json.load(file)

def find_tags_in_text(textStr, keywords):
    """ Find tags in the given text using the KeywordProcessor. """
    keyword_processor = KeywordProcessor()
    keyword_processor.add_keywords_from_list(keywords)
    return keyword_processor.extract_keywords(textStr)


def load_distinct_tags_from_dict(file_path,dict_nameStr,tagsStr):
    """ Load all distinct tags from a JSON file. """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            tagsSet = set()  # Using a set to avoid duplicates
            for entry in data[dict_nameStr]:
                for tag in entry[tagsStr]:
                    tagsSet.add(tag.lower())  # Adding tags in lowercase for uniqueness
            return list(tagsSet)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} could not be parsed.")
        return []

def create_key_tags_index(data,dict_nameStr,tagsStr,resStr):
    """ Create a hash table (dictionary) for tags and their treatments. """
    tag_index = {}
    for entry in data[dict_nameStr]:
        for tag in entry[tagsStr]:
            tag_lower = tag.lower()
            tag_index.setdefault(tag_lower, []).append(entry[resStr])
    return tag_index

def find_key(tags, tag_index):
    """ Find keys for given tags using the tag index. """
    keys = set()
    for tag in tags:
        matched_keys = tag_index.get(tag.lower(), [])
        keys.update(matched_keys)
    return list(keys)


def exec_search(inputStr,data,dict_nameStr,tagsStr,resStr):
    if data is not None:
        tag_index = create_key_tags_index(data,dict_nameStr,tagsStr,resStr)
        keys = find_key(inputStr, tag_index)
        if keys:
            for key in keys:
                return(key)
        else:
            return("No keys found for the given tags.")
    else:
        return("Unable to proceed without valid data.")
    