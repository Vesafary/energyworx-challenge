#!/bin/bash
set -e

python code/manage.py test tests.views.creation --noinput -v 2
python code/manage.py test tests.views.resolve --noinput -v 2
python code/manage.py test tests.views.stats --noinput -v 2
