import React, { useReducer } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

const initialState = {
  username: "",
  password: "",
  loading: false,
  error: null,
  loggedIn: false
};

const reducer = (state, action) => {
  switch (action.type) {
    case "FIELD_CHANGE":
      return {
        ...state,
        [action.field]: action.value,
        error: null
      };
    case "LOGIN_START":
      return {
        ...state,
        loading: true,
        error: null
      };
    case "LOGIN_SUCCESS":
      return {
        ...state,
        loading: false,
        loggedIn: true
      };
    case "LOGIN_FAILURE":
      return {
        ...state,
        loading: false,
        error: action.error
      };
    default:
      return state;
  }
};

const Login = () => {
  const [state, dispatch] = useReducer(reducer, initialState);

  const handleChange = (e) => {
    dispatch({
      type: "FIELD_CHANGE",
      field: e.target.id,
      value: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    dispatch({ type: "LOGIN_START" });
    const { username, password } = state;
    try {
      // Send login data to the server
      const response = await axios.post("/api/v1/login", {
        username,
        password
      });
      // Handle successful login response
      console.log("Login successful:", response.data);
      dispatch({ type: "LOGIN_SUCCESS" });
      // Redirect the user or perform other actions
    } catch (error) {
      // Handle login error
      console.error("Error logging in:", error.message);
      dispatch({ type: "LOGIN_FAILURE", error: error.message });
      // Display error message to the user
    }
  };

  const { username, password, loading, error } = state;

  return (
    <>
      <div className="login-container">
        <div className="login-form">
          <h2>Login</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <input
                type="text"
                className="form-control"
                id="username"
                placeholder="Username"
                value={username}
                onChange={handleChange}
                required
              />
            </div>
            <br />
            <div className="form-group">
              <input
                type="password"
                className="form-control"
                id="password"
                placeholder="Password"
                value={password}
                onChange={handleChange}
                required
              />
            </div>
            <br />
            <button type="submit" className="btn btn-primary btn-block" disabled={loading}>
              {loading ? 'Logging in...' : 'Login'}
            </button>
            {error && <div className="text-danger">{error}</div>}
          </form>
          <hr />
          <div className="text-center">
            <p className="forgot-password">
              Forgot your password? <a href="/">Reset it here</a>.
            </p>
            <p>
              Don't have an account? <Link to="/register">Sign up</Link>.
            </p>
          </div>
        </div>
      </div>
    </>
  );
};

export default Login;
