import React from 'react'
import { Layout } from '../Home/Layout'

const RegisterScreen = () => {
  return (
    <Layout>
        <div className='form-container'>
            <h2> Registrarse </h2>
            <form >
                <input type="text" placeholder='Nombre' />
                <input type="text" placeholder='Apellidos' />
                <input type="email" placeholder='email' />
                <input type="password" placeholder='password' />
                <input type="submit" className='btn-form' value="Registrarse"/>
                <span>¿Ya estas registrado?</span>

            </form>
        </div>
    </Layout>
  )
}

export default RegisterScreen