import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import ParentComponent from './ParentComponent'
import './index.css'
// import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
   <ParentComponent name=""/>
   {/* <App></App> */}
  </StrictMode>,
)
