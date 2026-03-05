import builtins as __builtin__

"""
# privathon.py

private scoped python

## RESOURCES

1. 1 CONSTANTS
2. 3 LAMBDAS
3. 0 FUNCTIONS
4. 1 CLASSES

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

### LAMBDAS

1. 3 builtin scope
2. 0 public scope
3. 0 local scope
4. 0 private scope

#### 3 builtin scope

 - __on_builtin_scope__ = lambda name : lambda value : setattr(__builtin__, name, value)

````markdown
# @__on_builtin_scope_(name : str) decorator

set name as (name : str) to set var in builtin scope

## for example

1. variable

```python
@__on_builtin_scope__("example")
_ = 45510

print(example == 45510) # True
```

2. lambda

```python
@__on_builtin_scope__("example")
_ = lambda : 45510

print(example() == 45510) # True
```

3. function

```python
@__on_builtin_scope__("example")
def example():
    return 45510

print(example() == 45510) # True
```

4. class

```python
@__on_builtin_scope__("AmamiyaGoro")
class AmamiyaGoro:
    def __str__(self):
        return "Social Justice"

class HoshinoAkuamarin(AmamiyaGoro):
    def __str__(self):
        return "Social ills"
```

 - fin -
````

 - __builtin_scope__ = lambda named_obj : __on_builtin_scope__(named_obj.__name__, named_obj)

````markdown
# @__builtin_scope__ decorator

1. function

```python
@__builtin_scope__
def example():
    return 45510
```

is

```python
@__on_builtin_scope__("example")
def example():
    return 45510
```

2. class

```python
@__builtin_scope__
class AmamiyaGoro:
    def __str__(self):
        return "Social Justice"
```

is

```python
@__on__=builtin_scope__("AmamiyaGoro")
class AmamiyaGoro:
    def __str__(self):
        return "Social Justice"
```

- fin -
````

 - getter_and_setter = lambda getter : lambda setter : property(fget = getter, fset = setter)

````markdown
# @getter_and_setter decorator

## for example to make property "example"

```python
@getter_and_setter
def example(self):
    return 45510

@example
def example(self, value):
    raise AttributeError("constant is immutable")
```

````
 
 - end

#### 0 public scope

 - end

#### 0 local scope

 - end

#### 0 private scope

 - end

### 0 FUCNTIONS

1. 0 builtin scope
2. 0 public scope
3. 0 local scope
4. 0 private scope

#### 0 builtin scope

 - end

#### 0 public scope

 - end

#### 0 local scope

 - end

#### 0 private scope

 - end

### 1 CLASSES

1. 1 builtin scope
2. 0 public scope
3. 0 local scope
4. 0 private scope

#### 0 builtin scope

 - ConstantError
 - end

#### 0 public scope

 - end

#### 0 local scope

 - end

#### 0 private scope

 - end

"""

__builtin__.__on_builtin_scope__ = lambda name : lambda value : setattr(__builtin__, name, value)

@__on_builtin_scope__("__builtin_scope__")
__builtin_scope__ = lambda named_obj : __on_builtin_scope__(named_obj.__name__, named_obj)

@__on_builtin_scope__("getter_and_setter")
getter_and_setter = lambda getter : lambda setter : property(fget = getter, fset = setter)

@__builtin_scope__
class ConstantError(Exception):
    """
    # error ConstantError

    writing...

     - fin -
    """
     
    pass

@__on_builtin_scope__("constant_err")
constant_err = ConstantError("const is immutable")
