import styles from './product-item.module.css'

function ButtonComponent(){
	return	<button className={styles.buttonStyle}>Click</button>
}

function ProductItem({singleItemProduct, key}) {
	
	return <div 
	style={{padding: "20px", border: "1px solid black", marginBottom: "10px"}}
	key={key}>
		<div className={styles.productTitle}>{singleItemProduct}</div>
		<ButtonComponent/>
	</div>
}

export default ProductItem;
