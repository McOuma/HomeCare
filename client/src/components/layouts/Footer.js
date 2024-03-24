import React, { Component } from "react";

export default class Footer extends Component {
  render() {
    return (
      <footer className="footer bg-dark text-light">
        <div className="container py-5">
          <div className="row">
            <div className="col-md-4">
              <h5>Company</h5>
              <ul className="list-unstyled">
                <li>
                  <a href="/">About Us</a>
                </li>
                <li>
                  <a href="/">Careers</a>
                </li>
                <li>
                  <a href="/">Investor Relations</a>
                </li>
                <li>
                  <a href="/">Trust, Safety & Security</a>
                </li>
              </ul>
            </div>
            <div className="col-md-4">
              <h5>Services</h5>
              <ul className="list-unstyled">
                <li>
                  <a href="/">Caregiver by Skill</a>
                </li>
                <li>
                  <a href="/">Search Caregiver by Location</a>
                </li>
                <li>
                  <a href="/">Schedule Booking</a>
                </li>
                <li>
                  <a href="/">Register</a>
                </li>
              </ul>
            </div>
            <div className="col-md-4">
              <h5>Contact Us</h5>
              <address>
                P .O. Box 34553-00100
                <br />
               Nairobi County
                <br />
                Kenya
                <br />
                <abbr title="Phone">Phone No:</abbr> (+254) 756-7890-092
              </address>
            </div>
          </div>
        </div>
        <div className="container-fluid bg-secondary text-center py-3">
                <p className="mb-0">&copy; {new Date().getFullYear() }HomeCare. All rights reserved.</p>
        </div>
      </footer>
    );
  }
}
