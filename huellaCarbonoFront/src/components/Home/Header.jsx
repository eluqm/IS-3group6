import React from 'react';
import { Link } from "react-router-dom";
import logo from '../../assets/images/logo.png'

const Header = () => {
  return (
    <header>
        <div className="logo">
          <Link to="/">
            <img src={logo} alt="logo"/>
          </Link>
        </div>

        <nav>
            <Link to="/auth/login"><span className='link'>Iniciar Sesión</span></Link>
            <Link to="/auth/register"><span className='link'>Registrarse</span></Link>
            <Link to="/calculator"><span className='link'>Calculadora</span></Link>
        </nav>
    </header>
  )
}

export default Header