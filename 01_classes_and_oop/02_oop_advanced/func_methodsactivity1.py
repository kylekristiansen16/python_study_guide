
class LuxWatch:
    watches_created = 0
    
    def __init__(self):        
        LuxWatch.watches_created += 1
        
    @classmethod
    def get_number_of_watches_created(cls):
        return cls.watches_created
    
    @classmethod
    def with_engraving(cls, engraving):
        print('Class method was called: engrave watch')
        try:
            cls.validate_engraving(engraving)
        except AssertionError as e:
            print(e)
            print('No watch was created')
            _watch = None
        else:
            _watch = cls()
            _watch.engraving = engraving
        finally:
            return _watch
            
    
    @staticmethod
    def validate_engraving(engraving):
        assert len(engraving) < 40, 'Engraving too long'
        assert engraving.isalnum(), 'Engraving can only contain letters and numbers'
        return True
    
w1 = LuxWatch()
print('Number of watches created:', LuxWatch.get_number_of_watches_created())
w2 = LuxWatch.with_engraving('HappyBirthday')
print('Number of watches created:', LuxWatch.get_number_of_watches_created())
w3 = LuxWatch.with_engraving('foo@baz.com')
print('Number of watches created:', LuxWatch.get_number_of_watches_created())