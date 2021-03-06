import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios'; //nuevo
import ProductsList from './components/ProductsList';
import AddProduct from './components/AddProduct';

//nuevo
class App extends Component {

	constructor(){
		super();
		this.state ={
			products: [],
			name: '',
			stock: '',
			price: '',
			trademark: '',
			category: '',
		};
		this.addProduct = this.addProduct.bind(this);
		this.handleChange = this.handleChange.bind(this);
	};

    //nuevo
	componentDidMount() {
		this.getProducts();
	};

	// nuevo
	getProducts() {
		axios.get(`${process.env.REACT_APP_PRODUCTS_SERVICE_URL}/products`)
		.then((res) => { this.setState({ products: res.data.data.products }); }) 
		.catch((err) => { console.log(err); });
	}

	addProduct(event) {
		event.preventDefault();
		const data = {
			name: this.state.name,
			stock: this.state.stock,
			price: this.state.price,
			trademark: this.state.trademark,
			category: this.state.category
		};
		axios.post(`${process.env.REACT_APP_PRODUCTS_SERVICE_URL}/products`,data)
		.then((res) => { 
			this.getProducts();
			this.setState({ 
				name: '', 
				stock: '', 
				price: '', 
				trademark: '', 
				category: ''});
		 })
		.catch((err) => { console.log(err); });
	};

	handleChange(event){
		const obj = {};
		obj[event.target.name] = event.target.value;
		this.setState(obj);
	};

	render(){
		return (
			<section className="section">
			<div className="container">
			<div className="columns">
			<div className="column is-one-third box">
			<br/>
			<h1 className="title is-1">Registro de Productos</h1>
			<hr/><br/>
			<AddProduct
			name={this.state.name} 
			stock={this.state.stock} 
			price={this.state.price} 
			trademark={this.state.trademark} 
			category={this.state.category} 
			addProduct={this.addProduct} 
			handleChange={this.handleChange}
			/>
			</div>
			<div className="column">
			<br/>
			<h1 className="title is-1">Todos los Productos</h1>
			<hr/><br/>
			<ProductsList products={this.state.products}/>
			</div>
			</div>
			</div>
			</section>
		)
	}
}


ReactDOM.render(
	<App />,
	document.getElementById('root')
);
