import React, { Component } from "react";

export default class Landing extends Component {
  render() {
    return (
      <div>
        <div className="container">
          <div className="jumbotron jumbotron-fluid">
            <div className="container">
              <h1 className="display-4">Welcome to HomeCare</h1>
              <p className="lead">
                "Welcome to HomeCare, your trusted platform connecting patients
                with compassionate caregivers. Whether you're seeking support
                for loved ones with special needs, assistance for the elderly,
                or care for individuals with chronic illnesses, HomeCare is here
                to provide personalized and reliable services. Our dedicated
                caregivers are committed to delivering quality care in the
                comfort of your own home. Join us today and experience peace of
                mind knowing your loved ones are in capable hands."
              </p>
            </div>
          </div>
        </div>

        <div className="cta-section">
          <div className="container">
            <div className="row">
              <div className="col-md-12 text-center">
                <h2>Ready to get started?</h2>
                <p>Sign up now to experience the power of our platform.</p>
                <a className="btn btn-light btn-lg" href="/" role="button">
                  Sign Up
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
