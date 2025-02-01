import { useEffect, useState } from 'react'

import EventCard from './EventCard'
import VenueIndustry from './VenueCard'

export default function Home(){
  const [event,setEvent] = useState([])
  const [venue,setVenue] = useState([])
  const [selectD,setSelectD] = useState('')
  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/event/events')
      .then(res => res.json())
      .then(data => {
        setEvent(data)
      })

       fetch('http://127.0.0.1:8000/api/venue/list')
      .then(res => res.json())
      .then(data => {
        setVenue(data)
      })

  },[selectD,setSelectD])
    return <>
    <div  className='flex gap-12 my-24'>
        <span className='underline cursor-pointer text-xl font-semibold' onClick={() => setSelectD('event')}>event</span>
        <span className='underline cursor-pointer text-xl font-semibold' onClick={() => setSelectD('venue')}>venue</span>
       </div>
      {selectD === 'event'?<div className='flex gap-4 flex-wrap '>
        {
          event.map((e,i) => (
            <EventCard event={e} key={i}/>
            
          ))
        }
      </div>:''}
      {
        selectD == 'venue'? <div>
            
            <VenueIndustry veneus={venue} />
        </div>:''
      }
      </>
}