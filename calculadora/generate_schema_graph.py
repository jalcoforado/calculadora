# generate_schema_graph.py
import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calculadora.settings')
django.setup()

call_command('graph_models', '-a', '-o', 'schema_graph.png')
