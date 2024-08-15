
import { Component } from 'react'

class ClassBaseComponent extends Component {
	state = {
		showText: true,
		changeColor: false,
		count: 0,
		changeCountStyle: false
	}; 

	handleClick = () => {
		this.setState((prevState) => ({
			...prevState,
			showText: !prevState.showText,
			changeColor: !prevState.changeColor
		}))
	}

	handleCount = () => {
		this.setState({
			...this.state,
			count: this.state.count + 1
		})
	}

	componentDidMount(){
		this.setState({
			...this.state,
			showText: !this.state.showText,
			changeColor: !this.state.changeColor
		})
	}
	componentDidUpdate(prevProps, prevState){
		if(prevState && prevState.count !== this.state.count && this.state.count === 10){
			this.setState({
				...this.state,
				changeCountStyle: !this.state.changeCountStyle
			})
		}
	}

	render(){
		const { showText, changeColor, count, changeCountStyle } = this.state;
		return <div>
			{
				showText ? <h3 style={{
					color: changeColor ? 'red': 'black'
				}}>Class Based Component</h3> : null
			}
			<button onClick={this.handleClick}>Toggle Text</button>
			<button onClick={this.handleCount}>Change Color</button>
			<p style={{color: changeCountStyle ? 'red': 'black', fontSize: changeCountStyle ? '30px': '20px'}}>Count {count}</p>
		</div>
	}	
}

export default ClassBaseComponent
