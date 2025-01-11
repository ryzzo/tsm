import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Management from './admin_components/Management';
import MainPage from './components/MainPage';

import './App.css';
import LeagueTable from './components/LeagueTable';
import MatchResults from './components/MatchList';


const App = () => {
  return (
    <div>
      <h1>Sports Media</h1>

      <Router>
        <Routes>
          <Route path='/' element={<MainPage />}> 
            <Route path='/matches' element={<MatchResults />}></Route>
            <Route path='/league-table' element={<LeagueTable />}></Route>
          </Route>
          <Route path='/management' element={<Management />}></Route>
        </Routes>
      </Router>
    </div>
  );
};

export default App;
