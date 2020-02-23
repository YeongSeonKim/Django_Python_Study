from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib import messages
from accounts.models import User