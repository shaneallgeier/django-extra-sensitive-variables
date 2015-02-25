Django Extra Sensitive Variables
================================

About
-----
extra_sensitive_variables is a third-party exception filter for Django. This
allows you to globally censor a set of default variable names in Django's error
reports regardless of a function's lack of @sensitive_* decorators. Basically,
any variable matching the names provided in settings.EXTRA_SENSITIVE_VARIABLES
or settings.EXTRA_SENSITIVE_POST_PARAMETERS will be censored.

Installation
------------
::

  pip install django-extra-sensitive-variables

Then add the following variables to your settings.py and modify them as you see fit:
::

  EXTRA_SENSITIVE_VARIABLES = ['password', 'credentials']
  EXTRA_SENSITIVE_POST_PARAMETERS = ['password', 'credentials', 'credit_card_number']

