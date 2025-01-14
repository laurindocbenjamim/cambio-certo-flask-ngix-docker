import os
import uuid
import secrets
from flask import Flask,Blueprint,make_response, render_template, request, redirect, url_for, flash, jsonify
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
#from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

