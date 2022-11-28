import React from "react";
import fetchData from "../helper.js";
import { useParams, useNavigate } from "react-router-dom";
import {
  Typography,
  Box,
  CircularProgress,
  Grid,
  Button,
  Fab,
} from "@mui/material";
import RecipeCard from "../components/RecipeCard";
import NavigationIcon from "@mui/icons-material/Navigation";

export default function SearchResults() {
  const params = useParams();
  const [loading, setLoading] = React.useState(true);
  const [recipeData, setRecipeData] = React.useState(null);
  const [isResults, setIsResults] = React.useState(false);
  const [showScroll, setShowScroll] = React.useState(false);
  const navigate = useNavigate();

  async function loadRecipe() {
    const data = await fetchData("GET", `api/search?${params.terms}`, {});
    return data;
  }

  React.useEffect(() => {
    async function loadreceipts() {
      const recipeOutput = await loadRecipe();
      if (recipeOutput.length !== 0) {
        setIsResults(true);
      }
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

  const navigateToSearch = () => {
    navigate("/search");
  };

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
            Search Results
          </Typography>
          {isResults ? (
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
            <Typography>No recipes found.</Typography>
          )}

          <Button
            variant="contained"
            onClick={navigateToSearch}
            sx={{ marginTop: "20px", marginBottom: "30px" }}
          >
            Back to Search
          </Button>
          <br></br>
        </Box>
      )}
    </>
  );
}
