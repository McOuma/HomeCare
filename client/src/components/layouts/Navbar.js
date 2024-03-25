// Navbar.js
import React, { Component } from "react";
import { Link } from "react-router-dom";

export default class Navbar extends Component {
  render() {
    return (
      <div>
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <div className="container">
            <Link className="navbar-brand" to="/">
              {this.props.title}
            </Link>
            <button
              className="navbar-toggler"
              type="button"
              data-toggle="collapse"
              data-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ml-auto">
                <li className="nav-item">
                  <Link className="nav-link" to="/">
                    {this.props.homePageText}
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/dashboard">
                    {this.props.dashBoard}
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/register">
                    {this.props.registerText}
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/login">
                    {this.props.loginText}
                  </Link>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="/">
                    {this.props.logoutText}
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    );
  }
}

Navbar.defaultProps = {
  title: "HomeCare",
  homePageText: "Home",
  dashBoard: "Dashboard",
  registerText: "Register",
  loginText: "Login",
  logoutText: "Logout"
};
