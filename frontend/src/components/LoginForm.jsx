import React from "react";
import PropTypes from "prop-types";
import {
  Button,
  TextField,
  FormControl,
  InputAdornment,
  IconButton,
} from "@mui/material";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";

import crypto from "crypto-js";

export default function LoginForm({ submit, setOpenLoginError }) {
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [showPassword, setShowPassword] = React.useState(false);

  const [emailError, setEmailError] = React.useState(false);
  const [passError, setPassError] = React.useState(false);

  const [hasAttemptedLogin, setHasAttemptedLogin] = React.useState(false);

  const handleShowPass = () => {
    const visible = !showPassword;
    setShowPassword(visible);
  };

  const handleLoginSubmit = () => {
    setHasAttemptedLogin(true);

    // hash the password
    const hashedpass = crypto.SHA3(password).toString();

    // submit the login request if no errors
    if (checkEmailValid() || checkPassValid()) {
      setOpenLoginError(true);
    } else {
      submit(email, hashedpass);
    }
  };

  const checkValidity = () => {
    if (hasAttemptedLogin) {
      setTimeout(() => {
        checkEmailValid();
        checkPassValid();
      }, 800);
    }
  };

  const checkEmailValid = () => {
    const re = /^[a-zA-Z0-9]+@(?:[a-zA-Z0-9]+\.)+[A-Za-z]+$/;
    setEmailError(!re.test(email));
    return !re.test(email);
  };

  const checkPassValid = () => {
    if (password.length < 1) {
      setPassError(true);
      return true;
    } else {
      setPassError(false);
      return false;
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleLoginSubmit();
    }
  };

  const formStyle = { marginTop: "30px", width: "80%" };
  const buttonStyle = { marginTop: "50px" };

  return (
    <>
      <FormControl style={formStyle}>
        <TextField
          id="email-login"
          label="Email"
          aria-label="email"
          type="email"
          variant="outlined"
          onBlur={checkValidity}
          onChange={(e) => {
            setEmail(e.target.value);
          }}
          onKeyDown={(e) => handleKeyDown(e)}
          helperText={emailError ? "please enter a valid email" : ""}
          error={emailError ? true : false}
        />
      </FormControl>
      <br />
      <FormControl style={formStyle}>
        <TextField
          id="password-login"
          label="Password"
          aria-label="password"
          onBlur={checkValidity}
          onChange={(e) => {
            setPassword(e.target.value);
          }}
          onKeyDown={(e) => handleKeyDown(e)}
          helperText={passError ? "please enter a password" : ""}
          error={passError ? true : false}
          type={showPassword ? "text" : "password"}
          variant="outlined"
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <IconButton
                  aria-label="toggle password visibility"
                  onClick={handleShowPass}
                >
                  {showPassword ? <VisibilityOff /> : <Visibility />}
                </IconButton>
              </InputAdornment>
            ),
          }}
        />
      </FormControl>
      <br />
      <Button
        variant="contained"
        aria-label="login-button"
        id="submit-login"
        style={buttonStyle}
        onClick={handleLoginSubmit}
      >
        Login
      </Button>
    </>
  );
}

LoginForm.propTypes = {
  submit: PropTypes.array,
};
