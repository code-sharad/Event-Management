import React, { useContext } from 'react';
import { Navigate,Outlet, replace } from 'react-router';
import Header from './Header';
// ...existing code...

// Example auth context or function
const isAuthenticated = () => {
  // Replace with real logic (e.g., check token/store)
  return true;
};

function AuthLayout({ children }) {
  if (!isAuthenticated()) {
    return <Navigate to="/login" replace />;
  }

  return (
    <div>
        <Header/>
      <main >
        {isAuthenticated() ? <Outlet /> : replace('/login')}
        
      </main>
    </div>
  );
}

export default AuthLayout;