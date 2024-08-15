import { useEffect, useState } from "react";
import ProductItem from "./components/product-item";
import "./style.css"
const initialState = false;
function ProductList({listProjects}) {
	const [flag, setFlag] = useState(initialState);
	const [count, setCount] = useState(0);
	const [changeCountStyle, setChangeCountStyle] = useState(false);

	// function renderTextBlock(getFlag){
	// 	return getFlag ? <h4>List of projects</h4> : 
	// 	<h4>List of projects with no data</h4>;
	// }
	function hangleToggleText(){
		setFlag(!flag)
	}
	const handleIncreaseCount = () =>{
		setCount(count + 1);
	}
	useEffect(() => {
		setFlag(!flag);
	}, []);

	useEffect(() =>{
		if (count === 10)
			setChangeCountStyle(true);
	}, [count]);
	return <div>
		<h3 className="title">Ecommerce Projects</h3>
		<div>
			<button style={{color: changeCountStyle ? 
				'white': 'black', backgroundColor:
				changeCountStyle ? 'black': 'white'}} onClick={handleIncreaseCount}>Increase Count</button>
			<p style={{fontSize: changeCountStyle ? '30px': '18px'}}>count {count}</p>
		</div>
		<button onClick={hangleToggleText}>Toggle Text</button>
		{/* {renderTextBlock(flag)} */}
		{flag ? <h4>List of projects</h4> :
		<h4>List of projects with no data</h4>}
		<ul>
			{
				listProjects.map((product, index) => (
				<ProductItem singleItemProduct={product} key={index} />
			))
			}
		</ul>
	</div>
}

export default ProductList;
