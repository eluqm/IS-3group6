import React from 'react'
import cover from '../../assets/images/cover.png'
import { Layout } from '../Home/Layout'

const Home = () => {
  return (
    <Layout>
      <img src={cover} alt = "main-cover"/>
    </Layout>
  )
}

export default Home