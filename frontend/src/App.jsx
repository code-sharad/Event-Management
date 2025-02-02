import { Link } from 'react-router'
import './App.css'

function App() {
  return (
    <div className="min-h-screen bg-[#0F172A] flex items-center justify-center p-4">
      <div className="backdrop-blur-lg bg-white/10 rounded-xl p-4 sm:p-8 shadow-2xl w-full ">
        <div className="flex flex-col items-center justify-center space-y-6 sm:space-y-8">
          <h1 className="text-4xl sm:text-5xl md:ytext-6xl font-bold text-center text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-600">
            Event Management
          </h1>
          <p className="text-lg sm:text-xl text-gray-300 text-center max-w-2xl px-2">
              Transform your event planning experience with our intuitive platform
          </p>
          <Link
            to="/home"
            className="px-6 sm:px-8 py-2.5 sm:py-3 bg-gradient-to-r from-purple-500 to-pink-500 
                     rounded-lg text-white font-semibold transition-all duration-300 
                     hover:opacity-90 hover:scale-105 shadow-lg shadow-purple-500/30
                     w-full sm:w-auto text-center"
          >
            Click Me
          </Link>
        </div>
      </div>
    </div>
  )
}

export default App
