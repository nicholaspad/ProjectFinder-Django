from os import getenv

from .base import *

if getenv("IS_PROD", "False").lower() in ("true", "1", "t"):
    from .prod import *
else:
    from .dev import *
