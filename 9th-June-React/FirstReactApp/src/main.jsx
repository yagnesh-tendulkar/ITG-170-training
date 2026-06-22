import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import MyComponent from './MyComponent.jsx'
import ComponentA from './ComponentA.jsx'
import ComponentB from './ComponentB.jsx'

createRoot(document.getElementById('root')).render(<App/>)
