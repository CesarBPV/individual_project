import React from 'react';
const AddProduct= (props) => {
    return (
    <form onSubmit={(event) => props.addProduct(event)}>
        <div className="field">
        <input
        name="name"
        className="input is-large"
        type="text"
        placeholder="Enter a name"
        required
        value={props.name}
        onChange={props.handleChange}
        />
        </div>
        <div className="field">
        <input
        name="stock"
        className="input is-large"
        type="text"
        placeholder="Enter stock"
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
        placeholder="Enter price"
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
        placeholder="Enter trademark"
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
        placeholder="Enter category"
        required
        value={props.category}
        onChange={props.handleChange}
        />
        </div>
        <input
        type="submit"
        className="button is-primary is-large is-fullwidth"
        value="Submit"
        />
        </form>
        )
    };

export default AddProduct;