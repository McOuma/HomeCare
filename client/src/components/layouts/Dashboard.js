import React, { Component } from "react";

class Dashboard extends Component {
  constructor(props) {
    super(props);
    this.state = {
      serviceType: "",
      date: "",
      time: "",
    };
  }

  handleChange = (e) => {
    this.setState({
      [e.target.id]: e.target.value,
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    // Add your booking logic here
    console.log("Service Type:", this.state.serviceType);
    console.log("Date:", this.state.date);
    console.log("Time:", this.state.time);
  };

  render() {
    return (
      <div className="container mt-5">
        <div className="row">
          <div className="col-md-3">
            {/* Sidebar */}
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">Dashboard</h5>
                <ul className="list-group list-group-flush">
                  <li className="list-group-item">Profile</li>
                  <li className="list-group-item">Bookings</li>
                  <li className="list-group-item">Messages</li>
                </ul>
              </div>
            </div>
          </div>
          <div className="col-md-9">
            {/* Main Content */}
            <div className="card">
              <div className="card-body">
                <h5 className="card-title">Book a Caregiver</h5>
                <form onSubmit={this.handleSubmit}>
                  <div className="form-group">
                    <label htmlFor="serviceType">Service Type:</label>
                    <select
                      className="form-control"
                      id="serviceType"
                      value={this.state.serviceType}
                      onChange={this.handleChange}
                    >
                      <option value="">Select Service Type</option>
                      <option value="Childcare">Childcare</option>
                      <option value="Elderly Care">Elderly Care</option>
                      <option value="Special Needs Care">
                        Special Needs Care
                      </option>
                      {/* Add more options as needed */}
                    </select>
                  </div>
                  <div className="form-group">
                    <label htmlFor="date">Date:</label>
                    <input
                      type="date"
                      className="form-control"
                      id="date"
                      value={this.state.date}
                      onChange={this.handleChange}
                    />
                  </div>
                  <div className="form-group">
                    <label htmlFor="time">Time:</label>
                    <input
                      type="time"
                      className="form-control"
                      id="time"
                      value={this.state.time}
                      onChange={this.handleChange}
                    />
                  </div>
                  <button type="submit" className="btn btn-primary">
                    Book Now
                  </button>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Dashboard;
