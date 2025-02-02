import { format, parseISO, formatDistanceStrict } from 'date-fns';
import { HomeIcon, CalendarIcon, UsersIcon, ClockIcon} from '@heroicons/react/24/outline';

import { useMemo, useState } from 'react';

const getStatusStyle = (status) => {
  switch (status.toLowerCase()) {
    case 'published':
      return 'bg-gradient-to-r from-emerald-500/20 to-green-500/20 text-emerald-300 border-emerald-500/30';
    case 'draft':
      return 'bg-gradient-to-r from-gray-500/20 to-slate-500/20 text-gray-300 border-gray-500/30';
    case 'archived':
      return 'bg-gradient-to-r from-amber-500/20 to-yellow-500/20 text-amber-300 border-amber-500/30';
    default:
      return 'bg-gradient-to-r from-blue-500/20 to-indigo-500/20 text-blue-300 border-blue-500/30';
  }
};

const EventCard = ({ event }) => {
  const [book, setBook] = useState('Book Ticket');
  
  const formattedDates = useMemo(() => ({
    startDate: format(parseISO(event.start_date), 'MMM dd, yyyy h:mm a'),
    endDate: format(parseISO(event.end_date), 'MMM dd, yyyy h:mm a'),
    duration: formatDistanceStrict(parseISO(event.start_date), parseISO(event.end_date)),
  }), [event.start_date, event.end_date]);

  return (
    <article className="backdrop-blur-xl my-8 max-w-[400px] bg-white/10 rounded-2xl overflow-hidden 
    shadow-[0_8px_30px_rgb(0,0,0,0.12)] border border-white/20 hover:shadow-purple-500/10 
    transition-all duration-300 transform hover:-translate-y-1">
      <div className="p-4 sm:p-8 bg-gradient-to-br from-slate-900/80 via-purple-900/60 to-slate-900/80">
        <div className="flex flex-col sm:flex-row sm:justify-between sm:items-start gap-4 mb-6">
          <h3 className="text-xl sm:text-2xl font-bold text-white drop-shadow-lg">
            {event.title}
          </h3>
          <span className={`px-4 py-1.5 text-sm font-semibold rounded-full border-2 
          backdrop-blur-sm ${getStatusStyle(event.status)} w-fit`}>
            {event.status}
          </span>
        </div>

        <p className="text-white/90 text-sm sm:text-base mb-6 sm:mb-8 leading-relaxed drop-shadow">
          {event.description}
        </p>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 sm:gap-4 mb-6 sm:mb-8">
          <div className="flex items-center space-x-3 bg-white/10 rounded-xl p-4 backdrop-blur-sm">
            <CalendarIcon className="h-5 w-5 text-white" />
            <time className="text-white text-sm font-medium">{formattedDates.startDate}</time>
          </div>
          
          <div className="flex items-center space-x-3 bg-white/10 rounded-xl p-4 backdrop-blur-sm">
            <ClockIcon className="h-5 w-5 text-white" />
            <time className="text-white text-sm font-medium">{formattedDates.endDate}</time>
          </div>

          <div className="flex items-center space-x-3 bg-white/10 rounded-xl p-4 backdrop-blur-sm">
            {/* <LocationMarkerIcon className="h-5 w-5 text-white" /> */}
            <span className="text-white text-sm font-medium">{event.location}</span>
          </div>
        </div>

        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between 
        gap-4 pt-6 border-t border-white/20">
          <div>
            <span className="text-white/80 text-sm font-medium">Price</span>
            <p className="text-2xl sm:text-3xl font-bold text-white drop-shadow-lg">₹{event.price} 400</p>
          </div>
          <button
            onClick={() => setBook('Processing...')}
            className="w-full sm:w-auto px-6 py-2.5 bg-white text-slate-900 rounded-xl font-semibold 
            hover:bg-purple-400 hover:text-white transition-all duration-200 
            shadow-lg hover:shadow-purple-500/25"
          >
            {book}
          </button>
        </div>
      </div>
    </article>

  );
};

export default EventCard;