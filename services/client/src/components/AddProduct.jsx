import React from 'react';
const AddProduct= (props) => {
    return (
    <form onSubmit={(event) => props.addProduct(event)}>
        <div className="field">
        <div className="control">
        <input
        name="name"
        className="input is-large"
        type="text"
        placeholder="Ingresa el nombre del producto"
        required
        value={props.name}
        onChange={props.handleChange}
        />
        </div>
        </div>
        <div className="field">
        <input
        name="stock"
        className="input is-large"
        type="text"
        placeholder="Ingresa el Stock"
        required
        value={props.stock}
        onChange={props.handleChange}
        />
        </div>
        <div className="field">
        <input
        name="price"
        className="input is-large"
        type="text"
        placeholder="Ingresa el precio"
        required
        value={props.price}
        onChange={props.handleChange}
        />
        </div>
        <div className="field">
        <input
        name="trademark"
        className="input is-large"
        type="text"
        placeholder="Ingresa la marca"
        required
        value={props.trademark}
        onChange={props.handleChange}
        />
        </div>
        <div className="field">
        <input
        name="category"

        className="input is-large"
        type="text"
        placeholder="Ingresa la categoria"
        required
        value={props.category}
        onChange={props.handleChange}
        />
        </div>
        <div className="field">
        <input
        type="submit"
        className="button is-primary is-large is-rounded is-fullwidth"
        value="Registrar"
        />
        </div>
        </form>
        )
    };

export default AddProduct;