from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import FeatureForm, ClientForm
from .models import Feature, Client


def increase_priority_level(client):
    client_features = Feature.query.filter_by(client=client).\
                      filter_by(client_priority=1)
    if client_features:
        Feature.query.filter_by(client=client).update(
            {'client_priority': Feature.client_priority + 1})


@app.route('/', methods=['GET'])
def index():
    clients = Client.query.all()
    features = Feature.query.all()
    return (render_template('index.html', clients=clients, features=features))


@app.route('/features', methods=['GET', 'POST'])
def feature():
    form = FeatureForm()
    default = [(0, "Choose a client")]
    clients = default + \
        [(client.id, client.name) for client in Client.query.all()]
    form.client.choices = clients
    title = form.title.data
    description = form.description.data
    client = dict(clients).get(form.client.data)
    client_priority = form.client_priority.data
    if client_priority == 1:
        increase_priority_level(client)
    target_date = form.target_date.data
    product_areas = form.product_areas.data
    if form.validate_on_submit():
        feature = Feature(title=title, description=description, client=client,
                          client_priority=client_priority,
                          target_date=target_date, product_areas=product_areas)
        db.session.add(feature)
        db.session.commit()
        flash('feature {} added'.format(form.title.data))
        return redirect(url_for('index'))
    return (render_template('feature.html', form=form))


@app.route('/clients', methods=['GET', 'POST'])
def client():
    form = ClientForm()
    name = form.name.data
    location = form.location.data
    if form.validate_on_submit():
        client = Client(name=name, location=location)
        db.session.add(client)
        db.session.commit()
        flash('Client {} added '.format(form.name.data))
        return redirect(url_for('index'))
    return (render_template('client.html', form=form))


@app.route('/features/<feat>', methods=['GET'])
def get_feature(feat):
    feature = Feature.query.filter_by(id=feat).first()
    return(render_template('details.html', feature=feature))


@app.route('/clients/<id>', methods=['GET'])
def get_client(id):
    client = Client.query.filter_by(id=id).first()
    return(render_template('details.html', client=client))
