import React from 'react';


const ProductsList = (props) => {
  return (
    <div>
      <table className="table is-narrow is-striped is-fullwidth is-hoverable">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Stock</th>
          <th>Marca</th>
          <th>Categoria</th>
        </tr>
      </thead>
      <tbody>
      {
        props.products.map((product) => {
          return (
            <tr key={product.id}>
            <td>{ product.name }</td>
            <td>{ product.price }</td>
            <td>{ product.stock }</td>
            <td>{ product.trademark }</td>
            <td>{ product.category }</td>
            </tr>
          )
        })
      }
      </tbody>
      </table>
    </div>
  )
};


export default ProductsList;