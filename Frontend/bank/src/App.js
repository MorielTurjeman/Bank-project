
import './App.css';
import NavBar from './components/NavBar';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'
import Transactions from './pages/transactions';
import Oparetions from './pages/oparetions';
import Breakdowns from './pages/breakdowns';
import { useEffect, useState } from 'react';
import UserApi from './data/userApi';


function App() {
  const [shouldReloadBalance, setShouldReloadBalance] = useState(true)
  const [balance, setBalance] = useState(0)

  useEffect(() => {
    if (shouldReloadBalance) {
      UserApi.getBalance().then(balance => setBalance(balance)).catch(err => console.log(err))
      setShouldReloadBalance(false)
    }
  }, [shouldReloadBalance])

  return (<Router>
    <div className="App">

      <div>
        <NavBar balance={balance} />

        <Route path="/Transactions" exact render={() => <Transactions setShouldReloadBalance={setShouldReloadBalance} />} />
        <Route path="/Oparetions" exact render={() => <Oparetions setShouldReloadBalance={setShouldReloadBalance} />} />
        <Route path="/Breakdowns" exact render={() => <Breakdowns />} />


      </div>
    </div >
  </Router>
  );
}

export default App;
