import React from 'react'
import { Layout } from '../Home/Layout'

const LoginScreen = () => {
  return (
    <Layout>
        <div className='form-container'>
            <h2> Iniciar Sesión </h2>
            <form >
                <input type="email" placeholder='email' />
                <input type="password" placeholder='password' />
                <input type="submit" className='btn-form' value="Login"/>

                <span>¿Olvidaste tu contraseña?</span>
            </form>
        </div>
    </Layout>
  )
}

export default LoginScreen