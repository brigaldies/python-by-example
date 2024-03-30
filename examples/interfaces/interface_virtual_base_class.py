"""
Example of an interface and classes hierarchy using "virtual base class".:param
"""
import logging

LOG = logging.getLogger("examples")


class PersonMeta(type):
    """A person metaclass"""

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'name') and
                callable(subclass.name) and
                hasattr(subclass, 'age') and
                callable(subclass.age))


class Person(metaclass=PersonMeta):
    """Person interface built from PersonMeta metaclass."""

    def name(self) -> str:
        """ Person's name """
        raise NotImplementedError

    def age(self) -> int:
        """ Person's age"""
        raise NotImplementedError


class PersonSuper:
    """A person superclass"""

    def name(self) -> str:
        """
        Super (base class) Name
        :return: class name
        """
        LOG.info("name: %s", self.__class__)
        return str(self.__class__)

    def age(self) -> int:
        """
        Super (base class) age
        :return: 50
        """
        LOG.info("age: %s", self.__class__)
        return 50


# Inheriting subclasses
class Employee(PersonSuper):
    """Inherits from PersonSuper
    PersonSuper will appear in Employee.__mro__
    """

    def name(self) -> str:
        """
        Employee's name
        :return: class name
        """
        LOG.info("name: %s", self.__class__)
        return str(self.__class__)


class Friend:
    """Built implicitly from Person
    Friend is a virtual subclass of Person since
    both required methods exist.
    Person not in Friend.__mro__
    """

    def name(self) -> str:
        """
        Friend's name
        :return: class name
        """
        LOG.info("name: %s", self.__class__)
        return str(self.__class__)

    def age(self) -> int:
        """
        Friend's age.
        :return: 10
        """
        LOG.info("age: %s", self.__class__)
        return 10


def introduce_person(person: Person) -> None:
    """
    Introduce the person's name and age.
    :param person: Person interface
    :return: None
    """
    LOG.info("Hi %s, you are %d old", person.name(), person.age())


def interface_with_virtual_base_class() -> None:
    """
    Run the example with virtual base class.
    :return: None.
    """
    LOG.info("------------------------------------------------------")
    LOG.info("Running the virtual base class-based interface example")
    person = PersonSuper()
    assert issubclass(person, Person) is True
    LOG.info("PersonSuper MRO: %s", str(PersonSuper.__mro__))
    introduce_person(person)

    employee = Employee()
    assert issubclass(employee, Person) is True
    LOG.info("Employee MRO: %s", str(Employee.__mro__))
    introduce_person(employee)

    friend = Friend()
    assert issubclass(friend, Person) is True
    LOG.info("Friend MRO: %s", str(Friend.__mro__))
    introduce_person(friend)
