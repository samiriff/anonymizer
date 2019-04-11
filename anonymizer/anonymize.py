from faker import Faker
from anonymizer.faker_type import FakerType


class Anonymizer:
    '''
    This class takes care of anonymizing names and keeping track of the names before and after anonymization
    '''

    def __init__(self, faker_type=FakerType.NAME, names=[]):
        '''
        Constructor that accepts a list of names as an optional argument and initializes a dictionary to track
        the anonymous names mapped to each entry in this list
        :param type: string containing the faking operation that has to be performed. Default: name
        :param names: List of strings (optional) that have to be anonymized
        '''
        self._faker = Faker()
        self._faker_type = faker_type
        self._nameMap, self._reverseMap = self.get_mapping(names)

    def get_mapping(self, names):
        '''
        Gets a dictionary mapping each name in the given list to an anonymous name
        :param names: List of string that have to be anonymized
        :return: Dictionary
        '''
        nameMap = {name: self.get_fake_name() for name in names}
        reverseMap = {anonName: name for name, anonName in enumerate(nameMap)}
        return nameMap, reverseMap

    def get_anonymized_name(self, name):
        '''
        Anonymizes the given name and keeps track of the original name for future reference
        :param name: string containing the name that has to be anonymized
        :return: string containing anonymized name
        '''
        if name not in self._nameMap:
            anonName = self.get_fake_name()
            self._nameMap[name] = anonName
            self._reverseMap[anonName] = name
        return self._nameMap[name]

    def get_anonymized_names(self, names):
        '''
        Anonymizes the given list of names and keeps track of the original names for future reference
        :param names: list containing names that have to be anonymized
        :return: list containing anonymized names
        '''
        return [self.get_anonymized_name(name) for name in names]

    def get_original_name(self, anonName):
        '''
        Gets the original name corresponding to the given anonymized name
        :param anonName: string containing anonymized name
        :return: string containing original name
        '''
        return self._reverseMap[anonName] if anonName in self._reverseMap else None

    def get_original_names(self, anonNames):
        '''
        Gets the list of original names corresponding to the given list of anonymized names
        :param anonNames: list containing anonymized names
        :return: list containing original names
        '''
        return [self.get_original_name(anonName) for anonName in anonNames]

    def get_fake_name(self):
        if self._faker_type == FakerType.NAME:
            return self._faker.name()
        elif self._faker_type == FakerType.ADDRESS:
            return self._faker.address()
        return None