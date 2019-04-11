from anonymizer.anonymize import Anonymizer
from anonymizer.faker_type import FakerType

if __name__ == '__main__':
    names = ['Kevin Bell', 'Ricky Sheppard', 'James Hill MD', 'Judith Crawford',
             'Christopher Garza', 'Lindsey Briggs', 'Andrew Bowers', 'Tracy Tyler',
             'Ashlee Green', 'Matthew Burch']
    anonymizer = Anonymizer(faker_type=FakerType.NAME)
    anonymizedNames = anonymizer.get_anonymized_names(names)
    originalNames = anonymizer.get_original_names(anonymizedNames)
    print("Anonymized Names = ", anonymizedNames)
    print("Original Names = ", originalNames)