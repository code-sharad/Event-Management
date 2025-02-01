import React, { useState } from 'react';
import { FaEnvelope, FaLock, FaGoogle } from 'react-icons/fa';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    const user = fetch('http://localhost:8000/api/user/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password}),
        }
    )
    console.log(user)
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 p-6">
      <div className="w-full max-w-md p-8 backdrop-blur-xl bg-white/10 rounded-2xl shadow-2xl">
        <h2 className="text-3xl font-bold text-center mb-8 text-white">Welcome Back</h2>
        
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="relative">
            <FaEnvelope className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
            <input
              type="text"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="w-full pl-10 pr-4 py-3 bg-white/20 border border-white/30 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 text-white placeholder-gray-300"
            />
          </div>

          <div className="relative">
            <FaLock className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400" />
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full pl-10 pr-4 py-3 bg-white/20 border border-white/30 rounded-lg focus:outline-none focus:ring-2 focus:ring-purple-500 text-white placeholder-gray-300"
            />
          </div>

          <div className="flex items-center justify-between text-sm">
            <label className="flex items-center space-x-2 text-white/80">
              <input
                type="checkbox"
                checked={rememberMe}
                onChange={(e) => setRememberMe(e.target.checked)}
                className="w-4 h-4 accent-purple-500"
              />
              <span>Remember me</span>
            </label>
            <a href="#forgot" className="text-purple-300 hover:text-purple-200">
              Forgot Password?
            </a>
          </div>

          <button
            type="submit"
            className="w-full py-3 bg-gradient-to-r from-purple-500 to-purple-600 text-white rounded-lg font-medium 
            transform transition-all duration-200 hover:from-purple-600 hover:to-purple-700 
            focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 focus:outline-none"
          >
            Sign In
          </button>

          {/* <div className="flex items-center gap-4 mt-8">
            <hr className="flex-1 border-white/20" />
            <span className="text-white/60 text-sm">or</span>
            <hr className="flex-1 border-white/20" />
          </div>

          <button
            type="button"
            className="w-full flex items-center justify-center gap-2 py-3 bg-white/10 text-white rounded-lg
            border border-white/30 hover:bg-white/20 transition-colors duration-200"
          >
            <FaGoogle />
            <span>Continue with Google</span>
          </button>

          <p className="text-center text-white/60 text-sm">
            Don't have an account?{' '}
            <a href="#signup" className="text-purple-300 hover:text-purple-200">
              Sign up
            </a>
          </p> */}
        </form>
      </div>
    </div>
  );
}

export default Login;