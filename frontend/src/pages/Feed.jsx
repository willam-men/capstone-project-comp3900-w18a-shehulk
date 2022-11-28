import React from "react";
import fetchData from "../helper.js";
import {
  Typography,
  Box,
  CircularProgress,
  Grid,
  Button,
  Fab,
} from "@mui/material";
import RecipeCard from "../components/RecipeCard";
import { useNavigate } from "react-router-dom";
import NavigationIcon from "@mui/icons-material/Navigation";

export default function Feed() {
  const token = localStorage.getItem("token");
  const navigate = useNavigate();

  const [recipeData, setRecipeData] = React.useState(null);
  const [loading, setLoading] = React.useState(true);
  const [isRecipes, setIsRecipes] = React.useState(false);
  const [showScroll, setShowScroll] = React.useState(false);

  // this fetches all the recipes
  async function loadRecipes() {
    const data = await fetchData("GET", "api/personalised_recipes", {}, token);
    return data;
  }

  // on load this calls the above function and fetches the recipes
  React.useEffect(() => {
    async function loadreceipts() {
      const recipeOutput = await loadRecipes();
      setRecipeData(recipeOutput);
      if (recipeOutput.length !== 0) {
        setIsRecipes(true);
      }
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

  const titleStyle = { margin: "40px" };
  const boxStyle = {
    margin: "10px",
    display: "flex",
    justfyContent: "center",
    width: "100%",
  };
  const buttonStyle = { margin: "40px" };
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
            Personal Feed
          </Typography>

          {isRecipes ? (
            <Box style={boxStyle}>
              <Grid
                container
                spacing={{ xs: 2, md: 3 }}
                columns={{ xs: 4, sm: 8, md: 12 }}
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
          ) : (
            <Box>
              <Typography>
                No recipes from subscribed users was found.
              </Typography>
              <Button style={buttonStyle} onClick={() => navigate("/users")}>
                Find Users to Subscribe To
              </Button>
            </Box>
          )}
        </Box>
      )}
    </>
  );
}
