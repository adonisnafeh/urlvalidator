urlvalidator
==============

URLValidator and EmailValidator classes from Django extracted to a separate package.
Used to avoid adding django dependency to a python only project.

Installation
------------

pip install ``urlvalidator`` (or add to your requirements.txt)


Usage
-----

.. code-block:: python

    from urlvalidator import validate_url, validate_email, ValidationError


    try:
       validate_url("https://www.google.com")
    except ValidationError:
       raise ValidationError("Invalid URL")

    try:
       validate_email("test@example.com")
    except ValidationError:
       raise ValidationError("Invalid Email")


License
-------

3 Clause BSD.

Bug report and Help
-------------------

For bug reports open a github ticket. Patches gratefully accepted.