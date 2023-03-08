from django import template
from django.contrib.auth.models import User
from django.db.models import Q
from frontend.models import *

register = template.Library()