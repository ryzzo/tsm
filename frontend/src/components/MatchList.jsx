import React, { useEffect, useState } from 'react';
import { Card, ListGroup, Row, Col, Container } from 'react-bootstrap';
import MatchCard from './MatchCard';

import { fetchMatches, matchByDates } from '../api';

const MatchList = () => {
  const [matches, setMatches] = useState([]);

  useEffect(() => {
    matchByDates()
      .then((response) => setMatches(response.data))
      .catch((error) => console.error('Error fetching matches:', error));
  }
  , []);

  // Function to format the time
  const formatTime = (timeString) => {
    // Extract hours and miniutes
    const [hours, minutes] = timeString.split(":").map(Number);
    const period = hours <= 12 ? "AM" : "PM";
    
    // convert hours from 24-hour format to 12-hour format
    const formattedHours = hours % 12 || 12; // 12-hour format
    const formattedMinutes = minutes < 10 ? `0${minutes}`:minutes;

    return `${formattedHours}:${formattedMinutes} ${period}`;
  };


  return (
    <Container>
      {Object.keys(matches).map((date) => (
        <div key={date} className='date-block'>
          <h2>{date}</h2>
          <div className='match-cards-container'>
            {/* Sort matches by time before rendering */}
            {matches[date]
              .sort((a, b) => {
                const timeA = new Date(`1970-01-01T${a.date.split("T")[1]}`);
                const timeB = new Date(`1970-01-01T${b.date.split("T")[1]}`);
                return timeA - timeB;
              })
              .map((match) => {
              //Extract date and time from the datetime field
              const [mactchDate, matchTime] = match.date.split("T");
              //Format the time without seconds
              const formattedTime = formatTime(matchTime)
              return (
                <MatchCard
                key={match.id}
                home_team={match.home_team_name}
                home_score={match.home_score}
                away_team={match.away_team_name}
                away_score={match.away_score}
                time = {formattedTime}
              />
              )
              }
            )}
          </div>
        </div>
      ))}
    </Container>
  );
};

export default MatchList;
