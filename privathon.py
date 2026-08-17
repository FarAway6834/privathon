from time import time as __unix_time__
from random import random as __random_of_unit_interval__
from types import SimpleNamespace as namespace
from martialaw.martialaw import martialaw as __clsr__
from martialaw.martialaw import partial as __partial__
from functools import wraps as __smart_deco_wraps__
import builtins as __builtin__

__import__("warnings").warn("recommended not to use. it's version 0.0.2... that's indev. indev(fix bug)-infdev(make function scope as privatly) dev age is written in repo. come to see if you want! :)")

"""
# privathon.py

private scoped python

## DEPENDENCY

1. 1 modules
2. 6 module::functions / module::classes
3. 0 module::all_resource

### 1 modules

 - builtins as __builtin__
 - end

### 1 module::functions / module::classes

 - martialaw.martialaw::martialaw as __clsr__
 - martialaw.martialaw::partial as __partial__
 - functools::wraps as __smart_deco_wraps__
 - types::SimpleNamespace as namespace
 - time::time as __unix_time__
 - random::random as __random_of_unit_interval__
 - end

### 0 module::all_resource

 - end

## RESOURCES

1. 1 CONSTANTS
2. 4 LAMBDAS
3. 1 FUNCTIONS
4. 2 CLASSES

### 1 CONSTANTS

1. 1 builtin scope
2. 0 public scope
3. 0 local scope
4. 0 private scope

#### 1 builtin scope

 - constant_err = ConstantError("const is immutable")

 ```markdown
 # constant_err

 writing...
 ```

 - end

#### 0 public scope

 - end

#### 0 local scope

 - end

#### 0 private scope

 - end

### 9 LAMBDAS

1. 4 builtin scope
2. 0 public scope
3. 0 local scope
4. 0 private scope

#### 4 builtin scope

 - __set_builtin_scope__ = __clsr__(lambda name, value : setattr(__builtin__, name, value))

````markdown
# @__set_builtin_scope__(name : str) decorator

set name as (name : str) to set var in builtin scope

## for example

1. variable

```python
@__set_builtin_scope__("example")
_ = 45510

print(example == 45510) # True
```

2. lambda

```python
@__set_builtin_scope__("example")
_ = lambda : 45510

print(example() == 45510) # True
```

3. function

```python
@__set_builtin_scope__("example")
def example():
    return 45510

print(example() == 45510) # True
```

4. class

```python
@__set_builtin_scope__("AmamiyaGoro")
class AmamiyaGoro:
    def __str__(self):
        return "Social Justice"

class HoshinoAkuamarin(AmamiyaGoro):
    def __str__(self):
        return "Social ills"
```

 - fin -
````

 - __on_builtin_scope__ = lambda named_obj : __set_builtin_scope__(named_obj.__name__, named_obj)

````markdown
# @__on_builtin_scope__ decorator

1. function

```python
@__on_builtin_scope__
def example():
    return 45510
```

is

```python
@__set_builtin_scope__("example")
def example():
    return 45510
```

2. class

```python
@__on_builtin_scope__
class AmamiyaGoro:
    def __str__(self):
        return "Social Justice"
```

is

```python
@__set_builtin_scope__("AmamiyaGoro")
class AmamiyaGoro:
    def __str__(self):
        return "Social Justice"
```

- fin -
````

 - call_constant_functor = lambda f : f()

````markdown
# function call_constant_functor

 - fin -
````

 - salt = lambda : hash(str(__unix_time__() + __random_of_unit_interval__()))

````markdown
# function salt

 - fin -
````

 - end

#### 0 public scope

 - end

#### 0 local scope

 - end

#### 0 private scope

 - end

### 1 FUCNTIONS

1. 0 builtin scope
2. 1 public scope
3. 0 local scope
4. 0 private scope

#### 0 builtin scope

 - end

#### 1 public scope

 - raise_constant_err
 - end

#### 0 local scope

 - end

#### 0 private scope

 - end

### 2 CLASSES

1. 1 builtin scope
2. 1 public scope
3. 0 local scope
4. 0 private scope

#### 1 builtin scope

 - ConstantError
 - end

#### 1 public scope

 - private
 - end

#### 0 local scope

 - end

#### 0 private scope

 - end

"""

@__clsr__
__builtin__.__set_builtin_scope__ = lambda name, value : setattr(__builtin__, name, value) #plz make this cythonic. str * obj -> Nonetype

@__set_builtin_scope__("__builtin_scope__")
__on_builtin_scope__ = lambda named_obj : __set_builtin_scope__(named_obj.__name__, named_obj) #this is also obj -> Nonetype

@__set_builtin_scope__("call_constant_functor")
call_constant_functor = lambda f : f() #this also object -> object

@__builtin_scope__
class ConstantError(Exception):
    """
    # error ConstantError

    writing...

     - fin -
    """
     
    pass

@__on_builtin_scope__("constant_err")
constant_err = ConstantError("const is immutable") # are you crazy? it's too easy to crack

