import React from 'react';
import { HomeIcon, CalendarIcon, UserCircleIcon} from '@heroicons/react/24/outline';

function Header() {
  return (
    <header className="sticky top-0 z-50 backdrop-blur-xl bg-gradient-to-r from-slate-900/80 via-purple-900/80 to-slate-900/80 border-b border-white/10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <h2 className="text-2xl font-bold bg-gradient-to-r from-purple-400 via-pink-400 to-purple-400 bg-clip-text text-transparent
            hover:from-purple-300 hover:to-pink-300 transition-all duration-300">
            Event Management
          </h2>
          
          <nav className="flex items-center gap-2">
            <a
              href="/"
              className="flex items-center gap-2 px-4 py-2 rounded-full text-white/70 
              hover:text-white hover:bg-white/10 transition-all duration-200 
              border border-transparent hover:border-white/20"
            >
              <HomeIcon className="w-4 h-4" />
              <span className="text-sm font-medium">Home</span>
            </a>
            <a
              href="/events"
              className="flex items-center gap-2 px-4 py-2 rounded-full text-white/70 
              hover:text-white hover:bg-white/10 transition-all duration-200
              border border-transparent hover:border-white/20"
            >
              <CalendarIcon className="w-4 h-4" />
              <span className="text-sm font-medium">Events</span>
            </a>
            <a
              href="/profile"
              className="flex items-center gap-2 px-4 py-2 rounded-full text-white/70 
              hover:text-white hover:bg-white/10 transition-all duration-200
              border border-transparent hover:border-white/20"
            >
              <UserCircleIcon className="w-4 h-4" />
              <span className="text-sm font-medium">Profile</span>
            </a>
          </nav>
        </div>
      </div>
    </header>
  );
}

export default Header;