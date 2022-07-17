import React from 'react'

import {
    BrowserRouter,
    Routes,
    Route
  } from 'react-router-dom';
import LoginScreen from '../components/Auth/LoginScreen';
import RegisterScreen from '../components/Auth/RegisterScreen';
import CalculatorScreen from '../components/Calculator/CalculatorScreen';
import ElectricityConsumption from '../components/Calculator/ElectricityConsumption';
import FoodConsumption from '../components/Calculator/FoodConsumption';
import LivingPlace from '../components/Calculator/LivingPlace';
import Transportation from '../components/Calculator/Transportation';
import WaterConsumption from '../components/Calculator/WaterConsumption';
import Home from '../components/Home/Home';

const AppRouter = () => {
  return (
    <BrowserRouter>
        <div>
            <Routes>
                <Route path='/' element = {<Home/>}/>
                <Route path='/auth/login' element = {<LoginScreen/>}/>
                <Route path='/auth/register' element = {<RegisterScreen/>}/>
                <Route path='/calculator' element = {<CalculatorScreen/>}/>
                <Route path='/calculator/living-place' element = {<LivingPlace/>}/>
                <Route path='/calculator/electricity' element = {<ElectricityConsumption/>}/>
                <Route path='/calculator/water' element = {<WaterConsumption/>}/>
                <Route path='/calculator/food' element = {<FoodConsumption/>}/>
                <Route path='/calculator/transportation' element = {<Transportation/>}/>
            </Routes>
        </div>
    </BrowserRouter>
  )
}

export default AppRouter