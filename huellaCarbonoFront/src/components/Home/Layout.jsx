import React from 'react'
import Header from './Header'

export const Layout = ({children}) => {
  return (
    <div className='layout'>
        <Header/>
        <main>
            {children}
          {/* <img src={cover} alt = "main-cover"/> */}
        </main>
    </div>
  )
}
