from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from form import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    '''home page, show the pets'''
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    '''display and submit the form for adding a pet'''
    form = AddPetForm()
    if form.validate_on_submit():
        try:
            name = form.name.data
            species = form.species.data
            photo_url = form.photo_url.data
            age = form.age.data
            notes = form.notes.data
            pet = Pet(name = name.capitalize(), species = species, photo_url = photo_url, age = age, notes = notes)
            db.session.add(pet)
            db.session.commit()
            flash('Added pet!', 'success')
            return redirect('/')
        except:
            db.session.rollback()
            flash('Error processing form!', 'error')
            return redirect('/')
    else:
        return render_template('add_pet.html', form = form)


@app.route('/<int:pet_id>', methods = ['GET', 'POST'])
def edit_pet(pet_id):
    '''show info page and allow user to edit pet'''
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        try:
            pet.photo_url = form.photo_url.data
            pet.notes = form.notes.data
            pet.available = form.available.data
           
            db.session.commit()
            flash('Edited pet!', 'success')
            return redirect('/')
        except:
            db.session.rollback()
            flash('Error editing pet!', 'error')
            return redirect('/')

    else:
        return render_template('show_edit.html', form = form, pet = pet)
