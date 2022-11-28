import React from "react";
import fetchData from "../helper.js";
import { Typography, Box, CircularProgress, Grid, Fab } from "@mui/material";

import UserCard from "../components/UserCard.jsx";
import NavigationIcon from "@mui/icons-material/Navigation";

export default function AllUsers() {
  const token = localStorage.getItem("token");

  const [users, setUsers] = React.useState(null);
  const [loading, setLoading] = React.useState(true);
  const [showScroll, setShowScroll] = React.useState(false);

  async function loadU() {
    const data = await fetchData("GET", `api/user_infos`, {}, token);
    return data;
  }

  React.useEffect(() => {
    async function loadUsers() {
      const userInfos = await loadU();
      setUsers(userInfos);
      setLoading(false);
    }
    loadUsers();
  }, []);

  // code adapted from https://dev.to/prnvbirajdar/react-hooks-component-to-smooth-scroll-to-the-top-35fd
  React.useEffect(() => {
    // Button is displayed after scrolling for 500 pixels
    const scrollToggle = () => {
      if (window.pageYOffset > 500) {
        setShowScroll(true);
      } else {
        setShowScroll(false);
      }
    };

    window.addEventListener("scroll", scrollToggle);
    return () => window.removeEventListener("scroll", scrollToggle);
  }, []);

  const titleStyle = { margin: "40px" };
  const boxStyle = {
    margin: "10px",
    display: "flex",
    justfyContent: "center",
    width: "100%",
  };
  const fabStyle = {
    position: "fixed",
    bottom: 16,
    right: 16,
  };

  return (
    <>
      {loading ? (
        <Box>
          <CircularProgress />
        </Box>
      ) : (
        <Box>
          <Typography variant="h4" style={titleStyle}>
            The Ratatouille Community
          </Typography>

          <Box style={boxStyle}>
            <Grid
              container
              spacing={{ xs: 2, md: 3 }}
              columns={{ xs: 4, sm: 8, md: 12 }}
            >
              {users.map((user, index) => {
                return (
                  <Grid
                    item
                    xs={2}
                    sm={4}
                    md={4}
                    key={index}
                    display="flex"
                    justifyContent="center"
                    alignItems="center"
                  >
                    <UserCard user={user} />
                  </Grid>
                );
              })}
            </Grid>
          </Box>

          {showScroll && (
            <Fab
              variant="extended"
              style={fabStyle}
              onClick={() =>
                window.scrollTo({ top: 0, left: 0, behavior: "smooth" })
              }
            >
              <NavigationIcon sx={{ mr: 1 }} />
              Back To Top
            </Fab>
          )}
        </Box>
      )}
    </>
  );
}
