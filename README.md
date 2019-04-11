
# Anonymizer

_Anonymizer_ is a Python package that generates fake data for you. It internally makes use of the [Faker](https://github.com/joke2k/faker) package, and allows you to keep track of the mapping between your original and fake data. This will be especially useful when you are anonymizing data in pandas data frames.

```
   _____                                           .__
  /  _  \    ____    ____    ____  ___.__.  _____  |__|________  ____ _______
 /  /_\  \  /    \  /  _ \  /    \<   |  | /     \ |  |\___   /_/ __ \\_  __ \
/    |    \|   |  \(  <_> )|   |  \\___  ||  Y Y  \|  | /    / \  ___/ |  | \/
\____|__  /|___|  / \____/ |___|  // ____||__|_|  /|__|/_____ \ \___  >|__|
        \/      \/              \/ \/           \/           \/     \/
```

## Basic Usage

### Initialization

```
names = ['Kevin Bell', 'Ricky Sheppard', 'James Hill MD']
anonymizer = Anonymizer()
```

### Get Anonymized Name
```
anonymizer.get_anonymized_name('Ghajinikanth Zuckerberg')
# 'Catherine Parker'
```

### Get Original Name
```
anonymizer.get_original_name('Catherine Parker')
# 'Ghajinikanth Zuckerberg'
```

### Get Anonymized Name for Same Name
```
anonymizer.get_anonymized_name('Ghajinikanth Zuckerberg') # First Call
# 'Catherine Parker'

anonymizer.get_anonymized_name('Ghajinikanth Zuckerberg') # Second Call
# 'Catherine Parker'
```

### Fetch list of Anonymized Names
```
anonymizer.get_anonymized_names(names)
# ['Leslie Adams', 'Michelle Burke', 'Annette Maxwell']
```
### Fetch list of Original Names
```
anonymizer.get_original_names(anonymizedNames)
# ['Kevin Bell', 'Ricky Sheppard', 'James Hill MD']
```
###  Get Anonymized Data for a different Faker Type
```
address_anonymizer = Anonymizer(faker_type=FakerType.ADDRESS)
address_anonymizer.get_anonymized_name('74437 Alexandra Well\nSouth Jade, CT 40282')
# 'USNS Hernandez\nFPO AA 32353'
```
## Acknowledgements
- [Faker](https://github.com/joke2k/faker)