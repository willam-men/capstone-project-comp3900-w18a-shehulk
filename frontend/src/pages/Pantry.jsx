import React from "react";
import fetchData from "../helper.js";
import { useNavigate } from "react-router-dom";

import {
  Paper,
  TextField,
  Divider,
  Typography,
  Box,
  Button,
  Autocomplete,
} from "@mui/material";

export default function Pantry() {
  const token = localStorage.getItem("token");
  const navigate = useNavigate();

  const defaultIngredientErrorMsg =
    "Ingredients are validated against our database. If there are no matches, please select a similar ingredient.";
  const [pantryList, setPantryList] = React.useState([]);
  const [addIngredient, setAddIngredient] = React.useState("");
  const [ingredientsOptions, setIngredientsOptions] = React.useState([]);
  const [ingredientError, setIngredientError] = React.useState(false);
  const [ingredientErrorMsg, setIngredientErrorMsg] = React.useState(
    defaultIngredientErrorMsg
  );
  const [reset, setReset] = React.useState(true);

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

  // on load this calls the above function and fetches the recipes
  React.useEffect(() => {
    async function loadLists() {
      const pantryOutput = await loadPantry();
      setPantryList(pantryOutput);
    }
    loadLists();
  }, []);

  const removeFromPantry = (index, ingredient) => {
    const newPantry = [...pantryList];
    newPantry.splice(index, 1);
    setPantryList(newPantry);
    // post request
    fetchData("POST", "api/pantry", { add: [], delete: [ingredient] }, token);
  };

  const handleEnterAddIngredient = (e) => {
    if (e.key === "Enter") {
      setPantryList((pantryList) => [...pantryList, addIngredient]);
      // post request
      fetchData(
        "POST",
        "api/pantry",
        { add: [e.target.value], delete: [] },
        token
      );
      setAddIngredient("");
    }
  };

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

  const paperStyle = {
    padding: "100px",
    width: "70vw",
    margin: "50px auto",
    alignItems: "center",
  };
  const listStyle = { width: "400px", margin: "50px auto" };
  const ingredStyle = {
    display: "flex",
    justifyContent: "space-between",
    margins: "10px 5px",
    marginRight: "10px",
  };
  const ingredText = { marginTop: "5px" };
  const ingredInputStyle = { marginTop: "50px" };

  return (
    <>
      <Paper style={paperStyle}>
        <Typography variant="h4">Pantry</Typography>
        <Box style={listStyle}>
          {pantryList.map((ingredient, index) => (
            <Box>
              <Box style={ingredStyle}>
                <Typography style={ingredText}>{ingredient}</Typography>
                <Button onClick={() => removeFromPantry(index, ingredient)}>
                  Remove From Pantry
                </Button>
              </Box>
              <Divider light />
            </Box>
          ))}
        </Box>
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
        <br></br>
        <Button onClick={() => navigate("/shoppinglist")} variant="contained">
          Go To Shopping List
        </Button>
      </Paper>
    </>
  );
}
