import React from "react";
import fetchData from "../helper.js";
import { useNavigate } from "react-router-dom";
import {
  Typography,
  Box,
  Button,
  Avatar,
  Card,
  CardContent,
} from "@mui/material";
import defaultPic from "../images/remy.jpg";

export default function UserCard({ user }) {
  const token = localStorage.getItem("token");
  const navigate = useNavigate();

  const [followerCount, setFollowerCount] = React.useState(user.followers);
  const [isSubscribed, setIsSubscribed] = React.useState(false);

  const [cardIsHover, setCardIsHover] = React.useState(false);
  const [picIsHover, setPicIsHover] = React.useState(false);
  const [contactIsHover, setContactIsHover] = React.useState(false);
  const [bioIsHover, setBioIsHover] = React.useState(false);

  async function loadU() {
    const data = await fetchData(
      "GET",
      `api/userInfo?userId=${user.id}`,
      {},
      token
    );
    return data;
  }

  React.useEffect(() => {
    async function loadUser() {
      const userInfo = await loadU();
      setIsSubscribed(userInfo.isSubscribed);
    }
    if (token) {
      loadUser();
    }
  }, []);

  const subscribe = () => {
    fetchData("POST", "api/subscribe", { userId: user.id }, token);
    setFollowerCount(parseInt(followerCount) + 1);
    setIsSubscribed(true);
  };

  const unsubscribe = () => {
    fetchData("POST", "api/unsubscribe", { userId: user.id }, token);
    setFollowerCount(parseInt(followerCount) - 1);
    setIsSubscribed(false);
  };

  const navToUser = () => {
    navigate(`/profile/${user.id}`);
  };

  const statsBox = {
    display: "flex",
    justifyContent: "center",
    margin: "10px",
    backgroundColor: "white",
    marginBottom: "40px",
  };
  const statsStyle = { margin: "10px", height: "auto", width: "100px" };
  const bioStyle = { margin: "10px", fontStyle: "italic" };
  const cardHover = {
    padding: "40px",
    margin: "10px",
    width: "auto",
    transform: "scale3d(1.05, 1.05, 1)",
    transition: "transform 0.15s ease-in-out",
  };
  const cardNoHover = { padding: "40px", margin: "10px", width: "auto" };

  const picHover = {
    width: "200px",
    height: "200px",
    margin: "10px",
    cursor: "pointer",
    transform: "scale3d(1.05, 1.05, 1)",
    transition: "transform 0.15s ease-in-out",
  };
  const picNoHover = {
    width: "200px",
    height: "200px",
    margin: "10px",
    transition: "transform 0.15s ease-in-out",
  };

  const contentHover = {
    cursor: "pointer",
    transform: "scale3d(1.05, 1.05, 1)",
    transition: "transform 0.15s ease-in-out",
  };
  const contentNoHover = { transition: "transform 0.15s ease-in-out" };

  return (
    <>
      <Card
        sx={{ maxWidth: 345 }}
        onMouseEnter={() => setCardIsHover(true)}
        onMouseLeave={() => setCardIsHover(false)}
        style={cardIsHover ? cardHover : cardNoHover}
      >
        {user.profilePic ? (
          <Box sx={{ display: "flex", justifyContent: "center" }}>
            <Avatar
              alt="user's profile picture"
              src={user.profilePic}
              onMouseEnter={() => setPicIsHover(true)}
              onMouseLeave={() => setPicIsHover(false)}
              style={picIsHover ? picHover : picNoHover}
              onClick={() => navToUser()}
            />
          </Box>
        ) : (
          <Box sx={{ display: "flex", justifyContent: "center" }}>
            <Avatar
              alt="default profile picture"
              src={defaultPic}
              onMouseEnter={() => setPicIsHover(true)}
              onMouseLeave={() => setPicIsHover(false)}
              style={picIsHover ? picHover : picNoHover}
              onClick={() => navToUser()}
            />
          </Box>
        )}

        <Box
          onClick={() => navToUser()}
          onMouseEnter={() => setContactIsHover(true)}
          onMouseLeave={() => setContactIsHover(false)}
          style={contactIsHover ? contentHover : contentNoHover}
        >
          <Typography variant="body2">@{user.username}</Typography>
          <Typography variant="body2">{user.email}</Typography>
        </Box>

        <CardContent>
          <Box
            onClick={() => navToUser()}
            onMouseEnter={() => setBioIsHover(true)}
            onMouseLeave={() => setBioIsHover(false)}
            style={bioIsHover ? contentHover : contentNoHover}
          >
            <Typography variant="h5">{user.name}</Typography>
            {user.title ? (
              <Typography variant="h6">{user.title}</Typography>
            ) : (
              <Typography variant="h6">Aspiring Masterchef</Typography>
            )}
            {user.bio ? (
              <Typography variant="body2" style={bioStyle}>
                {user.bio}
              </Typography>
            ) : (
              <Typography variant="body2" style={bioStyle}>
                So ya like jazz?
              </Typography>
            )}
          </Box>

          <Box style={statsBox}>
            <Box style={statsStyle}>
              <Typography variant="h5">
                {user.publishedRecipes.length}
              </Typography>
              <Typography variant="h8">Recipes</Typography>
            </Box>
            <Box style={statsStyle}>
              <Typography variant="h5">{followerCount}</Typography>
              <Typography variant="h8">Followers</Typography>
            </Box>
          </Box>

          {token ? (
            <Box>
              {isSubscribed ? (
                <Button onClick={unsubscribe}>UnSubscribe</Button>
              ) : (
                <Button variant="outlined" onClick={subscribe}>
                  Subscribe
                </Button>
              )}
            </Box>
          ) : (
            <Box></Box>
          )}
        </CardContent>
      </Card>
    </>
  );
}
