import React from "react";
import fetchData from "../helper.js";

import {
  AppBar,
  Box,
  Toolbar,
  IconButton,
  Typography,
  Menu,
  Container,
  Avatar,
  Tooltip,
  MenuItem,
} from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import RestaurantMenuIcon from "@mui/icons-material/RestaurantMenu";
import defaultPic from "../images/remy.jpg";

import { useNavigate } from "react-router-dom";

export default function NavBar({ setUserProfPic, userProfPic, setIsLoggedIn }) {
  const token = localStorage.getItem("token");

  const navigate = useNavigate();
  const [anchorElNav, setAnchorElNav] = React.useState(null);
  const [anchorElUser, setAnchorElUser] = React.useState(null);

  const [user, setUser] = React.useState(null);
  const [logoHover, setLogoHover] = React.useState(false);

  async function loadU() {
    const data = await fetchData("GET", `api/user_details`, {}, token);
    return data;
  }

  React.useEffect(() => {
    async function loadUser() {
      const userInfo = await loadU();
      setUser(userInfo);
      setUserProfPic(userInfo.profilePic);
    }
    loadUser();
  }, []);

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
  };
  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  const logoHoverStyle = {
    cusor: "pointer",
    transform: "scale3d(1.05, 1.05, 1)",
    transition: "transform 0.15s ease-in-out",
  };
  const logoNoHoverStyle = { transition: "transform 0.15s ease-in-out" };

  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <RestaurantMenuIcon
            sx={{ display: { xs: "none", md: "flex" }, mr: 1 }}
          />
          <Typography
            variant="h6"
            noWrap
            component="a"
            onMouseEnter={() => setLogoHover(true)}
            onMouseLeave={() => setLogoHover(false)}
            style={logoHover ? logoHoverStyle : logoNoHoverStyle}
            onClick={() => {
              navigate("/");
            }}
            sx={{
              mr: 2,
              display: { xs: "none", md: "flex" },
              fontFamily: "monospace",
              fontWeight: 700,
              letterSpacing: ".3rem",
              color: "inherit",
              textDecoration: "none",
            }}
          >
            RATATOUILLE
          </Typography>

          <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}>
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleOpenNavMenu}
              color="inherit"
            >
              <MenuIcon />
            </IconButton>
            <Menu
              id="menu-appbar"
              anchorEl={anchorElNav}
              anchorOrigin={{
                vertical: "bottom",
                horizontal: "left",
              }}
              keepMounted
              transformOrigin={{
                vertical: "top",
                horizontal: "left",
              }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenu}
              sx={{
                display: { xs: "block", md: "none" },
              }}
            >
              <MenuItem
                onClick={() => {
                  navigate("/explore");
                  handleCloseNavMenu();
                }}
              >
                <Typography textAlign="center">Explore All Recipes</Typography>
              </MenuItem>

              <MenuItem
                onClick={() => {
                  navigate("/feed");
                  handleCloseNavMenu();
                }}
              >
                <Typography textAlign="center">Personal Feed</Typography>
              </MenuItem>

              <MenuItem
                onClick={() => {
                  navigate("/users");
                  handleCloseNavMenu();
                }}
              >
                <Typography textAlign="center">Explore Users</Typography>
              </MenuItem>

              <MenuItem
                onClick={() => {
                  navigate("/mealplan");
                  handleCloseNavMenu();
                }}
              >
                <Typography textAlign="center">My Meal Plan</Typography>
              </MenuItem>

              <MenuItem
                onClick={() => {
                  navigate("/search");
                  handleCloseNavMenu();
                }}
              >
                <Typography textAlign="center">Search Recipes</Typography>
              </MenuItem>
            </Menu>
          </Box>
          <RestaurantMenuIcon
            sx={{ display: { xs: "flex", md: "none" }, mr: 1 }}
          />
          <Typography
            variant="h5"
            noWrap
            component="a"
            onClick={() => {
              navigate("/");
            }}
            sx={{
              mr: 2,
              display: { xs: "flex", md: "none" },
              flexGrow: 1,
              fontFamily: "monospace",
              fontWeight: 700,
              letterSpacing: ".3rem",
              color: "inherit",
              textDecoration: "none",
            }}
            onMouseEnter={() => setLogoHover(true)}
            onMouseLeave={() => setLogoHover(false)}
            style={logoHover ? logoHoverStyle : logoNoHoverStyle}
          >
            RATATOUILLE
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: "none", md: "flex" } }}>
            <MenuItem
              onClick={() => {
                navigate("/explore");
                handleCloseNavMenu();
              }}
            >
              <Typography textAlign="center" sx={{ fontFamily: "monospace" }}>
                Explore Recipes
              </Typography>
            </MenuItem>

            <MenuItem
              onClick={() => {
                navigate("/feed");
                handleCloseNavMenu();
              }}
            >
              <Typography textAlign="center" sx={{ fontFamily: "monospace" }}>
                Personal Feed
              </Typography>
            </MenuItem>

            <MenuItem
              onClick={() => {
                navigate("/users");
                handleCloseNavMenu();
              }}
            >
              <Typography textAlign="center" sx={{ fontFamily: "monospace" }}>
                Explore Users
              </Typography>
            </MenuItem>

            <MenuItem
              onClick={() => {
                navigate("/mealplan");
                handleCloseNavMenu();
              }}
            >
              <Typography textAlign="center" sx={{ fontFamily: "monospace" }}>
                My Meal Plan
              </Typography>
            </MenuItem>

            <MenuItem
              onClick={() => {
                navigate("/search");
                handleCloseNavMenu();
              }}
            >
              <Typography textAlign="center" sx={{ fontFamily: "monospace" }}>
                Search Recipes
              </Typography>
            </MenuItem>
          </Box>

          <Box sx={{ flexGrow: 0 }}>
            <Tooltip title="Open settings">
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                {userProfPic ? (
                  <Avatar alt="user's profile picture" src={userProfPic} />
                ) : (
                  <Avatar alt="default profile picture" src={defaultPic} />
                )}
              </IconButton>
            </Tooltip>
            <Menu
              sx={{ mt: "45px" }}
              id="menu-appbar"
              anchorEl={anchorElUser}
              anchorOrigin={{
                vertical: "top",
                horizontal: "right",
              }}
              keepMounted
              transformOrigin={{
                vertical: "top",
                horizontal: "right",
              }}
              open={Boolean(anchorElUser)}
              onClose={handleCloseUserMenu}
            >
              <MenuItem
                onClick={() => {
                  navigate(`/profile/${user.id}`);
                  handleCloseNavMenu();
                  handleCloseUserMenu();
                }}
              >
                <Typography textAlign="center">My Profile</Typography>
              </MenuItem>
              <MenuItem
                onClick={() => {
                  navigate("/createrecipe");
                  handleCloseNavMenu();
                  handleCloseUserMenu();
                }}
              >
                <Typography textAlign="center">Create Recipe</Typography>
              </MenuItem>

              <MenuItem
                onClick={() => {
                  navigate("/makeable");
                  handleCloseNavMenu();
                  handleCloseUserMenu();
                }}
              >
                <Typography textAlign="center">Makeable Recipes</Typography>
              </MenuItem>

              <MenuItem
                onClick={() => {
                  navigate("/pantry");
                  handleCloseNavMenu();
                  handleCloseUserMenu();
                }}
              >
                <Typography textAlign="center">Pantry List</Typography>
              </MenuItem>

              <MenuItem
                onClick={() => {
                  navigate("/shoppinglist");
                  handleCloseNavMenu();
                  handleCloseUserMenu();
                }}
              >
                <Typography textAlign="center">Shopping List</Typography>
              </MenuItem>

              <MenuItem
                onClick={() => {
                  navigate("/personalsettings");
                  handleCloseNavMenu();
                  handleCloseUserMenu();
                }}
              >
                <Typography textAlign="center">Personal Settings</Typography>
              </MenuItem>

              <MenuItem
                onClick={() => {
                  setIsLoggedIn(false);
                  fetchData("POST", `api/logout`, { token: token }, null);
                  localStorage.clear();
                  navigate("/");
                  handleCloseNavMenu();
                }}
              >
                <Typography textAlign="center">Logout</Typography>
              </MenuItem>
            </Menu>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
}
