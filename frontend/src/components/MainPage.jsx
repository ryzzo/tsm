import React from 'react';
import { Container, Nav, Navbar } from 'react-bootstrap';
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom';

import LeagueTable from './LeagueTable';
import MatchList from './MatchList';


const MainPage = () => {
  return (
    <>
      <Navbar bg='dark' data-bs-theme='dark'>
        <Container>
          <Navbar.Brand as={Link} to="/">
            KPL
          </Navbar.Brand>
          <Navbar.Toggle aria-controls='basic-navbar-nav' />
          <Navbar.Collapse id='basic-navbar-nav'>
            <Nav className='me-auto'>
              <Nav.Link as={Link} to='/league-table'>
                League Table
              </Nav.Link>
              <Nav.Link as={Link} to='/matches'>
                Matches
              </Nav.Link>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
        
      <Container className='mt-4'>
        <Routes>
          <Route path='/' element={<Navigate to='/league-table' replace />}/>
          <Route path='/league-table' element={<LeagueTable />}></Route>
          <Route path='/matches' element={<MatchList />}></Route>
        </Routes>
      </Container> 
    </>
  );
};

export default MainPage;