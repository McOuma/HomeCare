import React, { Component } from "react";

export default class Navbar extends Component {
  render() {
    return (
      <div>
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <div className="container">
            <a className="navbar-brand" href="/">
              {this.props.title}
            </a>
            <button
              className="navbar-toggler"
              type="button"
              data-toggle="collapse"
              data-target="/navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav ml-auto">
                <li className="nav-item">
                  <a className="nav-link" href="/">
                    {this.props.homePageText}
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="/">
                   {this.props.dashBoard}
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="/">
                    {this.props.registerText}
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="/">
                    {this.props.loginText}
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="/">
                    {this.props.logoutTest}
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
    logoutTest: "Logout"

};
