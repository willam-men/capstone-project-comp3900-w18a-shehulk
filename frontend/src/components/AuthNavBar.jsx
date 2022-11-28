import React from "react";
import {
  AppBar,
  Box,
  Toolbar,
  Typography,
  Container,
  MenuItem,
} from "@mui/material";
import RestaurantMenuIcon from "@mui/icons-material/RestaurantMenu";
import { useNavigate } from "react-router-dom";

export default function AuthNavBar() {
  const navigate = useNavigate();

  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <RestaurantMenuIcon sx={{ display: "flex", mr: 1 }} />
          <Typography
            variant="h6"
            noWrap
            component="a"
            onClick={() => {
              navigate("/");
            }}
            sx={{
              mr: 2,
              display: "flex",
              fontFamily: "monospace",
              fontWeight: 700,
              letterSpacing: ".3rem",
              color: "inherit",
              textDecoration: "none",
            }}
          >
            RATATOUILLE
          </Typography>

          <Box sx={{ flexGrow: 1, display: "flex" }}>
            <MenuItem
              onClick={() => {
                navigate("/explore");
              }}
            >
              <Typography textAlign="center" sx={{ fontFamily: "monospace" }}>
                Explore Recipes
              </Typography>
            </MenuItem>
            <MenuItem
              onClick={() => {
                navigate("/search");
              }}
            >
              <Typography textAlign="center" sx={{ fontFamily: "monospace" }}>
                Search Recipes
              </Typography>
            </MenuItem>
          </Box>

          <Box sx={{ display: "flex", justifyContent: "flex-end" }}>
            <MenuItem
              onClick={() => {
                navigate("/register");
              }}
            >
              <Typography textAlign="center" sx={{ fontFamily: "monospace" }}>
                Register
              </Typography>
            </MenuItem>
            <MenuItem
              onClick={() => {
                navigate("/login");
              }}
            >
              <Typography textAlign="center" sx={{ fontFamily: "monospace" }}>
                Login
              </Typography>
            </MenuItem>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
}
