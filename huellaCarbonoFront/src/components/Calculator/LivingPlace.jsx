import React from 'react'
import { Link } from 'react-router-dom'
import { Layout } from '../Home/Layout'

const LivingPlace = () => {
  return (
    <Layout>
        <h3> Vivienda </h3>
        <Link to="/calculator">
          <button>Regresar</button>
        </Link>
    </Layout>
  )
}

export default LivingPlace