import { useParams, useNavigate } from "react-router-dom";
import React from "react";
import fetchData from "../helper.js";
import {
  Typography,
  Paper,
  CircularProgress,
  Box,
  Button,
  Avatar,
  Dialog,
  Grid,
  IconButton,
  Fab,
  Breadcrumbs,
  Link,
  Alert,
  Collapse,
  Tooltip,
} from "@mui/material";
import defaultPic from "../images/remy.jpg";
import PhotoCameraIcon from "@mui/icons-material/PhotoCamera";

import KeyboardDoubleArrowDownIcon from "@mui/icons-material/KeyboardDoubleArrowDown";
import KeyboardDoubleArrowUpIcon from "@mui/icons-material/KeyboardDoubleArrowUp";

import EditProfileDialog from "../components/EditProfileDialog.jsx";
import EditProfPicDialog from "../components/EditProfPicDialog.jsx";
import RecipeCard from "../components/RecipeCard";

export default function Profile({ setUserProfPic }) {
  const params = useParams();
  const token = localStorage.getItem("token");
  const navigate = useNavigate();

  const [scrollDown, setScrollDown] = React.useState(true);

  const [openSuccessProfPic, setOpenSuccessProfPic] = React.useState(false);
  const [openSuccessProfile, setOpenSuccessProfile] = React.useState(false);

  const uinfo = {
    name: "",
    username: "",
    email: "",
    title: "",
    bio: "",
    followers: 0,
    likes: 0,
    profilepic: null,
    isSelf: false,
    isSubscribed: false,
    recipes: [],
  };

  const userId = params.userid;
  const [loading, setLoading] = React.useState(true);
  const [userInfo, setUserInfo] = React.useState(uinfo);

  // initially set to 0
  const [followerCount, setFollowerCount] = React.useState(0);
  // initially set to null
  const [isSubscribed, setIsSubscribed] = React.useState(null);
  const [profpic, setProfpic] = React.useState(null);

  const [isRecipes, setIsRecipes] = React.useState(false);

  const [editProfileOpen, setEditProfileOpen] = React.useState(false);
  const [editPicOpen, setEditPicOpen] = React.useState(false);

  const [update, setUpdate] = React.useState(true);

  // waiting for backend to finish get user route
  async function loadUser() {
    const data = await fetchData(
      "GET",
      `api/userInfo?userId=${params.userid}`,
      {},
      token
    );
    return data;
  }

  React.useEffect(() => {
    async function loadu() {
      window.scrollTo(0, 0);
      const userOutput = await loadUser();
      if ("code" in userOutput) {
        navigate("/notfound");
      }
      setIsSubscribed(userInfo.isSubscribed);
      setUserInfo(userOutput);
      setFollowerCount(userOutput.followers);
      setIsSubscribed(userOutput.isSubscribed);
      setProfpic(userOutput.profilePic);
      if (userOutput.recipes.length !== 0) {
        setIsRecipes(true);
      }
      setLoading(false);
    }
    loadu();
  }, [update, params]);

  // code adapted from https://dev.to/prnvbirajdar/react-hooks-component-to-smooth-scroll-to-the-top-35fd
  React.useEffect(() => {
    // Button is displayed after scrolling for 500 pixels
    const scrollToggle = () => {
      if (window.pageYOffset > 400) {
        setScrollDown(false);
      } else {
        setScrollDown(true);
      }
    };

    window.addEventListener("scroll", scrollToggle);
    return () => window.removeEventListener("scroll", scrollToggle);
  }, []);

  React.useEffect(() => {
    if (openSuccessProfPic === true) {
      setTimeout(() => {
        setOpenSuccessProfPic(false);
      }, 3000);
    }
    if (openSuccessProfile === true) {
      setTimeout(() => {
        setOpenSuccessProfile(false);
      }, 3000);
    }
  }, [openSuccessProfPic, openSuccessProfile]);

  const subscribe = () => {
    fetchData("POST", "api/subscribe", { userId: userId }, token);
    setFollowerCount(parseInt(followerCount) + 1);
    setIsSubscribed(true);
  };

  const unsubscribe = () => {
    fetchData("POST", "api/unsubscribe", { userId: userId }, token);
    setFollowerCount(parseInt(followerCount) - 1);
    setIsSubscribed(false);
  };

  const navToLogin = () => {
    navigate("/login");
  };

  const handleEditProfileOpen = () => {
    setEditProfileOpen(true);
  };

  const handleEditProfileClose = () => {
    setEditProfileOpen(false);
  };

  const handleEditPicOpen = () => {
    setEditPicOpen(true);
  };

  const handleEditPicClose = () => {
    setEditPicOpen(false);
  };

  const pageStyle = { padding: "100px" };
  const avatarStyle = { width: "200px", height: "200px", margin: "10px" };
  const profPicEditStyle = { transform: "translate(80px, -40px)" };
  const infoStyle = { margin: "5px" };
  const bioStyle = { margin: "40px", fontStyle: "italic" };
  const statsStyle = { margin: "10px", height: "100px", width: "100px" };
  const buttonStyle = { margin: "10px", width: "50%" };
  const boxStyle = {
    margin: "10px",
    display: "flex",
    justfyContent: "center",
    width: "100%",
  };
  const recipeTitleStyle = { marginTop: "150px", marginBottom: "50px" };
  const fabStyle = {
    position: "fixed",
    bottom: 16,
    right: 16,
  };

  return (
    <>
      {loading ? (
        <Box sx={{ display: "flex" }}>
          <CircularProgress />
        </Box>
      ) : (
        <Box>
          <Collapse in={openSuccessProfPic}>
            <Alert
              onClose={() => {
                setOpenSuccessProfPic(false);
              }}
              severity="success"
            >
              Sucessfully changed profile picture —{" "}
              <strong>check it out!</strong>
            </Alert>
          </Collapse>
          <Collapse in={openSuccessProfile}>
            <Alert
              onClose={() => {
                setOpenSuccessProfile(false);
              }}
              severity="success"
            >
              Sucessfully changed profile details —{" "}
              <strong>check it out!</strong>
            </Alert>
          </Collapse>
          <Paper style={pageStyle}>
            <Breadcrumbs aria-label="breadcrumb">
              <Link
                underline="hover"
                color="inherit"
                onClick={() => navigate("/users")}
              >
                All Profiles
              </Link>
              <Typography color="text.primary">{userInfo.name}</Typography>
            </Breadcrumbs>

            {profpic === null ? (
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
                  src={profpic}
                  style={avatarStyle}
                />
              </Box>
            )}
            {token && userInfo.isSelf && (
              <Tooltip title="Change Profile Picture">
                <IconButton
                  size="large"
                  style={profPicEditStyle}
                  onClick={handleEditPicOpen}
                >
                  <PhotoCameraIcon />
                </IconButton>
              </Tooltip>
            )}
            <Typography style={infoStyle} variant="h3">
              {userInfo.name}
            </Typography>
            <Typography style={infoStyle} variant="h6">
              {userInfo.title}
            </Typography>
            <Typography variant="h8">@{userInfo.username} | </Typography>
            <Typography variant="h8">{userInfo.email}</Typography>
            <Typography style={bioStyle} variant="h6">
              {userInfo.bio}
            </Typography>

            <Box sx={{ display: "flex", justifyContent: "center" }}>
              <Box style={statsStyle}>
                <Typography variant="h5">{userInfo.recipes.length}</Typography>
                <Typography variant="h8">Recipes</Typography>
              </Box>
              <Box style={statsStyle}>
                <Typography variant="h5">{followerCount}</Typography>
                <Typography variant="h8">Followers</Typography>
              </Box>
              <Box style={statsStyle}>
                <Typography variant="h5">{userInfo.likes}</Typography>
                <Typography variant="h8">Likes</Typography>
              </Box>
            </Box>

            {token ? (
              <Box>
                {userInfo.isSelf ? (
                  <Box sx={{ display: "flex", justifyContent: "center" }}>
                    <Button
                      variant="outlined"
                      style={buttonStyle}
                      onClick={handleEditProfileOpen}
                    >
                      Edit Profile
                    </Button>
                    <Button
                      variant="outlined"
                      style={buttonStyle}
                      onClick={() => navigate("/personalsettings")}
                    >
                      Edit Personal Settings
                    </Button>
                  </Box>
                ) : (
                  <Box>
                    {isSubscribed ? (
                      <Button
                        variant="outlined"
                        style={buttonStyle}
                        onClick={unsubscribe}
                      >
                        Unsubscribe
                      </Button>
                    ) : (
                      <Button
                        variant="outlined"
                        style={buttonStyle}
                        onClick={subscribe}
                      >
                        Subscribe
                      </Button>
                    )}
                  </Box>
                )}
              </Box>
            ) : (
              <Box>
                <Button onClick={navToLogin}>Login To Subscribe</Button>
              </Box>
            )}
            <Dialog
              open={editProfileOpen}
              onClose={handleEditProfileClose}
              fullWidth
              maxWidth="sm"
            >
              <EditProfileDialog
                currInfo={userInfo}
                submit={async (name, title, bio) => {
                  const body = {
                    name: name,
                    title: title,
                    bio: bio,
                    token: token,
                  };
                  await fetchData(
                    "POST",
                    `api/profile/${userId}/update`,
                    body,
                    token
                  );
                  setOpenSuccessProfile(true);
                  handleEditProfileClose();
                  setUpdate(!update);
                  // refresh the page or update the userInfo
                }}
              />
            </Dialog>
            <Dialog
              open={editPicOpen}
              onClose={handleEditPicClose}
              fullWidth
              maxWidth="sm"
            >
              <EditProfPicDialog
                submit={async (img) => {
                  await fetchData(
                    "POST",
                    `api/profile/${userId}/update`,
                    { profile_picture: img, token: token },
                    null
                  );
                  setOpenSuccessProfPic(true);
                  handleEditPicClose();
                  setUserProfPic(img);
                  setUpdate(!update);
                  // refresh the page or update the userInfo
                }}
              />
            </Dialog>

            {isRecipes ? (
              <Box>
                <Typography variant="h4" style={recipeTitleStyle}>
                  Recipes By {userInfo.name}
                </Typography>
                <Box style={boxStyle}>
                  <Grid
                    container
                    spacing={{ xs: 2, md: 3 }}
                    columns={{ xs: 4, sm: 8, md: 12 }}
                  >
                    {userInfo.recipes.map((recipe, index) => {
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
                          <RecipeCard
                            recipe={recipe}
                            origin={userInfo.isSelf ? "selfprofile" : "profile"}
                          />
                        </Grid>
                      );
                    })}
                  </Grid>
                </Box>
              </Box>
            ) : (
              <Typography style={recipeTitleStyle}>
                {userInfo.name} hasn't posted any recipes yet.
              </Typography>
            )}
            {isRecipes && (
              <>
                {scrollDown ? (
                  <Fab
                    variant="extended"
                    style={fabStyle}
                    onClick={() =>
                      window.scrollTo({
                        top: 1000,
                        left: 0,
                        behavior: "smooth",
                      })
                    }
                  >
                    <KeyboardDoubleArrowDownIcon sx={{ mr: 1 }} />
                    See Recipes By {userInfo.name}
                  </Fab>
                ) : (
                  <Fab
                    variant="extended"
                    style={fabStyle}
                    onClick={() =>
                      window.scrollTo({ top: 0, left: 0, behavior: "smooth" })
                    }
                  >
                    <KeyboardDoubleArrowUpIcon sx={{ mr: 1 }} />
                    Back To Top
                  </Fab>
                )}
              </>
            )}
          </Paper>
        </Box>
      )}
    </>
  );
}
