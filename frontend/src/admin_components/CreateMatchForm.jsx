import React, { useEffect, useState } from "react";
import axios from "axios";

const CreateMatchForm = ({ onMatchCreated }) => {
    const [homeTeam, setHomeTeam] = useState('');
    const [awayTeam, setAwayTeam] = useState('');
    const [teams, setTeams] = useState([]);

    // fetch available teams on component mount
    useEffect(() => {
        const fetchTeams = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/teams/');
                setTeams(response.data);
            } catch (error) {
                console.error('Error fetching teams:', error);
                alert('Failed to load teams.');
            }
        };

        fetchTeams();
    }, []);
          
    const handleSubmit = async (e) => {
        e.preventDefault();

        const matchData = {
            home_team: homeTeam,
            away_team: awayTeam,
        };

        try {
            const response = await axios.post('http://127.0.0.1:8000/matches/', matchData);
            onMatchCreated(response.data);
            alert('Match created successfully!');
            setHomeTeam('');
            setAwayTeam('');
        } catch (error) {
            console.error('Error creating match:', error);
            alert('Failed to create match.');
        }
    };

    console.log(teams)

    return (
        <form onSubmit={handleSubmit}>
            <h2>Create Match</h2>
            <label>
                Home Team:
                <select
                    value={homeTeam}
                    onChange={(e) => setHomeTeam(e.target.value)}
                    required
                >
                    <option value="">Select Home Team</option>
                    {teams.map((team) => (
                        <option key={team.id} value={team.id}>
                            {team.name}
                        </option>
                    ))}
                </select>
            </label>
            <br />
            <label>
                Away Team:
                <select
                    value={awayTeam}
                    onChange={(e) => setAwayTeam(e.target.value)}
                    required
                >
                    <option value="">Select Away Team</option>
                    {teams.map((team) => (
                        <option key={team.id} value={team.id}>
                            {team.name}
                        </option>
                    ))}
                </select>
            </label>
            <br />

            <button type="submit">Create Match</button>
            
        </form>
    );
};

export default CreateMatchForm;