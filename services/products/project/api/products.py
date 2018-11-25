# services/products/project/api/products.py


from flask import Blueprint, jsonify, request, render_template
from project.api.models import Product
from project import db
from sqlalchemy import exc


products_blueprint = Blueprint(
    'products', __name__, template_folder='./templates')


@products_blueprint.route('/products/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'estado': 'satisfactorio',
        'mensaje': 'Conectado exitosamente!'
    })


@products_blueprint.route('/products', methods=['POST'])
def add_product():
    post_data = request.get_json()
    response_object = {
        'estado': 'falló',
        'mensaje': 'Carga inválida.'
    }
    if not post_data:
        return jsonify(response_object), 400
    name = post_data.get('name')
    stock = post_data.get('stock')
    price = post_data.get('price')
    trademark = post_data.get('trademark')
    category = post_data.get('category')
    try:
        product = Product.query.filter_by(name=name).first()
        if not product:
            db.session.add(Product(
                name=name,
                stock=stock,
                price=price,
                trademark=trademark,
                category=category,
                ))
            db.session.commit()
            response_object['estado'] = 'satisfactorio'
            response_object['mensaje'] = f'{name} fue agregado!!!'
            return jsonify(response_object), 201
        else:
            response_object['estado'] = 'falló'
            response_object['mensaje'] = 'Lo siento, ese nombre ya existe.'
            return jsonify(response_object), 400
    except exc.IntegrityError as e:
        db.session.rollback()
        return jsonify(response_object), 400


@products_blueprint.route('/products/<product_id>', methods=['GET'])
def get_single_product(product_id):
    """Obteniendo detalles del producto único"""
    response_object = {
        'estado': 'falló',
        'mensaje': 'El producto no existe'
    }
    try:
        product = Product.query.filter_by(id=int(product_id)).first()
        if not product:
            return jsonify(response_object), 404
        else:
            response_object = {
                'estado': 'satisfactorio',
                'data': {
                    'id': product.id,
                    'name': product.name,
                    'stock': product.stock,
                    'price': product.price,
                    'trademark': product.trademark,
                    'category': product.category,
                    'active': product.active
                    }
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


@products_blueprint.route('/products', methods=['GET'])
def get_all_products():
    """Obteniendo todos los productos"""
    response_object = {
        'estado': 'satisfactorio',
        'data': {
            'products': [product.to_json() for product in Product.query.all()]
        }
    }
    return jsonify(response_object), 200


@products_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        stock = int(request.form['stock'])
        price = float(request.form['price'])
        trademark = request.form['trademark']
        category = request.form['category']
        db.session.add(Product(
            name=name,
            stock=stock,
            price=price,
            trademark=trademark,
            category=category))
        db.session.commit()
    products = Product.query.all()
    return render_template('index.html', products=products)
