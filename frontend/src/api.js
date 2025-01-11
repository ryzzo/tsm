import axios from 'axios';

const API_BASE = 'http://localhost:8000'; // Replace with your backend URL

export const fetchTeams = () => axios.get(`${API_BASE}/teams/`);
export const updateTeam = (id, data) => axios.put(`${API_BASE}/teams/${id}/`, data);
export const fetchMatches = () => axios.get(`${API_BASE}/matches/`);
export const updateMatchResult = (id, data) => axios.put(`${API_BASE}/matches/${id}/`, data);
export const matchByDates = () => axios.get(`${API_BASE}/matches-by-date/`);