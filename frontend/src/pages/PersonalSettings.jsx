import React from "react";
import fetchData from "../helper.js";
import {
  Typography,
  Paper,
  Box,
  TextField,
  Button,
  Alert,
  CircularProgress,
  Dialog,
  Breadcrumbs,
  Link,
} from "@mui/material";
import EditIcon from "@mui/icons-material/Edit";
import SaveIcon from "@mui/icons-material/Save";
import ChangePassword from "../components/ChangePassword.jsx";
import { useNavigate } from "react-router-dom";

export default function PersonalSettings() {
  const navigate = useNavigate();

  const token = localStorage.getItem("token");

  const [user, setUser] = React.useState(null);
  const [loading, setLoading] = React.useState(true);

  const [email, setEmail] = React.useState("");
  const [username, setUsername] = React.useState("");

  const [editEmail, setEditEmail] = React.useState(false);
  const [editUsername, setEditUsername] = React.useState(false);

  const [emailError, setEmailError] = React.useState(false);
  const [usernameError, setUsernameError] = React.useState(false);

  const [success, setSuccess] = React.useState(false);

  const [changePassword, setChangePassword] = React.useState(false);

  async function loadU() {
    const data = await fetchData("GET", `api/user_details`, {}, token);
    return data;
  }

  React.useEffect(() => {
    async function loadUser() {
      const userInfo = await loadU();
      setEmail(userInfo.email);
      setUsername(userInfo.username);
      setUser(userInfo);
      setLoading(false);
    }
    loadUser();
  }, []);

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

  const handleSubmit = () => {
    if (checkEmailValid() || checkUsernameValid()) {
      alert("pls check errors");
    } else {
      const body = { email: email, username: username, token: token };
      fetchData("POST", "api/credentials/manage", body);
      setSuccess(true);
      setEditUsername(false);
      setEditEmail(false);
    }
  };

  const handleChangePassword = () => {
    setChangePassword(true);
  };

  const handleChangePasswordClose = () => {
    setChangePassword(false);
  };

  const pageStyle = { padding: "100px", width: "70vw", margin: "50px auto" };
  const inputStyle = { width: "300px", marginTop: "50px" };
  const editButton = { marginTop: "40px", padding: "20px" };
  const submitStyle = { margin: "40px" };
  const alertStyle = { display: "flex", justifyContent: "center" };

  return (
    <>
      {loading ? (
        <Box>
          <CircularProgress />
        </Box>
      ) : (
        <Paper style={pageStyle}>
          {success ? (
            <div>
              <Alert severity="success" sx={alertStyle}>
                Your personal details were successfully updated!
              </Alert>
              <br />
              <br />
            </div>
          ) : (
            <div></div>
          )}
          <Breadcrumbs aria-label="breadcrumb">
            <Link
              underline="hover"
              color="inherit"
              onClick={() => navigate(`/users/`)}
            >
              All Profiles
            </Link>
            <Link
              underline="hover"
              color="inherit"
              onClick={() => navigate(`/profile/${user.id}`)}
            >
              {user.name}
            </Link>
            <Typography color="text.primary">
              {/* {userInfo.name} */}
              Settings
            </Typography>
          </Breadcrumbs>
          <Typography variant="h3">Settings</Typography>
          <Box>
            <TextField
              style={inputStyle}
              label="Username"
              variant="outlined"
              defaultValue={user.username}
              onChange={(e) => {
                setUsername(e.target.value);
                setSuccess(false);
              }}
              helperText={
                usernameError
                  ? "please enter a username between 2 and 20 characters long using letters and numbers only"
                  : ""
              }
              disabled={editUsername ? false : true}
              error={usernameError ? true : false}
            />
            {editUsername ? (
              <SaveIcon
                style={editButton}
                onClick={() => {
                  setEditUsername(false);
                  checkUsernameValid();
                }}
              />
            ) : (
              <EditIcon
                style={editButton}
                onClick={() => {
                  setEditUsername(true);
                  setSuccess(false);
                }}
              />
            )}
          </Box>

          <Box>
            <TextField
              style={inputStyle}
              label="Email"
              variant="outlined"
              defaultValue={user.email}
              onChange={(e) => {
                setEmail(e.target.value);
              }}
              helperText={emailError ? "please enter a valid email" : ""}
              error={emailError ? true : false}
              disabled={editEmail ? false : true}
            />
            {editEmail ? (
              <SaveIcon
                style={editButton}
                onClick={() => {
                  setEditEmail(false);
                  checkEmailValid();
                }}
              />
            ) : (
              <EditIcon
                style={editButton}
                onClick={() => {
                  setEditEmail(true);
                  setSuccess(false);
                }}
              />
            )}
          </Box>

          <Dialog
            open={changePassword}
            onClose={handleChangePasswordClose}
            fullWidth
            maxWidth="sm"
          >
            <ChangePassword
              submit={async (current, newPass) => {
                const body = {
                  current_password: current,
                  new_password: newPass,
                  token: token,
                };
                await fetchData("POST", "api/credentials/manage", body);
                handleChangePasswordClose();
              }}
            />
          </Dialog>

          <Button
            style={submitStyle}
            variant="contained"
            onClick={handleChangePassword}
          >
            Update password
          </Button>
          <Button
            style={submitStyle}
            variant="contained"
            onClick={handleSubmit}
          >
            Submit Changes
          </Button>
        </Paper>
      )}
    </>
  );
}
