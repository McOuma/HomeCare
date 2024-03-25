import React, { Component } from "react";

class Register extends Component {
  constructor() {
    super();
    this.state = {
      username: "",
      email: "",
      password: "",
      password2: "",
      role: "caregiver",
      firstName: "",
      lastName: "",
      location: "",
      phoneNumber: "",
    };
  }

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    console.log(this.state);
    // Add form submission logic here
  };

  handleRoleChange = (e) => {
    this.setState({
      role: e.target.value
    });
  };

  render() {
    const { username, email, password, password2, role, firstName, lastName, location, phoneNumber } = this.state;

    return (
      <div>
        <div className="container mt-5">
          <div className="row justify-content-center">
            <div className="col-md-6">
              <h2 className="mb-4">Registration</h2>
              <form onSubmit={this.handleSubmit}>
                <div className="form-group">
                  <label htmlFor="roleSelect">Select Role:</label>
                  <select
                    className="form-control"
                    id="roleSelect"
                    name="role"
                    value={role}
                    onChange={this.handleRoleChange}
                  >
                    <option value="caregiver">Caregiver</option>
                    <option value="client">Client</option>
                  </select>
                </div>
                <div className="form-group">
                  <label htmlFor="username">Create Username:</label>
                  <input
                    type="text"
                    className="form-control"
                    id="username"
                    name="username"
                    placeholder="Create your username"
                    value={username}
                    onChange={this.handleChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="email">Email address:</label>
                  <input
                    type="email"
                    className="form-control"
                    id="email"
                    name="email"
                    placeholder="Enter email"
                    value={email}
                    onChange={this.handleChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="password">Create Password:</label>
                  <input
                    type="password"
                    className="form-control"
                    id="password"
                    name="password"
                    placeholder="Enter Password"
                    value={password}
                    onChange={this.handleChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="password2">Confirm Password:</label>
                  <input
                    type="password"
                    className="form-control"
                    id="password2"
                    name="password2"
                    placeholder="Confirm Password"
                    value={password2}
                    onChange={this.handleChange}
                  />
                </div>
                {role === "client" && (
                  <div className="form-group">
                    <label htmlFor="companyName">Company Name:</label>
                    <input
                      type="text"
                      className="form-control"
                      id="companyName"
                      name="companyName"
                      placeholder="Enter your company name"
                      value={this.state.companyName || ""}
                      onChange={this.handleChange}
                    />
                  </div>
                )}
                <div className="form-group">
                  <label htmlFor="firstName">First Name:</label>
                  <input
                    type="text"
                    className="form-control"
                    id="firstName"
                    name="firstName"
                    placeholder="Enter your first name"
                    value={firstName}
                    onChange={this.handleChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="lastName">Last Name:</label>
                  <input
                    type="text"
                    className="form-control"
                    id="lastName"
                    name="lastName"
                    placeholder="Enter your last name"
                    value={lastName}
                    onChange={this.handleChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="location">Location:</label>
                  <input
                    type="text"
                    className="form-control"
                    id="location"
                    name="location"
                    placeholder="Enter your location"
                    value={location}
                    onChange={this.handleChange}
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="phoneNumber">Phone Number:</label>
                  <input
                    type="text"
                    className="form-control"
                    id="phoneNumber"
                    name="phoneNumber"
                    placeholder="Enter your phone number"
                    value={phoneNumber}
                    onChange={this.handleChange}
                  />
                </div>
                <button type="submit" className="btn btn-primary">
                  Register
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Register;
