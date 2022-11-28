import React from "react";
import { useNavigate } from "react-router-dom";
import RecipeCreateBasic from "../components/RecipeCreateBasic";
import RecipeAddIngredients from "../components/RecipeAddIngredients";
import RecipeAddSteps from "../components/RecipeAddSteps";
import RecipeTags from "../components/RecipeTags";
import fetchData from "../helper.js";
import ProgressBar from "../components/ProgressBar";

import { Typography, Button, Box } from "@mui/material";

export default function RecipeCreate() {
  const navigate = useNavigate();
  const [page, setPage] = React.useState(0);
  const token = localStorage.getItem("token");
  const [formData, setFormData] = React.useState({
    title: "",
    description: "",
    imageUrl: null,
    selectedImage: null,
    servings: "",
    difficulty: "",
    prepHours: 0,
    prepMins: 0,
    cookHours: 0,
    cookMins: 0,
    utensils: [],
    ingredients: [],
    steps: [],
    mealType: "",
    cuisines: [],
    dietaries: [],
  });

  let [validateData, setValidateData] = React.useState(false);

  React.useEffect(() => {
    if (token === null) {
      navigate("/notfound");
    }
  }, [token, navigate]);

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

  async function handleSubmit() {
    setValidateData(true);
    if (validateLastPage()) {
      const prepTime =
        formData.prepHours.toString() +
        " hours " +
        formData.prepMins.toString() +
        " mins";
      const cookTime =
        formData.cookHours.toString() +
        " hours " +
        formData.cookMins.toString() +
        " mins";
      const token = localStorage.getItem("token");

      const form = {
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

      const recipe = await fetchData("POST", "api/recipe/create", form, null);
      navigateToPage(recipe.id);
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

  function moveBack() {
    setPage(page - 1);
  }

  const marginStyle = {
    paddingTop: "5%",
    paddingBottom: "5%",
    paddingLeft: "15%",
    paddingRight: "15%",
  };
  const headingStyle = { paddingBottom: "50px" };

  return (
    <Box style={marginStyle} alignItems="center" justifyContent="center">
      <Typography variant="h3" style={headingStyle}>
        Create a New Recipe
      </Typography>
      <ProgressBar page={page} />
      <br></br>
      {conditionalComponent()}
      <div
        style={{
          position: "sticky",
          bottom: "0px",
          paddingBottom: "20px",
          background: "white",
        }}
      >
        {page > 0 && (
          <Button
            variant="contained"
            style={{ marginRight: "5px" }}
            onClick={moveBack}
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
            onClick={handleSubmit}
          >
            Submit
          </Button>
        )}
      </div>
    </Box>
  );
}
