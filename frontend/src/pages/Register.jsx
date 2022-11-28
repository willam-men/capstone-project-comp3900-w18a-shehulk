import React from "react";
import PropTypes from "prop-types";
import fetchData from "../helper.js";

import { Paper, Typography, Collapse, Alert } from "@mui/material";
import RegisterForm from "../components/RegisterForm";

import { useNavigate } from "react-router-dom";

export default function Register({ setIsLoggedIn }) {
  const navigate = useNavigate();

  const [openRegisterError, setOpenRegisterError] = React.useState(false);

  React.useEffect(() => {
    if (openRegisterError === true) {
      setTimeout(() => {
        setOpenRegisterError(false);
      }, 3000);
    }
  }, [openRegisterError]);

  const paperStyle = { padding: "100px", width: "70vw", margin: "50px auto" };
  const headingStyle = { marginBottom: "20px" };

  return (
    <>
      <Paper elevation={3} style={paperStyle}>
        <Collapse in={openRegisterError}>
          <Alert
            onClose={() => {
              setOpenRegisterError(false);
            }}
            severity="error"
          >
            Please review all errors before submitting.
          </Alert>
        </Collapse>
        <Typography variant="h4" style={headingStyle}>
          Register
        </Typography>
        <RegisterForm
          setOpenRegisterError={setOpenRegisterError}
          submit={async (email, username, password, name) => {
            const body = { email, password, username, name };
            const data = await fetchData("POST", "api/register", body, null);
            localStorage.setItem("token", data.token);
            setIsLoggedIn(true);
            navigate("/loginwelcome");
          }}
        />
      </Paper>
    </>
  );
}

Register.propTypes = {
  setIsLoggedIn: PropTypes.bool,
};
