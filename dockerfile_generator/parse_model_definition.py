import yaml
import os


allowed_languages = ['python', 'java', 'C', 'C++']

def parse_model_definition(model_definition_file):
    '''Parse the model definition file and return the spec section.'''
    with open(model_definition_file) as f:
        model_definition = yaml.safe_load(f)
    spec_section = model_definition.get('spec')
    if spec_section is None:
        raise Exception('No spec section in model definition')
    return spec_section

def parse_language_section(spec_section):
    '''Parse the language section of the spec.
    
    Raises an exception if the language section is not present or if the
    language is not supported.
    
    Should apply default values for optional parameters.'''
    language_section = spec_section.get('language')
    if language_section is None:
        raise ValueError('No language section in model definition')

    for language in language_section:
        if language not in allowed_languages:
            raise ValueError('Language {} is not supported'.format(language))

    return language_section

def parse_os_dependencies_section(spec_section):
    '''Parse the os_dependencies section of the spec.
    
    Returns None if the os_dependencies section is not present.

    Should apply default values for optional parameters.
    '''
    os_dependencies = spec_section.get('os_dependencies')
    if os_dependencies is None:
        os_dependencies = None
    else:
        os_dependencies = " ".join(os_dependencies)

    return os_dependencies


def parse_full(model_definition_path):
    spec = parse_model_definition(model_definition_path)

    out_dict = {}
    out_dict['os_dependencies'] = parse_os_dependencies_section(spec)

    language_section = parse_language_section(spec)
    for language in language_section:
        if 'language' not in out_dict:
            out_dict['language'] = language
    
    language_spec = language_section.get(out_dict['language'])
    out_dict['version'] = language_spec.get('version')
    out_dict['dependencies'] = language_spec.get('dependencies')

    print(out_dict)


parse_full(os.path.join(os.path.dirname(__file__), 'model_definition.yaml'))


