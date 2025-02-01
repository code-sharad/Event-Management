import React from 'react';

// interface Venue {
//   id: number;
//   name: string;
//   address: string;
//   capacity: number;
// }

// interface VenueIndustryProps {
//   venues: Venue[];
//   loading?: boolean;
//   error?: string | null;
//   currentPage?: number;
//   totalPages?: number;
//   onPageChange?: (page: number) => void;
// }

function VenueIndustry({veneus}){
//   if (loading) {
//     return (
//       <div className="animate-pulse space-y-4">
//         {[...Array(3)].map((_, i) => (
//           <div key={i} className="h-32 bg-gray-200 rounded-lg"></div>
//         ))}
//       </div>
//     );
//   }

//   if (error) {
//     return (
//       <div className="text-center py-8 text-red-500">
//         <p>Error loading venues: {error}</p>
//         <button
//           onClick={() => window.location.reload()}
//           className="mt-4 px-4 py-2 bg-red-100 text-red-600 rounded hover:bg-red-200"
//         >
//           Retry
//         </button>
//       </div>
//     );
//   }
  console.log('veneus',veneus)
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold text-gray-800 mb-8">Venue</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {veneus.map((venue) => (
          <article 
            key={venue.id}
            className="bg-white rounded-xl shadow-md overflow-hidden hover:shadow-lg transition-shadow"
          >
            <div className="p-6">
              <h2 className="text-xl font-semibold text-gray-800 mb-2">
                {venue.name}
              </h2>
              <p className="text-gray-600 mb-4">
                <svg
                  className="w-5 h-5 inline-block mr-2 text-blue-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                  />
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                </svg>
                {venue.address}
              </p>
              <div className="flex items-center text-gray-700">
                <svg
                  className="w-5 h-5 inline-block mr-2 text-green-500"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                  />
                </svg>
                <span className="font-medium">
                  Capacity: {venue.capacity.toLocaleString()}
                </span>
              </div>
            </div>
          </article>
        ))}
      </div>

      {/* {totalPages > 1 && (
        <div className="mt-8 flex justify-center space-x-2">
          <button
            onClick={() => onPageChange?.(currentPage - 1)}
            disabled={currentPage === 1}
            className="px-4 py-2 bg-gray-100 text-gray-700 rounded disabled:opacity-50 hover:bg-gray-200"
          >
            Previous
          </button>
          <span className="px-4 py-2 text-gray-700">
            Page {currentPage} of {totalPages}
          </span>
          <button
            onClick={() => onPageChange?.(currentPage + 1)}
            disabled={currentPage === totalPages}
            className="px-4 py-2 bg-gray-100 text-gray-700 rounded disabled:opacity-50 hover:bg-gray-200"
          >
            Next
          </button>
        </div>
      )} */}
    </div>
  );
}


export default VenueIndustry;