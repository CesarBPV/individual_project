import React from 'react';
import { shallow } from 'enzyme';
import renderer from 'react-test-renderer';
 
import ProductsList from '../ProductsList';
 
const products = [
  {
    'active': true,
    'stock': 20,
    'price': 0.7,
    'trademark': 'Nabisco',
    'category': 'Galletas',
    'id': 1,
    'name': 'Oreo'
  },
  {
    'active': true,
    'stock': 25,
    'price': 0.8,
    'trademark': 'Costa',
    'category': 'Galletas',
    'id': 2,
    'name': 'Picaras Fresa'
  }
];
 
test('ProductsList renders properly', () => {
  const wrapper = shallow(<ProductsList products={products}/>);
  const element = wrapper.find('h4');
  expect(element.length).toBe(2);
  expect(element.get(0).props.children).toBe('Oreo');
});

test('ProductsList renders a snapshot properly', () => {
  const tree = renderer.create(<ProductsList products={products}/>).toJSON();
  expect(tree).toMatchSnapshot();
});
