# services/products/project/tests/test_products.py


import json
import unittest

from project.tests.base import BaseTestCase

from project import db
from project.api.models import Product


def add_product(name, stock, price, trademark, category):
    product = Product(
        name=name,
        stock=stock,
        price=price,
        trademark=trademark,
        category=category
    )
    db.session.add(product)
    db.session.commit()
    return product


class TestProductService(BaseTestCase):
    """Pruebas para el Servicio de Productos """

    def test_products(self):
        """comprobado que la ruta /ping funcione correctamente."""
        response = self.client.get('/products/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('Conectado exitosamente!', data['mensaje'])
        self.assertIn('satisfactorio', data['estado'])

    def test_add_product(self):
        """ Asegurando que se pueda agregar
         un nuevo producto a la base de datos"""
        with self.client:
            response = self.client.post(
                '/products',
                data=json.dumps({
                    'name': 'Oreo',
                    'stock': 20,
                    'price': 0.7,
                    'trademark': 'Nabisco',
                    'category': 'Galletas'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn(
                'Oreo fue agregado!!!',
                data['mensaje'])
            self.assertIn('satisfactorio', data['estado'])

    def test_add_product_invalid_json(self):
        """Asegurando de que se lance un error
         cuando el objeto JSON esta vacío."""
        with self.client:
            response = self.client.post(
                '/products',
                data=json.dumps({}),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Carga inválida.', data['mensaje'])
            self.assertIn('falló', data['estado'])

    def test_add_product_invalid_json_keys(self):
        """Asegurando de que se produce un error si el
         objeto JSON no tiene una clave de nombre de
          producto."""
        with self.client:
            response = self.client.post(
                '/products',
                data=json.dumps({'name': 'Oreo'}),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Carga inválida.', data['mensaje'])
            self.assertIn('falló', data['estado'])

    def test_add_product_duplicate_name(self):
        """Asegurando que se produce un error si
         el nombre ya existe."""
        with self.client:
            self.client.post(
                '/products',
                data=json.dumps({
                    'name': 'Oreo',
                    'stock': 20,
                    'price': 0.7,
                    'trademark': 'Nabisco',
                    'category': 'Galletas'
                }),
                content_type='application/json',
            )
            response = self.client.post(
                '/products',
                data=json.dumps({
                    'name': 'Oreo',
                    'stock': 20,
                    'price': 0.7,
                    'trademark': 'Nabisco',
                    'category': 'Galletas'
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Lo siento, ese nombre ya existe.', data['mensaje'])
            self.assertIn('falló', data['estado'])

    def test_single_product(self):
        """Asegurando que el producto único se comporte
         correctamente."""
        product = add_product('Oreo', 20, 0.7, 'Nabisco', 'Galletas')
        with self.client:
            response = self.client.get(f'/products/{product.id}')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertIn('Oreo', data['data']['name'])
            self.assertEqual(20, data['data']['stock'])
            self.assertEqual(0.7, data['data']['price'])
            self.assertIn(
                'Nabisco',
                data['data']['trademark'])
            self.assertIn(
                'Galletas',
                data['data']['category']
                )
            self.assertIn('satisfactorio', data['estado'])

    def test_single_product_no_id(self):
        """Asegúrese de que se arroje un error si
         no se proporciona una identificación."""
        with self.client:
            response = self.client.get('/products/blah')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn(
                'El producto no existe',
                data['mensaje']
                )
            self.assertIn('falló', data['estado'])

    def test_single_product_incorrect_id(self):
        """Asegurando de que se arroje un error si
         la identificación no existe."""
        with self.client:
            response = self.client.get('/products/999')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 404)
            self.assertIn('El producto no existe', data['mensaje'])
            self.assertIn('falló', data['estado'])

    def test_all_products(self):
        """Asegurando obtener todos los productos
         correctamente."""
        add_product('Oreo', 20, 0.7, 'Nabisco', 'Galletas')
        add_product('Picaras Fresa', 25, 0.8, 'Costa', 'Galletas')
        with self.client:
            response = self.client.get('/products')
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['products']), 2)
            self.assertIn(
                'Oreo',
                data['data']['products'][0]['name']
                )
            self.assertEqual(
                20,
                data['data']['products'][0]['stock']
                )
            self.assertEqual(
                0.7,
                data['data']['products'][0]['price']
                )
            self.assertIn(
                'Nabisco',
                data['data']['products'][0]['trademark']
                )
            self.assertIn(
                'Galletas',
                data['data']['products'][0]['category']
                )
            self.assertIn(
                'Picaras Fresa',
                data['data']['products'][1]['name']
                )
            self.assertEqual(
                25,
                data['data']['products'][1]['stock']
                )
            self.assertEqual(
                0.8,
                data['data']['products'][1]['price']
                )
            self.assertIn(
                'Costa',
                data['data']['products'][1]['trademark']
                )
            self.assertIn(
                'Galletas',
                data['data']['products'][1]['category']
                )

    def test_main_no_products(self):
        """Asegura que la ruta principal actua
         correctamente cuando no hay productos en
          la base de datos"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'All Products', response.data)
        self.assertIn(
            b'<p>No hay productos!</p>',
            response.data
            )

    def test_main_with_products(self):
        """Asegura que la ruta principal actua
         correctamente cuando hay productos en la
          base de datos"""
        add_product('Ritz', 15, 0.6, 'Nabisco', 'Galletas')
        add_product('Tentacion', 30, 0.5, 'Victoria', 'Galletas')
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All Products', response.data)
            self.assertNotIn(
                b'<p>No hay productos!</p>',
                response.data
                )
            self.assertIn(b'Ritz', response.data)
            self.assertIn(b'Tentacion', response.data)

    def test_main_add_product(self):
        """Asegura que un nuevo producto puede ser
         agregado a la db"""
        with self.client:
            response = self.client.post(
                '/',
                data=dict(
                    name='Coca Cola personal plastico',
                    stock=35,
                    price=2.5,
                    trademark='The Coca Cola Company',
                    category='Gaseosas'
                    ),
                follow_redirects=True
            )
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'All Products', response.data)
            self.assertNotIn(
                b'<p>No hay productos!</p>',
                response.data
                )
            self.assertIn(b'Coca Cola personal plastico', response.data)


if __name__ == '__main__':
    unittest.main()
