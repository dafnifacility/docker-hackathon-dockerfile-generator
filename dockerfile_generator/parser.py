import os

import yaml

allowed_languages = ['python', 'java', 'C', 'C++']

def parse_model_definition(model_definition_file):
    '''Parse the model definition file.'''
    with open(model_definition_file) as f:
        model_definition = yaml.safe_load(f)
    return model_definition

def parse_language_section(model_definition):
    '''Parse the language section of the model definition.
    
    Raises an exception if the language section is not present or if the
    language is not supported.
    
    Should apply default values for optional parameters.'''
    spec_section = model_definition.get('spec')
    if spec_section is None:
        raise Exception('No spec section in model definition')

    language_section = spec_section.get('language')
    if language_section is None:
        raise ValueError('No language section in model definition')

    for language in language_section:
        if language not in allowed_languages:
            raise ValueError('Language {} is not supported'.format(language))

    return language_section

def parse_os_dependencies_section(model_definition):
    '''Parse the os_dependencies section of the model definition.
    
    Returns None if the os_dependencies section is not present.

    Should apply default values for optional parameters.
    '''
    spec_section = model_definition.get('spec')

    language_section = spec_section.get('os_dependencies')
    if language_section is None:
        language_section = None

    return language_section


def parse_full()
    raw = parse_model_definition(
        os.path.join(os.path.dirname(__file__), 'model_definition.yml')
        )
    lang = parse_language_section(raw)
    os_deps = parse_os_dependencies_section(raw)
    os_deps = raw['spec'].get('os_dependencies', None)

    return {"language": lang, "os_deps": os_deps}
