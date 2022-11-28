import React from "react";
import { useParams, useNavigate } from "react-router-dom";
import RecipeCreateBasic from "../components/RecipeCreateBasic";
import RecipeAddIngredients from "../components/RecipeAddIngredients";
import RecipeAddSteps from "../components/RecipeAddSteps";
import RecipeTags from "../components/RecipeTags";
import ProgressBar from "../components/ProgressBar";

import { Typography, Button, Box, CircularProgress } from "@mui/material";
import fetchData from "../helper.js";

export default function RecipeEdit() {
  const params = useParams();
  const recipeId = params.recipeid;
  const [loading, setLoading] = React.useState(true);
  const [formData, setFormData] = React.useState(null);
  const token = localStorage.getItem("token");

  async function loadRecipe() {
    const data = await fetchData(
      "GET",
      `api/recipe/user?recipeId=${recipeId}`,
      {},
      token
    );
    return data;
  }

  React.useEffect(() => {
    async function LoadReceipts() {
      const recipeOutput = await loadRecipe();
      if ("code" in recipeOutput) {
        navigate("/notfound");
      }
      setLoading(false);
      const prepTime = recipeOutput.prepTime.trim().split(/\s+/);
      const cookTime = recipeOutput.cookTime.trim().split(/\s+/);

      const prepHours = parseInt(prepTime[0]);
      const prepMins = parseInt(prepTime[2]);
      const cookHours = parseInt(cookTime[0]);
      const cookMins = parseInt(cookTime[2]);

      setFormData({
        title: recipeOutput.title,
        description: recipeOutput.description,
        imageUrl: recipeOutput.photo,
        selectedImage: null,
        servings: recipeOutput.servings,
        difficulty: recipeOutput.difficulty,
        prepHours: prepHours,
        prepMins: prepMins,
        cookHours: cookHours,
        cookMins: cookMins,
        utensils: recipeOutput.utensils,
        ingredients: recipeOutput.ingredients,
        steps: recipeOutput.method,
        mealType: recipeOutput.mealType,
        cuisines: recipeOutput.cuisine,
        dietaries: recipeOutput.dietaries,
      });
    }
    LoadReceipts();
  }, []);

  const navigate = useNavigate();
  const [page, setPage] = React.useState(0);

  let [validateData, setValidateData] = React.useState(false);

  const validateFirstPage = () => {
    if (
      formData.title === "" ||
      formData.servings === "" ||
      formData.difficulty === ""
    ) {
      return false;
    }
    return true;
  };

  const validateSecondPage = () => {
    if (formData.ingredients.length === 0) {
      return false;
    }
    return true;
  };

  const validateThirdPage = () => {
    if (formData.steps.length === 0) {
      return false;
    }
    return true;
  };

  const validateLastPage = () => {
    if (formData.cuisines.length === 0 || !formData.mealType) {
      return false;
    }
    return true;
  };

  const conditionalComponent = () => {
    switch (page) {
      case 0:
        return (
          <RecipeCreateBasic
            formData={formData}
            setFormData={setFormData}
            validateData={validateData}
          />
        );
      case 1:
        return (
          <RecipeAddIngredients
            formData={formData}
            setFormData={setFormData}
            validateData={validateData}
          />
        );
      case 2:
        return (
          <RecipeAddSteps
            formData={formData}
            setFormData={setFormData}
            validateData={validateData}
          />
        );
      case 3:
        return (
          <RecipeTags
            formData={formData}
            setFormData={setFormData}
            validateData={validateData}
          />
        );
      default:
        return;
    }
  };

  const navigateToPage = (recipeId) => {
    navigate(`/recipe/${recipeId}`);
  };

  async function HandleSubmit() {
    setValidateData(true);
    if (validateLastPage()) {
      const prepTime =
        formData.prepHours.toString() +
        " hours " +
        formData.prepMins.toString() +
        " mins ";
      const cookTime =
        formData.cookHours.toString() +
        " hours " +
        formData.cookMins.toString() +
        " mins ";
      const token = localStorage.getItem("token");

      const form = {
        id: recipeId,
        title: formData.title,
        description: formData.description,
        utensils: formData.utensils,
        ingredients: formData.ingredients,
        servings: formData.servings,
        method: formData.steps,
        difficulty: formData.difficulty,
        mealType: formData.mealType,
        cuisine: formData.cuisines,
        dietaries: formData.dietaries,
        photo: formData.imageUrl,
        prepTime: prepTime,
        cookTime: cookTime,
        token: token,
      };

      await fetchData("POST", "api/recipe/save", form, null);
      navigateToPage(recipeId);
    }
  }

  function moveNextPage() {
    setValidateData(true);
    switch (page) {
      case 0:
        if (validateFirstPage()) {
          setPage(1);
          setValidateData(false);
        }
        break;
      case 1:
        if (validateSecondPage()) {
          setPage(2);
          setValidateData(false);
        }
        break;
      case 2:
        if (validateThirdPage()) {
          setPage(3);
          setValidateData(false);
        }
        break;
      case 3:
        if (validateLastPage()) {
          setValidateData(false);
          // try submitting and return to home page if successful
        }
        break;
      default:
        break;
    }
  }

  const marginStyle = {
    paddingTop: "5%",
    paddingBottom: "5%",
    paddingLeft: "15%",
    paddingRight: "15%",
  };
  const headingStyle = { paddingBottom: "50px" };

  return (
    <>
      {loading ? (
        <Box sx={{ display: "flex" }}>
          <CircularProgress />
        </Box>
      ) : (
        <Box style={marginStyle} alignItems="center" justifyContent="center">
          <Typography variant="h3" style={headingStyle}>
            Edit a Recipe
          </Typography>
          <ProgressBar page={page} />
          <br />
          {conditionalComponent()}
          {page > 0 && (
            <Button
              variant="contained"
              style={{ marginRight: "5px" }}
              onClick={() => setPage(page - 1)}
            >
              Back
            </Button>
          )}
          {page < 3 && (
            <Button
              variant="contained"
              style={{ marginLeft: "5px" }}
              onClick={moveNextPage}
            >
              Next
            </Button>
          )}
          {page === 3 && (
            <Button
              variant="contained"
              style={{ marginLeft: "5px" }}
              onClick={HandleSubmit}
            >
              Submit
            </Button>
          )}
        </Box>
      )}
    </>
  );
}
