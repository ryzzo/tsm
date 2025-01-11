import React, { useEffect, useState } from 'react';
import { fetchTeams, updateTeam } from '../api';

const TeamManagement = () => {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    fetchTeams()
      .then((response) => setTeams(response.data))
      .catch((error) => console.error('Error fetching teams:', error));
  }, []);

  const handleUpdateTeam = (id) => {
    const name = prompt('Enter new team name:');
    if (name) {
      updateTeam(id, { name })
        .then(() => alert('Team updated!'))
        .catch((error) => console.error('Error updating team:', error));
    }
  };

  return (
    <div>
      <h2>Team Management</h2>
      <ul>
        {teams.map((team) => (
          <li key={team.id}>
            {team.name} <button onClick={() => handleUpdateTeam(team.id)}>Edit</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TeamManagement;
