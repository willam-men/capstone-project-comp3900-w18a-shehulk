import React from "react";
import {
  Typography,
  TextField,
  Box,
  Button,
  Autocomplete,
  CircularProgress,
} from "@mui/material";
import { mealTypeOptions } from "../RecipeTypes";
import fetchData from "../helper.js";
import { useNavigate } from "react-router-dom";

import SoupKitchenIcon from "@mui/icons-material/SoupKitchen";
import CoffeeIcon from "@mui/icons-material/Coffee";
import CakeIcon from "@mui/icons-material/Cake";
import CookieIcon from "@mui/icons-material/Cookie";
import BreakfastDiningIcon from "@mui/icons-material/BreakfastDining";
import DinnerDiningIcon from "@mui/icons-material/DinnerDining";
import RiceBowlIcon from "@mui/icons-material/RiceBowl";

export default function AdvancedSearch({ title }) {
  const navigate = useNavigate();

  const configureMeals = () => {
    let mTypes = [];
    for (let i = 0; i < mealTypeOptions.length; i++) {
      mTypes.push({ mealType: mealTypeOptions[i], selected: false });
    }
    return mTypes;
  };

  const [method, setMethod] = React.useState("");
  const [ingredients, setIngredients] = React.useState([]);
  const [mealTypes, setMealTypes] = React.useState(configureMeals());
  const [resetAdd, setResetAdd] = React.useState(true);
  const [resetRemove, setResetRemove] = React.useState(true);
  const [errorAdd, setErrorAdd] = React.useState(false);
  const [errorRemove, setErrorRemove] = React.useState(false);
  const [ingredientsOptions, setIngredientsOptions] = React.useState([]);

  async function loadIngredients() {
    const data = await fetchData("GET", `api/ingredients`, {});
    return data;
  }

  React.useEffect(() => {
    async function loadIngredient() {
      setIngredientsOptions(await loadIngredients());
    }
    loadIngredient();
  }, []);

  const ingredientValidation = (event) => {
    for (let index in ingredients) {
      if (ingredients[index].ingredient === event.target.value) {
        return false;
      }
    }
    return true;
  };

  const handleKeyDown = (event, type) => {
    if (event.key === "Enter" && event.value !== "") {
      if (
        ingredientValidation(event) &&
        ingredientsOptions.some((e) => e.ingredient === event.target.value)
      ) {
        setIngredients((ingredients) => [
          ...ingredients,
          {
            type: type,
            ingredient: event.target.value,
          },
        ]);
        setErrorAdd(false);
        setErrorRemove(false);
      } else {
        if (type === "+") {
          setErrorAdd(true);
        } else {
          setErrorRemove(true);
        }
      }
      if (type === "+") {
        setResetAdd(!resetAdd);
      } else {
        setResetRemove(!resetRemove);
      }
    }
  };

  const handleRemoveTag = (index) => {
    const newIngredients = [...ingredients];
    newIngredients.splice(index, 1);
    setIngredients(newIngredients);
  };

  const computeIcon = (mealType) => {
    switch (mealType) {
      case "Starter":
        return <SoupKitchenIcon />;
      case "Beverage":
        return <CoffeeIcon />;
      case "Breakfast":
        return <BreakfastDiningIcon />;
      case "Dessert":
        return <CakeIcon />;
      case "Main":
        return <DinnerDiningIcon />;
      case "Snack":
        return <CookieIcon />;
      case "Side":
        return <RiceBowlIcon />;
      default:
        return;
    }
  };

  const handleMealType = (mealType) => {
    setMealTypes(selectMealType(mealType));
  };

  const selectMealType = (mealType) => {
    const newMealT = [...mealTypes];
    for (let i = 0; i < mealTypes.length; i++) {
      if (newMealT[i].mealType === mealType) {
        newMealT[i].selected = !newMealT[i].selected;
      }
    }
    return newMealT;
  };

  const submitAdvSearch = () => {
    // navigate to page with /search/title?
    // construct search url
    let url = `/search/`;

    if (title !== "") {
      url = url + `title=${title}&`;
    }

    if (method !== "") {
      url = url + `method=${method}&`;
    }

    const includeexclude = extractIngredients();

    if (includeexclude.include.length !== 0) {
      url = url + `include=${constructIngredientUrl(includeexclude.include)}&`;
    }

    if (includeexclude.exclude.length !== 0) {
      url = url + `exclude=${constructIngredientUrl(includeexclude.exclude)}&`;
    }

    const mealTypeStr = constructMealTypeUrl();
    if (mealTypeStr !== "") {
      url = url + `mealtypes=${constructMealTypeUrl()}`;
    } else {
      url = url.slice(0, -1);
    }
    navigate(`${url}`);
  };

  const extractIngredients = () => {
    let include = [];
    let exclude = [];
    for (let i = 0; i < ingredients.length; i++) {
      if (ingredients[i].type === "+") {
        include.push(ingredients[i].ingredient);
      } else {
        exclude.push(ingredients[i].ingredient);
      }
    }
    return { include, exclude };
  };

  const constructIngredientUrl = (ingredients) => {
    let str = "";
    for (let i = 0; i < ingredients.length; i++) {
      str = str + `${ingredients[i]}`;
      if (i !== ingredients.length - 1) {
        str = str + `%2C`;
      }
    }
    return str;
  };

  const constructMealTypeUrl = () => {
    let str = "";
    for (let i = 0; i < mealTypes.length; i++) {
      if (mealTypes[i].selected === true) {
        str = str + `${mealTypes[i].mealType}%2C`;
      }
    }
    // remove %2C
    if (str !== "") {
      str = str.slice(0, -3);
    }
    return str;
  };

  const advSearchLabel = {
    padding: "10px",
    marginRight: "40px",
    marginTop: "10px",
  };
  const inputStyle = { width: "100%", margin: "0px" };
  const inputSection = { margin: "40px 0px" };
  const ingredSearchLabel = {
    marginLeft: "10px",
    marginRight: "0px",
    marginTop: "10px",
    textAlign: "left",
  };
  const ingredTags = { display: "flex", flexDirection: "row" };

  const tagStyle = {
    display: "flex",
    padding: "5px 10px",
    borderRadius: "25px",
    border: "2px solid #BBDEFB",
    margin: "5px",
    marginBottom: "30px",
  };
  const strikeThrough = {
    textDecoration: "line-through",
    marginRight: "20px",
    color: "#616161",
  };
  const normal = { marginRight: "20px", color: "#616161" };
  const crossStyle = {
    color: "#616161",
    padding: "0px 5px",
    margin: "0px",
    border: "none",
    backgroundColor: "white",
  };

  const mealLabelStyle = {
    textAlign: "left",
    display: "flex",
    justifyContent: "flex-start",
    marginLeft: "10px",
    marginBottom: "20px",
  };

  const flexStyle = {
    display: "flex",
    flexDirection: "row",
    justfyContent: "center",
    alignItems: "center",
    flexWrap: "wrap",
    alignContent: "spaceAround",
  };

  const submitStyle = { marginTop: "100px" };

  const ingredientStyle = {
    paddingLeft: "10%",
    minHeight: "30px",
    minWidth: "50%",
  };

  return (
    <>
      {ingredientsOptions.length === 0 ? (
        <Box sx={{ display: "flex" }}>
          <CircularProgress />
        </Box>
      ) : (
        <div>
          <Box sx={{ display: "flex" }} style={inputSection}>
            <Typography variant="h7" style={advSearchLabel}>
              Method
            </Typography>
            <TextField
              style={inputStyle}
              label="By Method"
              variant="outlined"
              onChange={(e) => {
                setMethod(e.target.value);
              }}
            />
          </Box>

          <Box
            sx={{ display: "flex", justifyContent: "space-between" }}
            style={inputSection}
          >
            <Box sx={{ display: "flex", width: "48%" }}>
              <Typography variant="h7" style={ingredSearchLabel}>
                Include Ingredients
              </Typography>
              <Autocomplete
                key={resetAdd}
                id="tags-standard"
                options={ingredientsOptions}
                getOptionLabel={(option) => option.ingredient}
                sx={ingredientStyle}
                onKeyDown={(e) => handleKeyDown(e, "+")}
                renderInput={(params) => (
                  <TextField
                    {...params}
                    variant="standard"
                    placeholder="Include Ingredients"
                    error={errorAdd}
                  />
                )}
              />
            </Box>
            <Box sx={{ display: "flex", width: "48%" }}>
              <Typography variant="h7" style={ingredSearchLabel}>
                Exclude Ingredients
              </Typography>
              <Autocomplete
                key={resetRemove}
                id="tags-standard"
                options={ingredientsOptions}
                getOptionLabel={(option) => option.ingredient}
                sx={ingredientStyle}
                onKeyDown={(e) => handleKeyDown(e, "-")}
                renderInput={(params) => (
                  <TextField
                    {...params}
                    variant="standard"
                    placeholder="Exclude Ingredients"
                    error={errorRemove}
                  />
                )}
              />
            </Box>
          </Box>
          <Box>
            <Box style={ingredTags}>
              {ingredients.map((data, index) => {
                return (
                  <Box style={tagStyle}>
                    <Typography
                      style={data.type === "-" ? strikeThrough : normal}
                    >
                      {data.ingredient}
                    </Typography>

                    <button
                      style={crossStyle}
                      onClick={(e) => handleRemoveTag(index)}
                    >
                      ×
                    </button>
                  </Box>
                );
              })}
            </Box>
          </Box>

          <Typography variant="h7" style={mealLabelStyle}>
            Meal Types
          </Typography>
          <div style={flexStyle}>
            {mealTypeOptions.map((mealType, index) => (
              <Button
                startIcon={computeIcon(mealType)}
                variant={
                  mealTypes[index].selected === true ? "contained" : "outlined"
                }
                style={{
                  marginRight: "20px",
                  width: "130px",
                  height: "50px",
                  marginBottom: "10px",
                  marginLeft: "10px",
                }}
                onClick={() => {
                  handleMealType(mealType);
                }}
                key={mealType}
              >
                {mealType}
              </Button>
            ))}
          </div>

          <Button
            variant="contained"
            onClick={submitAdvSearch}
            style={submitStyle}
          >
            Submit
          </Button>
        </div>
      )}
    </>
  );
}
