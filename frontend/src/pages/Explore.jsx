import React from "react";
import fetchData from "../helper.js";
import {
  Typography,
  Box,
  Button,
  CircularProgress,
  Grid,
  Fab,
} from "@mui/material";
import RecipeCard from "../components/RecipeCard";
import { useNavigate } from "react-router-dom";
import NavigationIcon from "@mui/icons-material/Navigation";

export default function Explore() {
  const [recipeData, setRecipeData] = React.useState(null);
  const [loading, setLoading] = React.useState(true);
  const token = localStorage.getItem("token");
  const [showScroll, setShowScroll] = React.useState(false);

  const navigate = useNavigate();

  // this fetches all the recipes
  async function loadRecipes() {
    const data = await fetchData("GET", "api/recipes", {});
    return data;
  }

  // on load this calls the above function and fetches the recipes
  React.useEffect(() => {
    async function loadreceipts() {
      const recipeOutput = await loadRecipes();
      setRecipeData(recipeOutput);
      setLoading(false);
    }
    loadreceipts();
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

  const navigateCreateRecipe = () => {
    navigate("/createrecipe");
  };

  const titleStyle = { margin: "40px" };
  const boxStyle = {
    margin: "10px",
    display: "flex",
    justfyContent: "center",
    alignItems: "center",
    width: "100%",
  };
  const flexStyle = { display: "flex", justifyContent: "flexStart" };
  const buttonStyle = { margin: "40px" };

  const fabStyle = {
    position: "fixed",
    bottom: 16,
    right: 16,
  };

  const pageStyle = { width: "100%" };

  return (
    <>
      {loading ? (
        <Box>
          <CircularProgress />
        </Box>
      ) : (
        <Box style={pageStyle}>
          <Box style={flexStyle}>
            <Box class="alignleft"></Box>
            <Box class="aligncenter">
              <Typography variant="h4" style={titleStyle}>
                Explore Recipes
              </Typography>
            </Box>
            {token !== null ? (
              <Box class="alignright">
                <Button
                  style={buttonStyle}
                  variant="contained"
                  onClick={navigateCreateRecipe}
                >
                  Create New Recipe
                </Button>
              </Box>
            ) : (
              <Box></Box>
            )}
          </Box>
          <Box style={boxStyle}>
            <Grid
              container
              spacing={{ xs: 2, md: 3 }}
              columns={{ xs: 4, sm: 8, md: 12 }}
              direction="row"
              alignItems="center"
              justifyContent="center"
            >
              {recipeData.map((recipe, index) => {
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
                    <RecipeCard recipe={recipe} />
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
