import React from "react";
import { Typography, Button, Box } from "@mui/material";
import { useNavigate } from "react-router-dom";

export default function NotFound() {
  const navigate = useNavigate();
  const navigateExplore = () => {
    navigate("/explore");
  };

  return (
    <>
      <Box sx={{ justifyContent: "center", paddingTop: "5%" }}>
        <Typography variant="h1">404</Typography>
        <Typography variant="h6">
          The page you are looking for doesn't exist
        </Typography>
        <br />
        <Button variant="contained" onClick={navigateExplore}>
          Back to Explore
        </Button>
      </Box>
    </>
  );
}
