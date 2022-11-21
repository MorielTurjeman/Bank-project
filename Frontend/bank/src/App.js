
import './App.css';
import NavBar from './components/NavBar';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'
import Transactions from './pages/transactions';
import Oparetions from './pages/oparetions';
import Breakdowns from './pages/breakdowns';
import TransactionsApi from './data/transactionsApi';
import { useEffect, useState } from 'react';


function App() {
  return (<Router>
    <div className="App">

      <div>
        <NavBar />

        <Route path="/Transactions" exact render={() => <Transactions />} />
        <Route path="/Oparetions" exact render={() => <Oparetions />} />
        <Route path="/Breakdowns" exact render={() => <Breakdowns />} />


      </div>
    </div >
  </Router>
  );
}

export default App;
