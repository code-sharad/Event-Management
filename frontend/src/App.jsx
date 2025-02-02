
import { Link } from 'react-router'
import './App.css'


function App() {
  
  return (
    <>
    <div>
      <h1 className='text-4xl font-thin font-mono my-24'>Event Management</h1>
      
      <Link to={'/home'}>Dashboard</Link>
    </div>
    </>
  )
}

export default App
