import React, { useState } from 'react'
import { Link } from 'react-router-dom';
import { Layout } from '../Home/Layout'

const AccountScreen = () => {

    const [selected, setSelected] = useState('personal-info');

    const renderContent = () => {
        switch(selected) {
            case 'personal-info':
                return <div className='wrapper-content'>
                    <h4>Nombre</h4>
                    <h4>Apellido</h4>
                    <h4>Edad</h4>
                    <h4>Localidad</h4>
                    <button className='primary-btn'>Editar</button>


                </div>
            case 'publications':
                return <div className='wrapper-content'> 
                        <article> Publicación 1</article>
                        <article> Publicación 1</article>
                        <button className='primary-btn'>Nueva publicación</button>
                     </div>
            default:
                return <div></div>

        }

    }

    return (
        <Layout>
            <div className='profile-containner'>
                <div className='menu'>
                    <img src={require("../../assets/images/user.png")} alt="" />
                    <span>Cambiar foto de perfil</span>

                    <ul className='menu-options'>
                        <li 
                            className={selected === 'personal-info' ? 'option-selected' : ''}
                            onClick = { () => setSelected('personal-info') }
                        >
                            Información Personal
                        </li>
                        <li 
                            className={selected === 'publications' ? 'option-selected' : ''}
                            onClick = { () => setSelected('publications') }
                        >
                            Publicaciones
                        </li>
                        <li > <Link to="/calculator">Calculadora</Link></li>
                    </ul>
                </div>
                {renderContent()}
            </div>

        </Layout>
  )
}

export default AccountScreen