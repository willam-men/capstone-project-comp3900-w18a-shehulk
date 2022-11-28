import React from "react";
import {
  Button,
  TextField,
  FormControl,
  InputAdornment,
  IconButton,
} from "@mui/material";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";
import PropTypes from "prop-types";
import crypto from "crypto-js";

export default function RegisterForm({ submit, setOpenRegisterError }) {
  const [email, setEmail] = React.useState("");
  const [username, setUsername] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [name, setName] = React.useState("");
  const [passwordConf, setPasswordConf] = React.useState("");
  const [showPassword, setShowPassword] = React.useState(false);
  const [showConfPassword, setShowConfPassword] = React.useState(false);

  const [emailError, setEmailError] = React.useState(false);
  const [usernameError, setUsernameError] = React.useState(false);
  const [nameError, setNameError] = React.useState(false);
  const [passwordMatchError, setPasswordMatchError] = React.useState(false);
  const [passwordError, setPasswordError] = React.useState(false);
  const [hasAttemptedRegister, setHasAttemptedRegister] = React.useState(false);

  const handleShowPass = () => {
    const visible = !showPassword;
    setShowPassword(visible);
  };

  const handleShowConfPass = () => {
    const visible = !showConfPassword;
    setShowConfPassword(visible);
  };

  const checkValidity = () => {
    if (hasAttemptedRegister) {
      setTimeout(() => {
        checkEmailValid();
        checkUsernameValid();
        checkNameValid();
        checkPasswordMatch();
        checkPasswordValid();
      }, 800);
    }
  };

  const handleRegisterSubmit = () => {
    // check validity of everything
    setHasAttemptedRegister(true);
    if (
      checkEmailValid() ||
      checkUsernameValid() ||
      checkPasswordMatch() ||
      checkPasswordValid() ||
      checkNameValid()
    ) {
      setOpenRegisterError(true);
    } else {
      const hashedpass = crypto.SHA3(password).toString();
      submit(email, username, hashedpass, name);
    }
  };

  const checkEmailValid = () => {
    // check email is in a valid format
    const re = /^[a-zA-Z0-9]+@(?:[a-zA-Z0-9]+\.)+[A-Za-z]+$/;
    setEmailError(!re.test(email));
    return !re.test(email);
  };

  const checkUsernameValid = () => {
    // username must be between 2 and 20 characters long
    // using alpha numeric characters only
    if (
      username.match(/^[0-9A-Za-z]+$/) === null ||
      username.length < 2 ||
      username.length > 20
    ) {
      setUsernameError(true);
      return true;
    } else {
      setUsernameError(false);
      return false;
    }
  };
  const checkNameValid = () => {
    // username must be between 2 and 20 characters long
    // using alpha characters only + spaces
    if (
      name.match(/^[a-zA-Z\s]*$/) === null ||
      name.length < 2 ||
      name.length > 20
    ) {
      setNameError(true);
      return true;
    } else {
      setNameError(false);
      return false;
    }
  };

  const checkPasswordMatch = () => {
    if (password !== passwordConf) {
      setPasswordMatchError(true);
      return true;
    } else {
      setPasswordMatchError(false);
      return false;
    }
  };

  const checkPasswordValid = () => {
    const uppercaseRegExp = /(?=.*?[A-Z])/;
    const lowercaseRegExp = /(?=.*?[a-z])/;
    const digitsRegExp = /(?=.*?[0-9])/;
    const specialCharRegExp = /(?=.*?[#?!@$%^&*-])/;

    if (
      password.length < 8 ||
      !uppercaseRegExp.test(password) ||
      !lowercaseRegExp.test(password) ||
      !digitsRegExp.test(password) ||
      !specialCharRegExp.test(password)
    ) {
      setPasswordError(true);
      return true;
    } else {
      setPasswordError(false);
      return false;
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      handleRegisterSubmit();
    }
  };

  const formStyle = { marginTop: "30px", width: "80%" };
  const buttonStyle = { marginTop: "50px" };

  return (
    <>
      <FormControl style={formStyle}>
        <TextField
          id="email-register"
          label="Email"
          aria-label="email"
          type="email"
          variant="outlined"
          onBlur={checkValidity}
          onChange={(e) => {
            setEmail(e.target.value);
          }}
          helperText={emailError ? "Please enter a valid email" : ""}
          error={emailError ? true : false}
        />
      </FormControl>
      <br />
      <FormControl style={formStyle}>
        <TextField
          id="username-register"
          label="Username"
          aria-label="username"
          type="text"
          variant="outlined"
          onBlur={checkValidity}
          onKeyDown={(e) => handleKeyDown(e)}
          onChange={(e) => {
            setUsername(e.target.value);
          }}
          helperText={
            usernameError
              ? "Please enter a username between 2 and 20 characters long using letters and numbers only"
              : ""
          }
          error={usernameError ? true : false}
        />
      </FormControl>
      <br />
      <FormControl style={formStyle}>
        <TextField
          id="name-register"
          label="Name"
          aria-label="name"
          type="text"
          variant="outlined"
          onBlur={checkValidity}
          onKeyDown={(e) => handleKeyDown(e)}
          onChange={(e) => {
            setName(e.target.value);
          }}
          helperText={
            nameError
              ? "Please enter a name between 2 and 20 characters long using letters and spaces only"
              : ""
          }
          error={nameError ? true : false}
        />
      </FormControl>
      <br />
      <FormControl style={formStyle}>
        <TextField
          id="password-register"
          label="Password"
          aria-label="password"
          onBlur={checkValidity}
          onKeyDown={(e) => handleKeyDown(e)}
          onChange={(e) => {
            setPassword(e.target.value);
          }}
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
          helperText={
            passwordError
              ? "Password must be at least 8 characters long and contain a minimum of one lowercase, uppercase, digit and special character"
              : ""
          }
          error={passwordError ? true : false}
        />
      </FormControl>
      <br />
      <FormControl style={formStyle}>
        <TextField
          id="passwordconf-register"
          label="Confirm Password"
          aria-label="confirm password"
          onBlur={checkValidity}
          onKeyDown={(e) => handleKeyDown(e)}
          onChange={(e) => {
            setPasswordConf(e.target.value);
          }}
          type={showConfPassword ? "text" : "password"}
          variant="outlined"
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <IconButton
                  aria-label="toggle password confirmation visibility"
                  onClick={handleShowConfPass}
                >
                  {showConfPassword ? <VisibilityOff /> : <Visibility />}
                </IconButton>
              </InputAdornment>
            ),
          }}
          helperText={passwordMatchError ? "Passwords do not match" : ""}
          error={passwordMatchError ? true : false}
        />
      </FormControl>
      <br />
      <Button
        variant="contained"
        aria-label="register-button"
        id="submit-register"
        style={buttonStyle}
        onClick={handleRegisterSubmit}
      >
        Register
      </Button>
    </>
  );
}

RegisterForm.propTypes = {
  submit: PropTypes.array,
};
