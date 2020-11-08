import * as React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import FacebookButton from './FacebookButton';
import GoogleButton from './GoogleButton';
import { Socket } from './Socket';

export default function App() {
  
  function handleSubmit(event) {
    event.preventDefault()
    Socket.emit('new user', {
      'user': 'new user',
    });
  }


  return (
    <Router>
      <div>
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <Link className="navbar-brand" to="/">liveArt</Link>
          <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
          </button>
          
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
              <ul className="navbar-nav mr-auto">
                  <li className="nav-item active">
                      <Link className="nav-link" to="/about">About</Link>
                  </li>
                  <li className="nav-item">
                      <Link className="nav-link" to="/events">Events</Link>
                  </li>
                  <li className="nav-item dropdown">
                      <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Dropdown
                  </a>
                      <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                          <a className="dropdown-item" href="#">Action</a>
                          <a className="dropdown-item" href="#">Another action</a>
                          <div className="dropdown-divider"></div>
                          <a className="dropdown-item" href="#">Something else here</a>
                      </div>
                  </li>
              </ul>
              <form className="form-inline my-2 my-lg-0">
                  <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Sign In</button>
              </form>
          </div>
        </nav>
        <div className="container">
          <Switch>
            <Route path="/about">
              <About />
            </Route>
            <Route path="/events">
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
    
  );
}

function About() {
  return (
    <div className="row">
      <div className="col-12 col-md-8">
        <p>Hello World</p>
      </div>
      <div className="col-6 col-md-4">
      </div>
    </div>
    
    );
}

