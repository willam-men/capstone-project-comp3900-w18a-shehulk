import React from "react";
import PropTypes from "prop-types";
import { Paper, Typography, Collapse, Alert } from "@mui/material";
import LoginForm from "../components/LoginForm";
import { useNavigate } from "react-router-dom";
import fetchData from "../helper.js";

export default function Login({ setIsLoggedIn }) {
  const navigate = useNavigate();
  const paperStyle = { padding: "100px", width: "70vw", margin: "50px auto" };
  const headingStyle = { marginBottom: "20px" };

  const [openLoginError, setOpenLoginError] = React.useState(false);

  React.useEffect(() => {
    if (openLoginError === true) {
      setTimeout(() => {
        setOpenLoginError(false);
      }, 3000);
    }
  }, [openLoginError]);

  return (
    <>
      <Paper elevation={3} style={paperStyle}>
        <Collapse in={openLoginError}>
          <Alert
            onClose={() => {
              setOpenLoginError(false);
            }}
            severity="error"
          >
            Please review all errors before submitting.
          </Alert>
        </Collapse>
        <Typography variant="h4" style={headingStyle}>
          Login
        </Typography>
        <LoginForm
          setOpenLoginError={setOpenLoginError}
          submit={async (email, password) => {
            const body = { email, password };
            const data = await fetchData("POST", "api/login", body, null);
            localStorage.setItem("token", data.token);
            setIsLoggedIn(true);
            navigate("/loginwelcome");
          }}
        />
      </Paper>
    </>
  );
}

Login.propTypes = {
  setIsLoggedIn: PropTypes.bool,
};
