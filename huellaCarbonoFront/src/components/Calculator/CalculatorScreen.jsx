import React from 'react'
import { Layout } from '../Home/Layout'
import { Link } from "react-router-dom";


const CalculatorScreen = () => {
  return (
    <Layout>
        <h2>Calcula tu huella de carbono</h2>
        <div className='options-container'>
            <div className='option-btn'>
                {/* <Link to="/calculator/personal-information"> */}
                    <img src={require("../../assets/images/icons8-documento-96.png")} alt="" />
                {/* </Link> */}
            </div>

            <div className='option-btn'>
                <Link to="/calculator/living-place">
                    <img src={require("../../assets/images/icons8-casa-96.png")} alt="" />
                </Link>
            </div>

            <div className='option-btn'>
                <Link to="/calculator/electricity">
                    <img src={require("../../assets/images/icons8-dentro-de-una-96.png")} alt="" />
                </Link>
            </div>

            <div className='option-btn'>
                <Link to="/calculator/water">
                    <img src={require("../../assets/images/icons8-agua-96.png")} alt="" />
                </Link>
            </div>

            <div className='option-btn'>
                <Link to="/calculator/food">
                    <img src={require("../../assets/images/icons8-comida-96.png")} alt="" />
                </Link>
            </div>

            <div className='option-btn'>
                <Link to="/calculator/transportation">
                    <img src={require("../../assets/images/icons8-bus-station-96.png")} alt="" />
                </Link>
            </div>

        </div>
    </Layout>
  )
}

export default CalculatorScreen