// App.js
import React, { Component } from "react";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import Login from "./components/auth/Login";
import Register from "./components/auth/Register";
import Dashboard from "./components/layouts/Dashboard"; // Import Dashboard
import Footer from "./components/layouts/Footer";
import Landing from "./components/layouts/Landing";
import Navbar from "./components/layouts/Navbar";

export default class App extends Component {
  render() {
    return (
      <div>
        <Router>
          <div className="App">
            <Navbar />

            <Routes>
              <Route path="/" element={<Landing />} />
              <Route exact path="/register" element={<Register />} />
              <Route exact path="/login" element={<Login />} />
              <Route exact path="/dashboard" element={<Dashboard />} /> 
            </Routes>

            <Footer />
          </div>
        </Router>
      </div>
    );
  }
}
