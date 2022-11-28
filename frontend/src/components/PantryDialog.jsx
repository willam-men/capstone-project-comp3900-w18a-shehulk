import React from "react";
import fetchData from "../helper.js";
import {
  Typography,
  Box,
  Divider,
  Button,
  Autocomplete,
  DialogTitle,
  TextField,
} from "@mui/material";

export default function PantryDialog() {
  const defaultIngredientErrorMsg =
    "Ingredients are validated against our database. If there are no matches, please select a similar ingredient.";
  const token = localStorage.getItem("token");
  const [pantryList, setPantryList] = React.useState([]);
  const [allNeededIngredients, setAllNeededIngredients] = React.useState([]);
  const [shoppingList, setShoppingList] = React.useState([]);
  const [addIngredient, setAddIngredient] = React.useState("");
  const [ingredientsOptions, setIngredientsOptions] = React.useState([]);
  const [reset, setReset] = React.useState(true);
  const [ingredientError, setIngredientError] = React.useState(false);
  const [ingredientErrorMsg, setIngredientErrorMsg] = React.useState(
    defaultIngredientErrorMsg
  );

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

  // fetch ingredients in pantry
  async function loadPantry() {
    const data = await fetchData("GET", "api/pantry", {}, token);
    return data.pantry;
  }

  // fetch ingredients to buy
  async function loadShoppingList() {
    const data = await fetchData(
      "GET",
      "api/missing_ingredients",
      { token: token },
      token
    );
    return data.ingredients;
  }

  // fetch all required ingredients in meal plan
  async function loadAllIngredients() {
    const data = await fetchData(
      "GET",
      "api/meal_plan/ingredients",
      { token: token },
      token
    );
    return data;
  }

  // validate ingredient is valid
  const validateIngredients = (ingredient) => {
    if (!ingredient) {
      setIngredientError(true);
      setIngredientErrorMsg(
        "Please enter an ingredient. If there are no matches, please select a similar ingredient."
      );
      return false;
    } else if (!ingredientsOptions.some((e) => e.ingredient === ingredient)) {
      setIngredientError(true);
      setIngredientErrorMsg(
        "This is not a valid ingredient. If there are no matches, please select a similar ingredient."
      );
      return false;
    } else {
      // check whether pantry already contains ingredient
      for (let index in pantryList) {
        if (pantryList[index] === ingredient) {
          setIngredientError(true);
          setIngredientErrorMsg(
            "This ingredient has already been added into the ingredients list. Please add a new ingredient"
          );
          return false;
        }
      }
      setIngredientError(false);
      setIngredientErrorMsg(defaultIngredientErrorMsg);
      return true;
    }
  };

  // on load this calls the above function and fetches the recipes
  React.useEffect(() => {
    async function loadLists() {
      const pantryOutput = await loadPantry();
      setPantryList(pantryOutput);
      const shoppingOutput = await loadShoppingList();
      setShoppingList(shoppingOutput.sort((a, b) => a.localeCompare(b)));
      const allIngredients = await loadAllIngredients();
      setAllNeededIngredients(allIngredients);
    }
    loadLists();
  }, []);

  const handleEnterAddIngredient = (e) => {
    if (addIngredient) {
      setPantryList((pantryList) => [...pantryList, addIngredient]);
      // post request
      fetchData(
        "POST",
        "api/pantry",
        { add: [e.target.value], delete: [] },
        token
      );
    }
  };

  const handleRemoveIngredientPantry = (index, ingredient) => {
    const newPantry = [...pantryList];
    newPantry.splice(index, 1);
    setPantryList(newPantry);
    // post request
    fetchData("POST", "api/pantry", { add: [], delete: [ingredient] }, token);
    // if the deleted ingredient was originally in shopping list add it back
    if (allNeededIngredients.includes(ingredient)) {
      setShoppingList((shoppingList) => [...shoppingList, ingredient]);
    }
  };

  const handleAddIngredientToPantry = (index, ingredient) => {
    // post request
    fetchData("POST", "api/pantry", { add: [ingredient], delete: [] }, token);
    // add to pantry frontend
    setPantryList((pantryList) => [...pantryList, ingredient]);
    // remove from shopping front end
    const newShopping = [...shoppingList];
    newShopping.splice(index, 1);
    setShoppingList(newShopping);
  };

  const flexStyle = {
    display: "flex",
    justifyContent: "flexStart",
    padding: "0px 25px",
  };
  const ingredStyle = {
    display: "flex",
    justifyContent: "space-between",
    margins: "10px 5px",
    marginRight: "10px",
  };
  const ingredText = { marginTop: "5px" };
  const partitionStyle = { width: "200px" };

  const splitStyle = { width: "50%" };
  const dividerStyle = { marginBottom: "20px", marginTop: "10px" };
  const ingredInputStyle = { marginTop: "50px" };

  return (
    <>
      <DialogTitle variant="h5">Manage Pantry and Shopping List</DialogTitle>
      <Divider variant="middle" style={dividerStyle} />
      <Box style={flexStyle}>
        <Box style={splitStyle}>
          <Typography variant="h6">Pantry</Typography>
          {pantryList.map((ingredient, index) => (
            <Box>
              <Box style={ingredStyle}>
                <Typography style={ingredText}>{ingredient}</Typography>
                <Button
                  onClick={() =>
                    handleRemoveIngredientPantry(index, ingredient)
                  }
                >
                  Remove
                </Button>
              </Box>
              <Divider light />
            </Box>
          ))}
          <Autocomplete
            style={ingredInputStyle}
            key={reset}
            id="tags-standard"
            options={ingredientsOptions}
            getOptionLabel={(option) => option.ingredient}
            sx={{ minHeight: "30px" }}
            onChange={(e, v) => {
              if (v == null) {
                setAddIngredient("");
                setIngredientError(false);
                setIngredientErrorMsg(defaultIngredientErrorMsg);
              } else {
                setAddIngredient(v.ingredient);
              }
            }}
            renderInput={(params) => (
              <TextField
                {...params}
                variant="outlined"
                helperText={ingredientErrorMsg}
                error={ingredientError}
                label="Add Ingredient To Pantry"
                onKeyDown={(e) => {
                  if (e.key === "Enter" && addIngredient !== "") {
                    if (validateIngredients(e.target.value)) {
                      handleEnterAddIngredient(e);
                      setReset(!reset);
                      setAddIngredient("");
                    }
                  }
                }}
              />
            )}
          />
        </Box>
        <Box style={partitionStyle}></Box>
        <Box style={splitStyle}>
          <Typography variant="h6">Shopping List</Typography>
          {shoppingList.map((ingredient, index) => (
            <Box>
              <Box style={ingredStyle}>
                <Typography style={ingredText}>{ingredient}</Typography>
                <Button
                  onClick={() => handleAddIngredientToPantry(index, ingredient)}
                >
                  Add To Pantry
                </Button>
              </Box>
              <Divider light />
            </Box>
          ))}
        </Box>
      </Box>
    </>
  );
}
