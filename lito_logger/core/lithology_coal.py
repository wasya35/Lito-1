# lithology_coal.py

# Coal-bearing lithology database
lithology_database = {
    'coal': {
        'description': 'Coal',
        'hatch_pattern': '////'
    },
    'coaly': {
        'description': 'Coaly',
        'hatch_pattern': '\\//'
    },
    'argillites': {
        'description': 'Argillites',
        'hatch_pattern': '......'
    },
    'siltstone': {
        'description': 'Siltstone',
        'hatch_pattern': '++++++'
    },
    'sandstone': {
        'description': 'Sandstone',
        'hatch_pattern': '------'
    }
}

def get_lithology_info(lithology_type):
    return lithology_database.get(lithology_type, 'Lithology type not found.')