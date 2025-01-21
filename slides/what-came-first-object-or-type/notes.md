# Origin quesion

Everything in Python is an object, even object. But also everything is of type type. So which is the UR-thing?

## object

> The base class of the class hierarchy

inserted as the base MRO, even when not asked for
gives most classes default behavior of dunders

`type(object) == 'type'`
`isinstance(object, type) == True`
`isinstance(object, object) == True`
`issubclass(object, type) == False`
`issubclass(object, object) == True`

`object.__class__ == 'type'`
`object.__mro__ == ('object')`

## type

creates new classes (functional class statement)
type is the original metaclass
  other classes are isinstances of type
but type is a subclass of object because all things in python are objects and type is a first class object, not some language construct.

`type(type) == 'type'`
`isinstance(type, object) == True`
`isinstance(type, type) == True`
`issubclass(type, object) == True`
`issubclass(type, type) == True`

`type.__class__ == 'type'`
`type.__mro__ == ('type', 'object')`

## custom things
`o = object()`
`class O(object)`
`t = type('t', (), {})`
`class T(type)`

## Answer Thuoghts
object creates instances
type creates classes
but classes are themselves instances
everything is an instance (created by a class) but not everything is a class (can create new instances)
some instances can create classes (metaclasses)
some instances can create other instances (classes)
some instances can create neither (what we typically call instances - instances of user classes(others))

`type()` of everything is (eventually) type because `type()` answers the question "what class created this?"
no builtin to ask direct parentage of a thing. But last on the list of every class's MRO is `object`
