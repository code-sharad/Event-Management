import { useEffect, useState } from 'react'

import EventCard from './EventCard'
import VenueIndustry from './VenueCard'

export default function Home(){
  const [event,setEvent] = useState([])
  const [venue,setVenue] = useState([])
  const [selectD,setSelectD] = useState('event')
  useEffect(() => {
    fetch('https://event-management-456128109301.asia-south1.run.app/api/event/events')
      .then(res => res.json())
      .then(data => {
        setEvent(data)
      })

       fetch('https://event-management-456128109301.asia-south1.run.app/api/venue/list')
      .then(res => res.json())
      .then(data => {
        setVenue(data)
      })

  },[selectD,setSelectD])
    return <>
    <div  className='flex gap-12 my-24 mx-24'>
        <span className={`${selectD === 'event'?'underline underline-offset-4 font-bold':'font-light'} cursor-pointer text-xl `} onClick={() => setSelectD('event')}>Event</span>
        <span className={`${selectD === 'venue'?'underline underline-offset-4 font-bold':'font-light'} cursor-pointer text-xl `} onClick={() => setSelectD('venue')}>Venue</span>
       </div>
      {selectD === 'event'?<div className='px-8 flex-wrap'>
        {
          event.map((e,i) => (
            <EventCard  event={e} key={i}/>
            
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