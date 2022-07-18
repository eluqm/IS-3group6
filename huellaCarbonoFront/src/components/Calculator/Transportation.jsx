import React from 'react'
import { Link } from 'react-router-dom'
import { Layout } from '../Home/Layout'

const Transportation = () => {
  return (
    <Layout>
        <h3> Transporte </h3>
        <Link to="/calculator">
          <button className='primary-btn'>Regresar</button>
        </Link>
    </Layout>
  )
}

export default Transportation