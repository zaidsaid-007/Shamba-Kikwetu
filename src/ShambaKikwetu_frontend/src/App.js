import './App.css';
import Nav from "./Components/Navbar/navbar.components";
import Body from "./Components/Body/body.component";
import { BrowserRouter as Router } from 'react-router-dom';

function App() {
  return (
    <div className="data">
        <Nav></Nav>
        <Body />
    </div>

  );
}

export default App;