def raise_constant_err():
    """
    # function raise_constant_err()

    writing...

     - fin -
    """
    raise constant_err # fuck... it's too easy to crack... please wrap as c void function

@__set_builtin_scope__("salt")
salt = lambda : hash(str(__unix_time__() + __random_of_unit_interval__())) #it's too easy to crack... please wrap as c void function

class private(type):
    """
    # metaclass private
    
    ## as metaclass

    writing...
    
    ## static methods
    
    1. 9 LAMBDAS
    2. 2 FUNCTIONS

    ### 5 LAMBDAS
    
     - sealed_value = lambda value : const(lambda self : value)
    
    ````markdown
    # function sealed_value
    
     - fin -
    ````

     - static = __clsr__(lambda __static__,     func : __smart_deco_wraps__(__partial__(func, __static__ = __static__)))
    
    ````markdown
    # @static(__static__) decorator
    
     - fin -
    ````
    
     - static_decocls = lambda cls : static(call_constant_functor(cls))
    
    ````markdown
    # decorator static_decocls
    
     - fin -
    ````
    
     - end
    
    ## 1 FUNCTIONS
    
    - sealed_value
    - end
    
    ## as for lib

    writing...
    
     - fin -
    """
    
    @staticmethod
    @__clsr__
    seal = lambda getter, setter : property(fget = getter, fset = setter) # it's too easy to hack... damb. I've no idea 2 solve this problem

    @staticmethod
    const = lambda constant_function : private.seal(constant_function)(raise_constant_err) # it's too easy to crack or neutralize... I give up. go last line

    @staticmethod
    def sealed_value(var):
        """
        # function sealed_value
        
         - fin -
        """
        @private.seal(lambda self : var)
        def ret(self, value):
            nonlocal var
            var = value
        return ret

    @staticmethod
    const_value = lambda value : private.const(lambda self : value)

    @staticmethod
    @__clsr__
static = lambda __static__, func : __smart_deco_wraps__(__partial__(func, __static__ = __static__))

    @staticmethod
    static_decocls = lambda cls : static(call_constant_functor(cls))
    
    def __new__(metacls, name, *argv):

        """
        # privathon private class constructor
        
        ## as constructor
        ## as function
        
         - fin -
        """

        L = len(argv)

        assert L * L == L + L, f"private get 1 or 3 arguments but {L} given" # L(L - 2) = 0 ↔ L = 0 ∨ L = 2
        
        if L: # L == 2. check "as constructor
            __dict__ = argv[1]

            @const
            def private(self, private_wraps = {}): # how2works? : hide in getter's arugment
                selfid = id(self)

                if selfid in private_wraps: return private_wraps[selfid] # same ob becuase same address
                else:
                    this = self # this method's self

                    __private__ = __dict__["private"]() # function private's value

                    # object's attribute "private" is actually delete it self, and return object which "this"
                    @const
                    def private(self):
                        del self # pop the private-wrapper objects on "computer memory"
                        return this

                    # when delete the object, private_wraps's object is also unregisterd
                    def __del__(self):
                        __dict__["__del__"](self) # for method "__del__"
                        del private_wraps[selfid]

                    # it returns PrivateWrapper Object. and this src is actually class gen perttern for complete privaty
                    return type(
                            "PrivateWrapper", 
                            (), 
                            {
                                i
                                :
                                (
                                    private if i == "private" else ( # attribute "private"
                                        __del__ if i == "__del__" else ( # method "__del__"
                                            __smart_deco_wraps__(
                                                j # this function get "this" and "__private__"
                                            )(
                                                __partial__(
                                                    j,
                                                    this = self, # refer which "ORIGIN"... actually this src pack in getter as attribuate name "private" to which obj "ORIGIN"
                                                    __private__ = __private__ # class src's private()'s value. generally dictionarry because it's purpose is for dict or list. it's object's private fields
                                                )
                                            )
                                        ) if callable(j) else j)
                                )
                                for i, j in __dict__.items()
                                if i != "__init__" # no __private__ fields in __init__. because __init__ is before __private__ field
                            }
                        )
           return type(
                   metacls,
                   name,
                   argv[0],
                   {
                       i
                       :
                       private if i == "private" else ( # cls.private is generating private-wrapper and return that.
                           __smart_deco_wraps__(
                               j
                            )(
                                __parital__(
                                    j,
                                    this = metacls, # this refer metaclass... it's dummy datas. because non private-wrapper object has no non-private version. this is non-private version. this is "ORIGIN"
                                    __private__ = metacls #privater metaclass. because non private-wrapper object has no __private__ field
                                )
                            ) if callable(j) else j
                        )
                       for i, j in __dict__.items()
                    }
                ) # if this is private, then self is "ORIGIN", if is not, this is "ORIGIN"
        else: return name.private # if L == 1 then just return private. check "as function"

# function scope safe lock lib is inevitable
