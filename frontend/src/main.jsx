import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

import { BrowserRouter, Route, Routes } from 'react-router'
import AuthLayout from './components/AuthLayout.jsx'
import Login from './components/Login.jsx'
import Home from './components/Home.jsx'


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route index path="/" element={<App />} />
         <Route path='/login' element={<Login />} />
        <Route element={<AuthLayout/>}>
          <Route path='/home' element={<Home/>} />
        </Route>
      </Routes>
      
    </BrowserRouter>
  </StrictMode>,
)
