from __future__ import unicode_literals
import frappe

def get_context(context):
    context.no_cache = 1
    context.show_sidebar = True
    context.title = "Employee Job Matching"
    context.content = "Your custom content goes here..."
