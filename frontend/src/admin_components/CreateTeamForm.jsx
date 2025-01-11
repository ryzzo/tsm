import React, { useState, useEffect } from 'react';
import axios from 'axios';

const CreateTeamForm = ({ onTeamCreated }) => {
    const [teamName, setTeamName] = useState('');
    const [coachName, setCoachName] = useState('');
    const [leagueOptions, setLeagueOptions] = useState([]);
    const [selectedLeague, setSelectedLeague] = useState('');

    useEffect(() => {
        const fetchLeagues = async() => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/leagues/')
                setLeagueOptions(response.data);
            } catch (error) {
                console.error('Error fetching leagues:', error);
            }
        };
        fetchLeagues();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();

        const teamData = {
            name: teamName,
            coach: coachName,
            league: selectedLeague,
        };

        try {
            const response = await axios.post('http://127.0.0.1:8000/teams/', teamData);
            onTeamCreated(response.data);
            alert('Team created successfully!');
            setTeamName('');
            setCoachName('');
            setSelectedLeague('');
        } catch (error) {
            console.error('Error creating team:', error);
            alert('Failed to create team.')
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Create Team</h2>
            <label>
                Team Name:
                <input
                    type='text'
                    value={teamName}
                    onChange={(e) => setTeamName(e.target.value)}
                    required
                />
            </label>
            <br />
            <label>
                Coach Name:
                <input
                    type='text'
                    value={coachName}
                    onChange={(e) => setCoachName(e.target.value)}
                />
            </label>
            <br />
            <label>
                League:
                <select
                    value={selectedLeague}
                    onChange={(e) => setSelectedLeague(e.target.value)}
                >
                    <option value="">-- Select League --</option>
                    {leagueOptions.map((league) => ( 
                        <option key={league.id} value={league.id}>
                            {console.log(league)}
                            {league.tier}
                        </option>
                    ))}
                </select>
            </label>
            <br />
            <button type='submit'>Create Team</button>
        </form>
    );
};

export default CreateTeamForm;