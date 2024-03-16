class A:
    def  hello ( self ):
        print ( 'Hello from class A' )
 
 
class  B ( A ):
    def  hello ( self ):
        print ( 'Hello from class B' )
 
 
class  C ( A ):
    def  hello ( self ):
        print ( 'Hello from class C' )
 
 
class  D ( A ,  C ):
    pass

D().hello()