#There are three ways that the parent and child classes
# can interact:
# 1. Actions on the child imply an action on the parent.
# 2. Actions on the child override the action on the parent.
# 3. Actions on the child alter the action on the parent.


#-----------------------------------------------------#
# Implicit Inheritance

## class Parent(object):

##     def Implicit(self):
##         print("Parent implicit()")

## class Child(Parent):
##     pass

## dad = Parent()
## son = Child()

## dad.Implicit()
## son.Implicit()
#-----------------------------------------------------#
# Override Explicitly

## class Parent(object):
##     def override(self):
##         print("Parent override()")

## class Child(Parent):

##     def override(self):
##        print("Child override()")

## dad = Parent()
## son = Child()

## dad.override()
## son.override()
#-----------------------------------------------------#
# Alter Before or After

## class Parent(object):

##     def altered(self):
##         print("Parent altered()")

## class Child(Parent):

##     def altered(self):
##         print("Child, before Parent altered()")
##         super(Child, self).altered()
##         print("Child, after the Parent altered()")

## dad = Parent()
## son = Child()

## dad.altered()
## son.altered()
#-----------------------------------------------------#
# All Three Combined

## class Parent(object):

##     def override(self):
##         print("Parent override()")
    
##     def implicit(self):
##         print("Parent implicit()")
    
##     def altered(self):
##         print("Parent altered()")

## class Child(Parent):

##     def override(self):
##         print("Child override()")
    
##     def altered(self):
##         print("Child, before Parent altered()")
##         super(Child, self).altered()
##         print("Child, after Parent altered()")

## dad = Parent()
## son = Child()

## dad.implicit()
## son.implicit()

## dad.override()
## son.override()

## dad.altered()
## son.altered()
#-----------------------------------------------------#
# Composition

class Other(object):

    def override(self):
        print("Other override()")
    
    def implicit(self):
        print("Other implicit()")
    
    def altered(self):
        print("Other altered()")

class Child(object):

    def __init__(self):
        self.other = Other()
    
    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print("Child override()")
    
    def altered(self):
        print("Child, before Other altered()")
        self.other.altered()
        print("Child, after Other altered()")

son = Child()

son.implicit()
son.override()
son.altered()

# 1. Avoid multiple inheritance at all costs, as it’s too
# complex to be reliable. If you’re stuck with it, then be
# prepared to know the class hierarchy and spend time finding
# where everything is coming from.

# 2. Use composition to package code into modules that are
# used in many different unrelated places and situations.

# 3. Use inheritance only when there are clearly related
# reusable pieces of code that fit under a single common
# concept or if you have to because of something you’re using.