import React from "react";
import { useNavigate } from "react-router-dom";
import fetchData from "../helper.js";
import {
  Typography,
  Paper,
  Box,
  Button,
  Avatar,
  CircularProgress,
} from "@mui/material";
import defaultPic from "../images/remy.jpg";

export default function LoginWelcome() {
  const token = localStorage.getItem("token");
  const navigate = useNavigate();

  const [user, setUser] = React.useState(null);
  const [profPic, setProfPic] = React.useState(null);
  const [loading, setLoading] = React.useState(true);

  async function loadU() {
    const data = await fetchData("GET", `api/user_details`, {}, token);
    return data;
  }

  React.useEffect(() => {
    async function loadUser() {
      const userInfo = await loadU();
      setUser(userInfo);
      setProfPic(userInfo.profilePic);
      setLoading(false);
    }
    loadUser();
  }, []);

  const pageStyle = { padding: "100px" };
  const avatarStyle = { width: "200px", height: "200px", margin: "50px" };
  const buttonStyle = { padding: "10px", margin: "10px", width: "50%" };

  return (
    <>
      {loading ? (
        <Box>
          <CircularProgress />
        </Box>
      ) : (
        <Paper style={pageStyle}>
          <Typography variant="h3">Welcome {user.name}!</Typography>
          {profPic === null ? (
            <Box sx={{ display: "flex", justifyContent: "center" }}>
              <Avatar
                alt="default profile picture"
                src={defaultPic}
                style={avatarStyle}
              />
            </Box>
          ) : (
            <Box sx={{ display: "flex", justifyContent: "center" }}>
              <Avatar
                alt="default profile picture"
                src={profPic}
                style={avatarStyle}
              />
            </Box>
          )}

          <Box>
            <Button
              style={buttonStyle}
              variant="contained"
              onClick={() => {
                navigate("/feed");
              }}
            >
              Go To Personal Feed
            </Button>
            <Button
              style={buttonStyle}
              variant="contained"
              onClick={() => {
                navigate("/createrecipe");
              }}
            >
              Create A Recipe
            </Button>
            <Button
              style={buttonStyle}
              variant="contained"
              onClick={() => {
                navigate(`/profile/${user.id}`);
              }}
            >
              Go To Profile
            </Button>
          </Box>
        </Paper>
      )}
    </>
  );
}
