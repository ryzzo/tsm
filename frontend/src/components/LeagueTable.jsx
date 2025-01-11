import React, { useEffect, useState } from 'react';
import { Table } from 'react-bootstrap';

import { fetchTeams } from '../api';

const LeagueTable = () => {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetchTeams()
      .then((response) => setTeams(response.data))
      .catch((error) => console.error('Error fetching league table:', error));
  }, []);

  console.log(teams)

  return (
    <div>
      {console.log(teams)}
      <h2>League Table</h2>
      <Table>
        <thead>
          <tr>
            <th>#</th>
            <th>Team</th>
            <th>PTS</th>
            <th>MP</th>
            <th>W</th>
            <th>L</th>
            <th>D</th>
            <th>GF</th>
            <th>GA</th>
            <th>GD</th>
          </tr>
        </thead>
        <tbody>
          {teams.map((team, index) => (
            <tr key={team.id}>
              <td>{index + 1}</td>
              <td>{team.name}</td>
              <td>{team.points}</td>
              <td>{team.matches_played}</td>
              <td>{team.wins}</td>
              <td>{team.losses}</td>
              <td>{team.draws}</td>
              <td>{team.goals_scored}</td>
              <td>{team.goals_conceded}</td>
              <td>{team.goal_difference}</td>

            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default LeagueTable;
