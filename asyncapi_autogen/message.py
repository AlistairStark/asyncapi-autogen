import abc


class Message(abc.ABC):
    """Base class for topic data.

    Child classes must include the TOPIC name.

    Child classes should also be dataclasses, and optional extra information for
    documenting fields can be added using the fields metadata keyword argument.

    ex.
    @dataclass
    MyMessage(Message):
        TOPIC = 'shared.example-topic'

        example_field: str
        example_field_with_docs: str = field(
            metadata={
                "description": "This is an example field",
                "example": "example field content example"
            }
        )
    """

    # don't add type hints here, it will break the api spec generation
    TOPIC = ""  # type: ignore
    headers = {}  # type: ignore
