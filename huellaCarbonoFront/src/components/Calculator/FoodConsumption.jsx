import React from 'react'
import { Link } from 'react-router-dom'
import { Layout } from '../Home/Layout'

const FoodConsumption = () => {
  return (
    <Layout>
        <h3> Consumo de Alimentos </h3>
        <Link to="/calculator">
          <button className='primary-btn'>Regresar</button>
        </Link>
    </Layout>
  )
}

export default FoodConsumption