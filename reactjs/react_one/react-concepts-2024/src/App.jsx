import './App.css'
import ProductList from './components/products'
// import ClassBaseComponent from './components/class-based-component'
// import FuntionalComponent from './components/functional-component'
const dummyProductData = ['Product 1', 'Product 2', 'Product 3'];
function App() {

  return (
   <div>
	<h1>React js Concepts 2024</h1>
	{/* <ClassBaseComponent /> */}
	{/* <FuntionalComponent /> */}
	<ProductList listProjects={dummyProductData} />
   </div>
  )
}

export default App
