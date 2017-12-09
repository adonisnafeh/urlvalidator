=============================
urlvalidator |latest-version|
=============================

|travis-master| |coverage-master|

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


.. |travis-master| image:: https://travis-ci.org/adonisnafeh/urlvalidator.svg?branch=master
   :alt: Build Status - master branch
   :target: https://travis-ci.org/adonisnafeh/urlvalidator
.. |coverage-master| image:: https://coveralls.io/repos/github/adonisnafeh/urlvalidator/badge.svg?branch=master
   :alt: Coverage of the code
   :target: https://coveralls.io/github/adonisnafeh/urlvalidator?branch=master
.. |latest-version| image:: https://badge.fury.io/py/urlvalidator.svg
   :alt: Latest version on Pypi
   :target: https://badge.fury.io/py/urlvalidator