class Meta ( type ): 
    def __init__ ( cls , name , bases , attrs ):
        super (). __init__ ( name , bases , attrs )
        cls . __name__ = cls . __name__ . upper ()
 
 
class MyClass ( metaclass = Meta ): 
    pass

print(MyClass.__name__)