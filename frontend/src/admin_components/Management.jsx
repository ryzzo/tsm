import React, { useEffect, useState } from 'react';
import TeamManagement from './TeamManagement';
import CreateMatchForm from './CreateMatchForm';
import CreateTeamForm from './CreateTeamForm';

const Management = () => {
  return (
    <div>
      <CreateTeamForm />
      <TeamManagement />
      <CreateMatchForm />
    </div>
  );
};

export default Management;