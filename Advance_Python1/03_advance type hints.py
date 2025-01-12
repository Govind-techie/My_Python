# Advance Type Hints : We use a typing module to import various advance types and are used as hints.

from typing import List,Tuple,Dict,Union # Here, we imported different datatypes for hints using typing module.

a : List[int] = [1,2,3,4,5] # Here, we defines that a is a list of integer as values in it.

b : Tuple[int,str] = ("Govind",1,2,3,4) # Here, we defines that b is a tuple having integer and string as values in it 

c : Dict[str,int] = {"Name" : "Govind", "age": 16} # Here, we defines that c is a dict having string and an integer as (key/value ) pairs in it.

d : Union[str,int,bool,float] = "Id,12,3.4,True" # Here, we defines that d is a Union having (str,int,bool,float) and can accept multiple types.



